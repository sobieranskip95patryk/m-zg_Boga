import Fastify from "fastify";
import cors from "@fastify/cors";
import fetch from "node-fetch";

const app = Fastify({ logger: true });
app.register(cors, { origin: true });

const {
  GOKAI_BASE = "http://localhost:3000",  // Używamy istniejący serwer GOK:AI
  SPIRALMIND_BASE = "http://localhost:3801",
  MIGI_BASE = "http://localhost:3802",
  GOKAI_TOKEN = "",
  SPIRALMIND_TOKEN = "",
  MIGI_TOKEN = "",
} = process.env;

app.get("/api/health", async (_req, reply) => {
  const services = {};
  
  // Sprawdź dostępność każdego serwisu
  try {
    const gokaiCheck = await fetch(`${GOKAI_BASE}/api/ask`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: 'ping' }),
      timeout: 3000
    });
    services.gokai = gokaiCheck.ok;
  } catch (e) {
    services.gokai = false;
  }
  
  try {
    const spiralmindCheck = await fetch(`${SPIRALMIND_BASE}/api/ask`, {
      method: 'POST', 
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: 'ping' }),
      timeout: 3000
    });
    services.spiralmind = spiralmindCheck.ok;
  } catch (e) {
    services.spiralmind = false;
  }
  
  try {
    const migiCheck = await fetch(`${MIGI_BASE}/api/process`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' }, 
      body: JSON.stringify({ prompt: 'ping' }),
      timeout: 3000
    });
    services.migi = migiCheck.ok;
  } catch (e) {
    services.migi = false;
  }
  
  reply.send({ 
    ok: true, 
    services: Object.keys(services),
    status: services,
    timestamp: new Date().toISOString()
  });
});

app.post("/api/chat/ask", async (req, reply) => {
  const { engine, prompt } = req.body || {};
  if (!prompt || !engine) return reply.code(400).send({ ok: false, error: "engine + prompt required" });

  try {
    if (engine === "gokai") {
      const r = await proxyJson(`${GOKAI_BASE}/api/ask`, { prompt }, tokenHeader(GOKAI_TOKEN));
      return reply.send(standardize("gokai", r));
    }
    if (engine === "spiralmind") {
      const r = await proxyJson(`${SPIRALMIND_BASE}/api/ask`, { prompt }, tokenHeader(SPIRALMIND_TOKEN));
      return reply.send(standardize("spiralmind", r));
    }
    if (engine === "migi") {
      const r = await proxyJson(`${MIGI_BASE}/api/process`, { prompt }, tokenHeader(MIGI_TOKEN));
      return reply.send(standardize("migi", r));
    }
    return reply.code(400).send({ ok: false, error: "unknown engine" });
  } catch (e) {
    console.error(`Engine ${engine} error:`, e.message);
    return reply.code(502).send({ ok: false, error: String(e.message || e) });
  }
});

// Credits/Tokenization endpoints
app.get("/api/credits/balance", async (req, reply) => {
  // TODO: Integracja z DB użytkowników
  reply.send({ 
    ok: true, 
    balance: 1000, 
    currency: "MTA_CREDITS",
    user: "demo_user"
  });
});

app.post("/api/credits/topup", async (req, reply) => {
  const { amount } = req.body || {};
  if (!amount || amount <= 0) return reply.code(400).send({ ok: false, error: "invalid amount" });
  
  // TODO: Integracja z payment gateway
  reply.send({
    ok: true,
    transaction_id: `tx_${Date.now()}`,
    amount,
    new_balance: 1000 + amount
  });
});

function tokenHeader(token) {
  return token ? { Authorization: `Bearer ${token}` } : {};
}

async function proxyJson(url, body, headers = {}) {
  const r = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json", ...headers },
    body: JSON.stringify(body),
    timeout: 15000
  });
  if (!r.ok) throw new Error(`Upstream ${url} HTTP ${r.status}`);
  return r.json();
}

function standardize(engine, upstream) {
  if (upstream && typeof upstream === "object" && "ok" in upstream) {
    if (upstream.ok) return { 
      ok: true, 
      engine, 
      text: upstream.text ?? "", 
      meta: {
        provider: upstream.provider,
        model: upstream.model,
        keyUsed: upstream.keyUsed,
        timestamp: new Date().toISOString()
      }
    };
    return { ok: false, engine, error: upstream.error ?? "upstream error" };
  }
  // fallback, jeśli upstream nie ma {ok}
  const text = typeof upstream === "string" ? upstream : JSON.stringify(upstream);
  return { 
    ok: true, 
    engine, 
    text, 
    meta: { 
      fallback: true,
      timestamp: new Date().toISOString()
    }
  };
}

const PORT = process.env.PORT || 8080;
app.listen({ port: Number(PORT), host: "0.0.0.0" }).then(() => {
  console.log(`🚀 MTA Gateway running on port ${PORT}`);
  console.log(`📡 GOKAI_BASE: ${GOKAI_BASE}`);
  console.log(`🌀 SPIRALMIND_BASE: ${SPIRALMIND_BASE}`);  
  console.log(`🔵 MIGI_BASE: ${MIGI_BASE}`);
});