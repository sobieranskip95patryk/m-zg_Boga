import Fastify from "fastify";
import cors from "@fastify/cors";
import { spawn } from "child_process";
import path from "path";

const app = Fastify({ logger: true });
app.register(cors, { origin: true });

// Ścieżka do Python pipeline SpiralMind-Nexus
const SPIRALMIND_PATH = process.env.SPIRALMIND_PATH || "../_UNIFIED/engines/spiralmind-nexus";

app.get("/healthz", (_, reply) => reply.send({ ok: true, service: "spiralmind-adapter" }));

app.post("/api/ask", async (req, reply) => {
  const { prompt } = req.body || {};
  if (!prompt) return reply.code(400).send({ ok: false, error: "No prompt provided" });
  
  try {
    // Wywołanie Python pipeline
    const result = await runSpiralMindPipeline(prompt);
    return reply.send({ 
      ok: true, 
      text: result,
      meta: {
        engine: "spiralmind-nexus",
        timestamp: new Date().toISOString()
      }
    });
  } catch (error) {
    console.error("SpiralMind pipeline error:", error);
    return reply.code(500).send({ 
      ok: false, 
      error: error.message || "Pipeline execution failed"
    });
  }
});

async function runSpiralMindPipeline(prompt) {
  return new Promise((resolve, reject) => {
    // Wywołanie Python script z _UNIFIED/engines/spiralmind-nexus/
    const pythonProcess = spawn('python', [
      path.join(SPIRALMIND_PATH, 'main.py'),
      '--prompt', prompt
    ], {
      cwd: SPIRALMIND_PATH
    });
    
    let output = '';
    let errorOutput = '';
    
    pythonProcess.stdout.on('data', (data) => {
      output += data.toString();
    });
    
    pythonProcess.stderr.on('data', (data) => {
      errorOutput += data.toString();
    });
    
    pythonProcess.on('close', (code) => {
      if (code === 0) {
        resolve(output.trim() || `SpiralMind processed: "${prompt}"`);
      } else {
        reject(new Error(`Python process exited with code ${code}: ${errorOutput}`));
      }
    });
    
    pythonProcess.on('error', (error) => {
      reject(new Error(`Failed to start Python process: ${error.message}`));
    });
    
    // Timeout po 30 sekundach
    setTimeout(() => {
      pythonProcess.kill();
      reject(new Error('Pipeline timeout after 30 seconds'));
    }, 30000);
  });
}

const PORT = process.env.PORT || 3801;
app.listen({ port: Number(PORT), host: "0.0.0.0" }).then(() => {
  console.log(`🌀 SpiralMind adapter on port ${PORT}`);
  console.log(`🐍 Python path: ${SPIRALMIND_PATH}`);
});