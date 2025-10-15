import React, { useEffect, useRef, useState } from "react";

// MTAQuestWebsideX — hybrydowy frontend (neon cyan → violet)
// Integracja z: SpiralMind‑Nexus (GOK:AI) i Apex Infinity MIGI Core.
// Tailwind wymagany w hostującej aplikacji.

/**
 * PROBLEM: Niektóre toolchainy nie akceptują odwołań do `import.meta` poza ESM,
 * co wywołało błąd parsera. Żeby było pancernie:
 *  - NIE używamy `import.meta.env` w runtime.
 *  - Czytamy tylko z process.env (jeśli istnieje) i z window.__CONFIG__.
 *  - Zostawiamy fallback na localhosty.
 */

// Czysta funkcja do testowania priorytetu źródeł (używana też w mini‑testach)
export function resolveEnvOrder(
  keyNext: string,
  keyWin: string,
  envObj: Record<string, string | undefined> | undefined,
  winObj: Record<string, string | undefined> | undefined,
  fallback = ""
): string {
  return (
    (envObj ? envObj[keyNext] : undefined) ??
    (winObj ? winObj[keyWin] : undefined) ??
    fallback
  ) ?? "";
}

// Wrapper na globalne źródła (bez `import.meta`)
function getEnv(keyNext: string, keyWin: string, fallback = ""): string {
  // globalThis działa w przeglądarce i node
  const g: any = typeof globalThis !== "undefined" ? (globalThis as any) : {};
  const envObj = g?.process?.env as Record<string, string | undefined> | undefined;
  const winObj = g?.__CONFIG__ as Record<string, string | undefined> | undefined;
  return resolveEnvOrder(keyNext, keyWin, envObj, winObj, fallback);
}

// Adresy bazowe (możesz nadpisać przez NEXT_PUBLIC_* lub __CONFIG__)
const SPIRALMIND_BASE = getEnv("NEXT_PUBLIC_SPIRALMIND_URL", "SPIRALMIND_URL", "http://localhost:3801");
const MIGI_BASE       = getEnv("NEXT_PUBLIC_MIGI_URL",        "MIGI_URL",        "http://localhost:3802");

// Domyślne ścieżki API (dopasuj do backendów jeśli różnią się kontraktem)
const PATHS = {
  spiralmindAsk: "/api/ask",      // POST {prompt} -> {ok, text}
  migiProcess:   "/api/process",  // POST {prompt} -> {ok, text}
  health:        "/healthz",      // GET 200 OK (opcjonalny)
} as const;

interface Msg { role: "system" | "user" | "assistant"; text: string }

type EngineKey = "spiralmind" | "migi" | "simulation";

const ENGINES: Record<EngineKey, {
  name: string;
  endpoint: string | null;
  description: string;
  sources: string[];
}> = {
  spiralmind: {
    name: "SpiralMind‑Nexus (GOK:AI)",
    endpoint: `${SPIRALMIND_BASE}${PATHS.spiralmindAsk}`,
    description: "Kwantowy silnik świadomości z algorytmem 9π + F(n)",
    sources: ["GOK:AI Core", "Quantum Pipeline", "X Integration", "Psyche Module"],
  },
  migi: {
    name: "Apex Infinity MIGI Core",
    endpoint: `${MIGI_BASE}${PATHS.migiProcess}`,
    description: "Globalny rdzeń inteligencji MIGI z perspektywą nieskończoności",
    sources: ["MIGI Core", "Infinity Engine", "Global Intelligence", "Apex Systems"],
  },
  simulation: {
    name: "Symulacja (Demo)",
    endpoint: null,
    description: "Symulowany silnik dla celów demonstracyjnych",
    sources: ["Demo Core", "Symulacja AI", "Test Pipeline", "Mock Data"],
  },
};

export default function App() {
  // Chat
  const [messages, setMessages] = useState<Msg[]>([
    { role: "system", text: "Witaj w MTA Quest Webside X — okno treści GOK:AI (Mózg Boga)." },
  ]);
  const [input, setInput] = useState("");
  const listRef = useRef<HTMLDivElement | null>(null);

  // Reaktor
  const [engine, setEngine] = useState<EngineKey>("simulation");
  const [engineStatus, setEngineStatus] = useState<string>("Gotowy");
  const [stream, setStream] = useState<string[]>([]);

  // Autoscroll czatu
  useEffect(() => {
    listRef.current?.scrollTo({ top: listRef.current.scrollHeight, behavior: "smooth" });
  }, [messages.length]);

  // Strumień "telemetrii" dla klimatu UI
  useEffect(() => {
    const tick = setInterval(() => {
      const cfg = ENGINES[engine];
      const src = cfg.sources[Math.floor(Math.random() * cfg.sources.length)];
      const t = new Date().toLocaleTimeString();
      const size = (Math.random() * 10).toFixed(3);
      setStream((s) => {
        const next = [...s, `[${t}] ${cfg.name}: ${src} - ${size} TB`];
        return next.length > 20 ? next.slice(-20) : next;
      });
    }, 1500);
    return () => clearInterval(tick);
  }, [engine]);

  // Sprawdzanie statusu wybranego silnika
  useEffect(() => {
    const cfg = ENGINES[engine];
    if (!cfg.endpoint) {
      setEngineStatus("Symulacja aktywna");
      return;
    }
    setEngineStatus("Sprawdzanie połączenia...");
    const healthURL = cfg.endpoint
      .replace(PATHS.spiralmindAsk, PATHS.health)
      .replace(PATHS.migiProcess, PATHS.health);
    checkEngine(healthURL)
      .then((ok) => setEngineStatus(ok ? "Połączony" : "Endpoint OK, health offline — spróbuj zapytania"))
      .catch(() => setEngineStatus("Offline — sprawdź CORS/port/URL"));
  }, [engine]);

  async function checkEngine(url: string) {
    try {
      const r = await fetch(url, { method: "GET" });
      return r.ok;
    } catch {
      return false;
    }
  }

  // Wysyłanie promptu
  async function send() {
    const text = input.trim();
    if (!text) return;
    setMessages((m) => [...m, { role: "user", text }]);
    setInput("");

    const cfg = ENGINES[engine];

    if (engine === "simulation" || !cfg.endpoint) {
      const reply = await simulateResponse(text);
      setMessages((m) => [...m, { role: "assistant", text: reply }]);
      return;
    }

    try {
      const resp = await fetch(cfg.endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: text }),
      });
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      const data = await resp.json();
      if (typeof data?.ok !== "boolean" || (data.ok && typeof data.text !== "string")) {
        throw new Error("Niepoprawny kontrakt API: oczekiwano { ok: boolean, text?: string }");
      }
      const finalText = data.ok ? data.text : (data.error || "Błąd silnika");
      const decorated = decorateEngineReply(cfg.name, finalText);
      setMessages((m) => [...m, { role: "assistant", text: decorated }]);
    } catch (e: any) {
      const fallback = `Błąd połączenia z ${cfg.name}: ${e?.message || "nieznany"}\nPrzełączam na tryb symulacji...`;
      setMessages((m) => [...m, { role: "assistant", text: fallback }]);
      const sim = await simulateResponse(text);
      setMessages((m) => [...m, { role: "assistant", text: sim }]);
    }
  }

  function onKey(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  }

  // MINIMALNA PULA TESTÓW RUNTIME (logi w konsoli)
  useEffect(() => {
    type T = { name: string; run: () => boolean | Promise<boolean> };
    const tests: T[] = [
      {
        name: "resolveEnvOrder: preferuje process.env",
        run: () => resolveEnvOrder("A", "B", { A: "X" }, { B: "Y" }, "Z") === "X",
      },
      {
        name: "resolveEnvOrder: potem window.__CONFIG__",
        run: () => resolveEnvOrder("A", "B", {}, { B: "Y" }, "Z") === "Y",
      },
      {
        name: "resolveEnvOrder: fallback gdy brak wartości",
        run: () => resolveEnvOrder("A", "B", {}, {}, "Z") === "Z",
      },
      {
        name: "Symulacja zwraca tekst",
        run: async () => typeof (await simulateResponse("test")) === "string",
      },
    ];

    (async () => {
      for (const t of tests) {
        try {
          const ok = await t.run();
          console.log(`[TEST] ${t.name}: ${ok ? "OK" : "FAIL"}`);
        } catch (err) {
          console.error(`[TEST] ${t.name}: EXCEPTION`, err);
        }
      }
    })();
  }, []);

  return (
    <div className="min-h-screen w-full bg-[#0b0b12] text-slate-200 relative overflow-hidden">
      <BackgroundAura />

      <header className="relative z-10 max-w-6xl mx-auto px-6 pt-10 pb-6 flex items-center gap-4">
        <LogoMark />
        <div>
          <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-violet-500">MTA QUEST</span>{" "}
            <span className="text-slate-100">WEBSIDE</span>{" "}
            <span className="text-violet-400">X</span>
          </h1>
          <p className="text-xs sm:text-sm text-slate-400">www.MTAQuestWebsideX.com • Hybrid AI Interface</p>
        </div>
        <div className="ml-auto hidden sm:block"><Badge>GAIA INFINITI</Badge></div>
      </header>

      <main className="relative z-10 max-w-6xl mx-auto px-6 pb-12 grid md:grid-cols-5 gap-6">
        {/* Panel lewy: Reaktor */}
        <section className="md:col-span-2 rounded-3xl bg-[#0f0f1c]/70 border border-white/10 backdrop-blur-xl p-5 space-y-4">
          <div className="text-center">
            <h2 className="text-xl font-bold">Mózg Boga</h2>
            <p className="text-sm text-slate-400">Ekosystem `pinkplayevo-app`</p>
          </div>
          <div className="flex flex-col items-center">
            <LogoMark size={96} />
            <p className="mt-3 text-xs text-slate-300">Mózg Boga aktywny — wszystkie systemy online.</p>
          </div>

          <h3 className="text-sm font-semibold">Reaktor Paliwowy</h3>

          <label className="block text-xs text-slate-300">Wybierz Silnik AI:</label>
          <select
            className="w-full p-2 bg-slate-900/70 border border-white/10 rounded-xl focus:outline-none focus:ring-2 focus:ring-violet-500/30"
            value={engine}
            onChange={(e) => setEngine(e.target.value as EngineKey)}
          >
            <option value="spiralmind">SpiralMind‑Nexus (GOK:AI)</option>
            <option value="migi">Apex Infinity MIGI Core</option>
            <option value="simulation">Symulacja (Demo)</option>
          </select>

          <div className="text-xs bg-slate-900/50 border border-white/10 rounded-lg p-2">
            <p><span className="text-violet-300">Aktywny silnik:</span> {ENGINES[engine].name}</p>
            <p><span className="text-cyan-300">Status:</span> {engineStatus}</p>
          </div>

          <div className="h-64 overflow-y-auto border border-white/10 rounded-xl p-3 bg-[#0b0b12] font-mono text-xs">
            {stream.map((line, i) => (
              <p key={i} className="text-emerald-300">{line}</p>
            ))}
          </div>
        </section>

        {/* Panel prawy: Chat */}
        <section className="md:col-span-3 rounded-3xl bg-[#0f0f1c]/70 border border-white/10 backdrop-blur-xl p-5 flex flex-col">
          <h2 className="text-center text-xl sm:text-2xl font-bold mb-3">
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-fuchsia-400 to-cyan-400">Reaktor Termiczny — Interfejs</span>
          </h2>

          <div className="mb-3">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={onKey}
              placeholder="Wpisz swoje zapytanie... (Enter wysyła)"
              className="w-full h-28 p-4 bg-slate-900/70 border border-white/10 rounded-xl resize-none focus:outline-none focus:ring-2 focus:ring-violet-500/30 text-sm"
            />
          </div>

          <div className="flex items-center gap-3 mb-4">
            <button onClick={send} className="flex-1 bg-violet-600 hover:bg-violet-700 text-white font-bold py-3 px-6 rounded-xl transition-all shadow-lg shadow-violet-900/40">Zasil reaktor</button>
            <button onClick={() => setInput(sampleTests[Math.floor(Math.random()*sampleTests.length)])} className="flex-1 bg-cyan-600 hover:bg-cyan-700 text-white font-bold py-3 px-6 rounded-xl transition-all shadow-lg shadow-cyan-900/40">Test Silników</button>
          </div>

          <div ref={listRef} className="flex-1 overflow-y-auto space-y-3 border border-white/10 rounded-xl p-3 bg-[#0b0b12]">
            {messages.map((m, i) => (
              <ChatBubble key={i} role={m.role} text={m.text} />
            ))}
          </div>
        </section>
      </main>

      <footer className="relative z-10 max-w-6xl mx-auto px-6 pb-8">
        <div className="flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-500">
          <div>© {new Date().getFullYear()} MTAQuestWebsideX.com — All rights reserved.</div>
          <div className="flex items-center gap-2"><span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse" />Interfejs hybrydowy GOK:AI online</div>
        </div>
      </footer>
    </div>
  );
}

const sampleTests = [
  "Jaka jest przyszłość sztucznej inteligencji?",
  "Opisz koncepcję świadomości kwantowej",
  "Co to jest algorytm 9π + F(n)?",
];

function decorateEngineReply(name: string, text: string) {
  const ps = Math.floor(Math.random() * 40 + 60);
  const qp = (9 * Math.PI + fibonacci(9)).toFixed(3);
  return `\n${name} — odpowiedź:\n${text}\n\n🧠 Quantum consciousness pipeline aktywny\n🔄 Algorithm: 9π + F(n) = ${qp}\n📊 Success rate: ${ps}%`;
}

function simulateResponse(q: string) {
  return new Promise<string>((resolve) => {
    setTimeout(() => {
      const patterns = (Math.floor(Math.random() * 9000000 + 1000000)).toLocaleString();
      const neurons = (Math.floor(Math.random() * 50000 + 10000)).toLocaleString();
      const err = (Math.random() * 0.1).toFixed(3);
      resolve(
        `Symulacja Mózgu Boga:\nZapytanie: "${q}"\n— Wykryto ${patterns} powiązanych wzorców\n— ${neurons} neuronów kwantowych aktywnych\n— Przewidywanie błędu: ${err}%\n\nAby uzyskać prawdziwe odpowiedzi, wybierz SpiralMind‑Nexus i uruchom backend.`
      );
    }, 1200);
  });
}

function fibonacci(n: number): number {
  if (n <= 1) return n;
  let a = 0, b = 1;
  for (let i = 2; i <= n; i++) [a, b] = [b, a + b];
  return b;
}

function Badge({ children }: { children: React.ReactNode }) {
  return (
    <div className="px-3 py-1.5 rounded-full text-[10px] font-semibold tracking-wide bg-gradient-to-r from-cyan-400/20 to-violet-500/20 border border-white/10 text-slate-200">{children}</div>
  );
}

function ChatBubble({ role, text }: { role: Msg["role"]; text: string }) {
  const isUser = role === "user";
  const isSystem = role === "system";
  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div className={`max-w-[90%] sm:max-w-[75%] rounded-2xl px-4 py-3 text-sm whitespace-pre-wrap border ${
          isSystem
            ? "bg-white/[0.03] border-white/10"
            : isUser
            ? "bg-gradient-to-r from-cyan-500/15 to-violet-500/15 border-white/10"
            : "bg-white/[0.04] border-white/10"}`}>
        {!isUser && !isSystem && (<div className="mb-1 text-[10px] uppercase tracking-wider text-fuchsia-300">GOK:AI</div>)}
        {text}
      </div>
    </div>
  );
}

function BackgroundAura() {
  return (
    <div className="pointer-events-none absolute inset-0">
      <div className="absolute -top-40 -left-32 h-[420px] w-[420px] rounded-full blur-3xl opacity-30" style={{
        background: "radial-gradient(closest-side, #00e5ff, rgba(0,229,255,0))",
      }} />
      <div className="absolute -bottom-40 -right-32 h-[520px] w-[520px] rounded-full blur-3xl opacity-30" style={{
        background: "radial-gradient(closest-side, #7c3aed, rgba(124,58,237,0))",
      }} />
      <div className="absolute inset-0 mix-blend-screen opacity-[0.07]" style={{
        backgroundImage: "repeating-radial-gradient(circle at 50% 50%, rgba(255,255,255,.12) 0 1px, transparent 1px 8px)",
      }} />
    </div>
  );
}

function LogoMark({ size = 56 }: { size?: number }) {
  const s = size;
  return (
    <div
      className="relative"
      style={{ width: s, height: s }}
      aria-label="MTA Quest Webside X Logo"
      title="MTA Quest Webside X"
    >
      {/* Glow */}
      <div className="absolute inset-0 blur-xl opacity-80" style={{
        background: "conic-gradient(from 180deg at 50% 50%, #06b6d4, #7c3aed, #06b6d4)",
        filter: "blur(16px)",
        borderRadius: "9999px",
      }} />
      {/* Symbol */}
      <svg viewBox="0 0 100 100" className="relative z-10">
        <defs>
          <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stopColor="#22d3ee" />
            <stop offset="100%" stopColor="#8b5cf6" />
          </linearGradient>
        </defs>
        <circle cx="50" cy="50" r="44" stroke="url(#g)" strokeWidth="4" fill="none" />
        <ellipse cx="50" cy="50" rx="46" ry="18" stroke="url(#g)" strokeWidth="3" fill="none" />
        <ellipse cx="50" cy="50" rx="30" ry="30" stroke="url(#g)" strokeWidth="2" fill="none" />
        {/* Infinity */}
        <path d="M30 50c6-12 18-12 24 0 6 12 18 12 24 0" fill="none" stroke="url(#g)" strokeWidth="6" strokeLinecap="round" />
      </svg>
    </div>
  );
}
