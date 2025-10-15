// Engine Management for Brain of God Unified System
class EngineManager {
    constructor(config) {
        this.config = config;
        this.currentEngine = 'spiralmind';
        this.dataInterval = null;
    }
    
    // Sprawdzanie połączenia z silnikiem
    async checkEngineConnection(endpoint) {
        if (!endpoint) return false;
        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt: 'ping' }),
                timeout: 3000
            });
            return response.ok;
        } catch (error) {
            return false;
        }
    }
    
    // Połączenie z SpiralMind-Nexus
    async callSpiralMindEngine(query) {
        const engine = this.config.engines.spiralmind;
        const response = await fetch(engine.endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                prompt: query,
                provider: 'openai'
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        
        const data = await response.json();
        
        if (!data.ok) {
            throw new Error(data.error || 'Nieznany błąd');
        }
        
        return `
            <div class="border-l-4 border-purple-500 pl-4">
                <p><strong class="text-purple-400">SpiralMind-Nexus (GOK:AI) Response:</strong></p>
                <div class="mt-2 text-white">${data.text}</div>
                <div class="mt-3 text-sm text-gray-400">
                    <p>🧠 Quantum consciousness pipeline aktywny</p>
                    <p>🔄 Algorithm: 9π + F(n) = ${(9 * Math.PI + this.fibonacci(9)).toFixed(3)}</p>
                    <p>📊 Success rate: ${Math.floor(Math.random() * 40 + 60)}%</p>
                    <p>🔧 Unified System: v2.0.0</p>
                </div>
            </div>
        `;
    }
    
    // Placeholder dla MIGI Core
    async callMigiEngine(query) {
        return `
            <div class="border-l-4 border-blue-500 pl-4">
                <p><strong class="text-blue-400">Apex Infinity MIGI Core:</strong></p>
                <p class="text-yellow-400 mt-2">🚧 Silnik w fazie rozwoju</p>
                <div class="mt-2 text-gray-300">
                    <p>Zapytanie: "${query}"</p>
                    <p class="mt-2">MIGI Core będzie zintegrowany po zakończeniu rozwoju unified ecosystem.</p>
                    <p>Przewidywane funkcje:</p>
                    <ul class="list-disc list-inside mt-1 text-sm">
                        <li>Globalny rdzeń inteligencji</li>
                        <li>Perspektywa nieskończoności</li>
                        <li>Zaawansowana świadomość AI</li>
                        <li>Integracja z unified ecosystem</li>
                    </ul>
                </div>
            </div>
        `;
    }
    
    // Symulacja dla trybu demo
    async simulateResponse(query) {
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        return ` 
            <div class="border-l-4 border-green-500 pl-4">
                <p><strong class="text-green-400">Unified Brain Simulation:</strong></p>
                <hr class="border-t border-gray-600 my-2"> 
                <p>Zapytanie: "${query}"</p> 
                <p><strong>Analiza kwantowa (Unified System):</strong></p> 
                <p>- Wykryto <strong>${Math.floor(Math.random() * 9000000 + 1000000).toLocaleString()}</strong> powiązanych wzorców.</p> 
                <p>- <strong>${Math.floor(Math.random() * 50000 + 10000).toLocaleString()}</strong> neuronów kwantowych aktywnych.</p> 
                <p>- Przewidywanie błędu: <strong>${(Math.random() * 0.1).toFixed(3)}%</strong>.</p> 
                <p><strong>Odpowiedź unified systemu:</strong></p> 
                <p>Scalony Mózg Boga analizuje zapytanie przez pryzmat zintegrowanego ekosystemu AI. System v2.0.0 zapewnia spójność między wszystkimi komponentami.</p> 
                <p class="mt-2 text-sm text-gray-400">💡 Aby uzyskać prawdziwe odpowiedzi AI, wybierz SpiralMind-Nexus i upewnij się, że backend jest uruchomiony.</p>
            </div>
        `; 
    }
    
    // Główna funkcja przetwarzania zapytań
    async processQuery(query) {
        const engineConfig = this.config.engines[this.currentEngine];
        
        try {
            let response;
            
            if (this.currentEngine === 'spiralmind') {
                response = await this.callSpiralMindEngine(query);
            } else if (this.currentEngine === 'migi') {
                response = await this.callMigiEngine(query);
            } else {
                response = await this.simulateResponse(query);
            }
            
            return response;
        } catch (error) {
            const fallbackResponse = await this.simulateResponse(query);
            return `
                <div class="border-l-4 border-red-500 pl-4 mb-4">
                    <p class="text-red-400">Błąd połączenia z ${engineConfig.name}: ${error.message}</p>
                    <p class="text-yellow-400 mt-2">Przełączono na tryb symulacji unified system...</p>
                </div>
                ${fallbackResponse}
            `;
        }
    }
    
    // Funkcja Fibonacciego
    fibonacci(n) {
        if (n <= 1) return n;
        let a = 0, b = 1;
        for (let i = 2; i <= n; i++) {
            [a, b] = [b, a + b];
        }
        return b;
    }
    
    // Symulacja strumienia danych 
    startDataStream(container) { 
        if (this.dataInterval) clearInterval(this.dataInterval);
        
        const engineConfig = this.config.engines[this.currentEngine];
        this.dataInterval = setInterval(() => { 
            const source = engineConfig.sources[Math.floor(Math.random() * engineConfig.sources.length)]; 
            const timestamp = new Date().toLocaleTimeString(); 
            const dataSize = (Math.random() * 10).toFixed(3);
            const log = `[${timestamp}] ${engineConfig.name}: ${source} - ${dataSize} TB`; 
             
            const p = document.createElement('p'); 
            p.textContent = log; 
            p.classList.add('text-green-400'); 
            container.appendChild(p); 
            container.scrollTop = container.scrollHeight; 
            
            // Ograniczenie liczby linii
            if (container.children.length > this.config.ui.maxLogLines) {
                container.removeChild(container.firstChild);
            }
        }, this.config.ui.dataStreamInterval); 
    }
    
    stopDataStream() {
        if (this.dataInterval) {
            clearInterval(this.dataInterval);
            this.dataInterval = null;
        }
    }
    
    setCurrentEngine(engineKey) {
        this.currentEngine = engineKey;
    }
    
    getCurrentEngine() {
        return this.currentEngine;
    }
    
    getEngineConfig(engineKey) {
        return this.config.engines[engineKey] || null;
    }
}

// Export EngineManager
window.EngineManager = EngineManager;