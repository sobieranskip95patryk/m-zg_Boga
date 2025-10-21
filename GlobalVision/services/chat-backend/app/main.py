from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os, json, pathlib, joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_DIR = pathlib.Path(os.getenv("GV_DATA_DIR", "data/knowledge"))
SRC_DIR = DATA_DIR / "source"
IDX_DIR = DATA_DIR / "index"
IDX_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="GlobalVision Chat Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    question: str
    top_k: int = 5

def load_corpus():
    docs = []
    paths = []
    for p in SRC_DIR.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".txt", ".md"}:
            try:
                txt = p.read_text(encoding="utf-8")
            except Exception:
                try:
                    txt = p.read_text(encoding="latin-1", errors="ignore")
                except Exception:
                    continue
            docs.append(txt)
            paths.append(str(p.relative_to(SRC_DIR)))
    return docs, paths

def load_index():
    vec_path = IDX_DIR / "vectorizer.joblib"
    mat_path = IDX_DIR / "matrix.joblib"
    meta_path = IDX_DIR / "meta.json"
    if vec_path.exists() and mat_path.exists() and meta_path.exists():
        vectorizer = joblib.load(vec_path)
        matrix = joblib.load(mat_path)
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        return vectorizer, matrix, meta
    return None, None, None

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/ingest")
def ingest():
    docs, paths = load_corpus()
    if not docs:
        return {"ok": False, "message": "Brak dokumentów .txt/.md w data/knowledge/source"}
    vectorizer = TfidfVectorizer(max_features=50000, ngram_range=(1,2))
    matrix = vectorizer.fit_transform(docs)
    IDX_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(vectorizer, IDX_DIR / "vectorizer.joblib")
    joblib.dump(matrix, IDX_DIR / "matrix.joblib")
    (IDX_DIR / "meta.json").write_text(json.dumps({"paths": paths}, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"ok": True, "docs": len(docs)}

@app.post("/chat")
def chat(req: ChatRequest):
    vectorizer, matrix, meta = load_index()
    if vectorizer is None:
        return {"ok": False, "message": "Brak indeksu. Uruchom /ingest najpierw."}
    q_vec = vectorizer.transform([req.question])
    sims = cosine_similarity(q_vec, matrix)[0]
    idxs = sims.argsort()[::-1][:req.top_k]
    results = []
    for i in idxs:
        results.append({"score": float(sims[i]), "path": meta["paths"][i]})
    snippets = []
    for r in results:
        full_path = SRC_DIR / r["path"]
        try:
            txt = full_path.read_text(encoding="utf-8")
        except Exception:
            txt = full_path.read_text(encoding="latin-1", errors="ignore")
        snippets.append(txt[:1200])
    answer = "Najbardziej powiązane fragmenty:\n\n" + "\n\n---\n\n".join(snippets)
    return {"ok": True, "answer": answer, "contexts": results}
