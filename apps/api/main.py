from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from fastapi.middleware.cors import CORSMiddleware
import sys, pathlib, os, re, json, sqlite3, io, csv, time, hashlib, datetime
from dotenv import load_dotenv
import httpx

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from gokai import AIPsycheGOKAI, s_gok, fibonacci

load_dotenv(dotenv_path=ROOT / ".env", override=True)

app = FastAPI(title="MTA Quest API", version="0.3.0")

# CORS
origins = (os.getenv("CORS_ORIGINS") or "http://localhost").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in origins if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data paths
DATA_DIR = ROOT / "data"
UPLOAD_DIR = ROOT / "uploads" / "tracks"
DATA_DIR.mkdir(parents=True, exist_ok=True)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# SQLite (events + drift)
DB_PATH = DATA_DIR / "events.sqlite"
def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

with db() as c:
    c.execute("""CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ts REAL NOT NULL,
        event TEXT NOT NULL,
        user TEXT,
        meta TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS drift_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL,
        updated REAL NOT NULL
    )""")
    c.commit()

psyche = AIPsycheGOKAI()

class GOKAIInput(BaseModel):
    W: Optional[int] = None; M: Optional[int] = None; D: Optional[int] = None
    C: Optional[int] = None; A: Optional[int] = None; E: Optional[int] = None; T: Optional[int] = None

class MatrixInput(BaseModel):
    identity_matrix: Optional[List[int]] = Field(default=None, description="6-length vector like [3,6,9,9,6,3]")

class SGOKInput(BaseModel):
    n: int = 10

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[ChatMessage]
    model: Optional[str] = None
    params: Optional[dict] = None

def reduce9(s: str) -> int:
    digits = re.findall(r"\d", s)
    if not digits: 
        return 0
    total = sum(int(d) for d in digits)
    m9 = total % 9
    return 9 if m9 == 0 and total>0 else m9

async def provider_chat(messages: List[Dict[str, str]], model: Optional[str]=None) -> str:
    provider = (os.getenv("PROVIDER") or "openai").lower()
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        mdl = model or os.getenv("OPENAI_MODEL") or "gpt-4o-mini"
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY missing. Set it in .env")
        payload = {"model": mdl, "messages": messages}
        async with httpx.AsyncClient(timeout=60) as client:
            r = await client.post("https://api.openai.com/v1/chat/completions",
                                  headers={"Authorization": f"Bearer {api_key}",
                                           "Content-Type":"application/json"},
                                  json=payload)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"]
    else:
        raise RuntimeError(f"Unsupported PROVIDER: {provider}")

@app.post("/api/gokai/calculate")
def calculate(inp: GOKAIInput):
    for k, v in inp.dict(exclude_none=True).items():
        setattr(psyche, k, int(v))
    ps = psyche.calculate_success_probability()
    phase = psyche.assess_development_phase().name
    return {"probability": ps, "phase": phase, "matrix": psyche.identity_matrix}

@app.post("/api/evolve/matrix")
def evolve(inp: MatrixInput):
    if inp.identity_matrix:
        psyche.identity_matrix = tuple(map(int, inp.identity_matrix[:6]))
    phase = psyche.assess_development_phase()
    mat = psyche.evolve_identity_matrix(phase)
    return {"phase": phase.name, "matrix": mat}

@app.get("/api/gaia/status")
def gaia_status():
    return {"temperature": 15.0, "humidity": 0.6, "co2": 400.0, "health_index": 0.72}

@app.post("/api/gokai/sgok")
def sgok_endpoint(inp: SGOKInput):
    return {"n": inp.n, "S": s_gok(inp.n)}

@app.post("/api/chat")
async def chat(req: ChatRequest):
    user_msg = next((m.content for m in reversed(req.messages) if m.role == "user"), "")
    try:
        content = await provider_chat([m.dict() for m in req.messages], req.model)
        log_event("chat_provider", meta={"ok": True})
        return {"role": "assistant", "content": content}
    except Exception as e:
        nums = re.findall(r"-?\d+(?:\.\d+)?", user_msg)
        reply_lines = []
        a = getattr(psyche, "W", 7)
        b = getattr(psyche, "T", 3)
        x = float(nums[0]) if nums else 1.0
        y = a*x + b
        reply_lines.append(f"Fallback (heurystycznie) — y = a·x + b → {a}·{x} + {b} = **{y:.4f}**")
        n = int(float(nums[1])) if len(nums) > 1 else 10
        reply_lines.append(f"S(GOK:AI) = 9π + F({n}) = **{s_gok(n):.6f}** (F({n})={fibonacci(n)})")
        m9 = reduce9(user_msg)
        reply_lines.append(f"Σ(digits) mod 9 = **{m9}** → {'Zamknięcie cyklu' if m9==9 else 'W trakcie cyklu'}")
        ps = psyche.calculate_success_probability()
        reply_lines.append(f"P(S) = **{ps:.3f}**; faza = **{psyche.assess_development_phase().name}**; matryca = {psyche.identity_matrix}")
        log_event("chat_fallback", meta={"error": str(e)})
        return {"role": "assistant", "content": "\n".join(reply_lines)}

@app.post("/api/hiphop/upload")
async def hiphop_upload(file: UploadFile = File(...), author: Optional[str] = Form(None)):
    safe_name = file.filename.replace("/", "_").replace("\\", "_")
    data = await file.read()
    path = UPLOAD_DIR / safe_name
    with open(path, "wb") as f:
        f.write(data)
    token_id = hashlib.sha1((safe_name + str(len(data))).encode()).hexdigest()[:16]
    meta = {"title": safe_name, "author": author or "unknown", "size": len(data),
            "token_id": token_id, "uri": f"/api/hiphop/download/{safe_name}"}
    log_event("hiphop_upload", meta=meta)
    return {"status": "ok", "track": meta}

@app.get("/api/hiphop/list")
def hiphop_list():
    items = []
    for name in os.listdir(UPLOAD_DIR):
        p = UPLOAD_DIR / name
        if p.is_file():
            items.append({"name": name, "size": p.stat().st_size})
    return {"tracks": items}

@app.get("/api/hiphop/download/{name}")
def hiphop_download(name: str):
    path = UPLOAD_DIR / name
    if not path.exists():
        return {"error": "not_found"}
    return FileResponse(path)

class DriftScore(BaseModel):
    name: str
    score: int

@app.get("/api/drift/leaderboard")
def drift_leaderboard(limit: int = 20):
    with db() as c:
        rows = c.execute("SELECT name, score, updated FROM drift_scores ORDER BY score DESC, updated ASC LIMIT ?", (limit,)).fetchall()
        data = [{"name": r["name"], "score": r["score"], "updated": r["updated"]} for r in rows]
        return {"leaderboard": data}

@app.post("/api/drift/score")
def drift_set_score(payload: DriftScore):
    with db() as c:
        now = time.time()
        row = c.execute("SELECT id, score FROM drift_scores WHERE name=?", (payload.name,)).fetchone()
        if row is None:
            c.execute("INSERT INTO drift_scores(name, score, updated) VALUES(?,?,?)", (payload.name, payload.score, now))
        else:
            new_score = max(payload.score, row["score"])
            c.execute("UPDATE drift_scores SET score=?, updated=? WHERE id=?", (new_score, now, row["id"]))
        c.commit()
    log_event("drift_score", meta={"name": payload.name, "score": payload.score})
    return {"ok": True}

class EventPayload(BaseModel):
    event: str
    user: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None

def log_event(event: str, user: Optional[str]=None, meta: Optional[Dict[str, Any]]=None):
    with db() as c:
        c.execute("INSERT INTO events(ts, event, user, meta) VALUES(?,?,?,?)",
                  (time.time(), event, user, json.dumps(meta or {})))
        c.commit()

@app.post("/api/events/log")
def events_log(p: EventPayload):
    log_event(p.event, p.user, p.meta)
    return {"ok": True}

@app.get("/api/events/export.csv")
def events_export_csv():
    with db() as c:
        rows = c.execute("SELECT ts, event, user, meta FROM events ORDER BY ts ASC").fetchall()
        output = io.StringIO()
        w = csv.writer(output)
        w.writerow(["ts_iso", "event", "user", "meta_json"])
        for r in rows:
            ts_iso = datetime.datetime.utcfromtimestamp(r["ts"]).isoformat() + "Z"
            w.writerow([ts_iso, r["event"], r["user"] or "", r["meta"] or "{}"])
        output.seek(0)
        return StreamingResponse(iter([output.read()]), media_type="text/csv", headers={"Content-Disposition":"attachment; filename=events.csv"})
