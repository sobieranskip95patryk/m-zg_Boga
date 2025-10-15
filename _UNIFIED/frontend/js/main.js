// Main Application Controller for Unified Brain of God System
class BrainOfGodApp {
    constructor() {
        this.config = window.BRAIN_CONFIG;
        this.engineManager = new window.EngineManager(this.config);
        this.elements = {};
        this.init();
    }
    
    // Inicjalizacja aplikacji
    init() {
        this.bindElements();
        this.setupEventListeners();
        this.initializeSystem();
    }
    
    // Przypisanie elementów DOM
    bindElements() {
        this.elements = {
            dataStream: document.getElementById('data-stream'),
            statusMessage: document.getElementById('status-message'),
            promptInput: document.getElementById('prompt-input'),
            sendBtn: document.getElementById('send-btn'),
            outputDisplay: document.getElementById('output-display'),
            engineSelector: document.getElementById('engine-selector'),
            currentEngineSpan: document.getElementById('current-engine'),
            engineConnectionSpan: document.getElementById('engine-connection'),
            exploreBtn: document.getElementById('explore-btn')
        };
    }
    
    // Konfiguracja event listenerów
    setupEventListeners() {
        // Przełączanie silników
        this.elements.engineSelector.addEventListener('change', (e) => {
            this.handleEngineSwitch(e.target.value);
        });
        
        // Przycisk wyślij
        this.elements.sendBtn.addEventListener('click', () => {
            this.handleSendQuery();
        });
        
        // Przycisk testowania silników
        this.elements.exploreBtn.addEventListener('click', () => {
            this.handleTestEngines();
        });
        
        // Enter w textarea
        this.elements.promptInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.handleSendQuery();
            }
        });
    }
    
    // Inicjalizacja systemu
    async initializeSystem() {
        this.elements.statusMessage.textContent = 'Unified Brain of God aktywny - wszystkie systemy online.';
        this.engineManager.startDataStream(this.elements.dataStream);
        
        // Sprawdź dostępność silników przy starcie
        await this.checkEngineStatus();
    }
    
    // Sprawdzenie statusu silników
    async checkEngineStatus() {
        const spiralmindEngine = this.config.engines.spiralmind;
        const connected = await this.engineManager.checkEngineConnection(spiralmindEngine.endpoint);
        
        this.elements.engineConnectionSpan.textContent = connected ? 'Połączony' : 'Offline - Symulacja';
        this.elements.engineConnectionSpan.className = connected ? 'text-green-400' : 'text-yellow-400';
    }
    
    // Obsługa przełączania silników
    async handleEngineSwitch(engineKey) {
        this.engineManager.setCurrentEngine(engineKey);
        const engineConfig = this.engineManager.getEngineConfig(engineKey);
        
        this.elements.currentEngineSpan.textContent = engineConfig.name;
        
        // Aktualizacja statusu połączenia
        if (engineKey === 'spiralmind') {
            this.elements.engineConnectionSpan.textContent = 'Próba połączenia...';
            const connected = await this.engineManager.checkEngineConnection(engineConfig.endpoint);
            this.elements.engineConnectionSpan.textContent = connected ? 'Połączony' : 'Offline - Symulacja';
            this.elements.engineConnectionSpan.className = connected ? 'text-green-400' : 'text-yellow-400';
        } else if (engineKey === 'migi') {
            this.elements.engineConnectionSpan.textContent = 'W przygotowaniu';
            this.elements.engineConnectionSpan.className = 'text-blue-400';
        } else {
            this.elements.engineConnectionSpan.textContent = 'Symulacja aktywna';
            this.elements.engineConnectionSpan.className = 'text-purple-400';
        }
        
        this.elements.statusMessage.textContent = `Przełączono na: ${engineConfig.description}`;
        this.engineManager.startDataStream(this.elements.dataStream);
    }
    
    // Obsługa wysyłania zapytania
    async handleSendQuery() {
        const query = this.elements.promptInput.value.trim();
        if (!query) {
            alert('Wpisz zapytanie, aby uruchomić reaktor.');
            return;
        }
        
        await this.processQuery(query);
    }
    
    // Obsługa testowania silników
    async handleTestEngines() {
        const testQueries = this.config.testQueries;
        const randomQuery = testQueries[Math.floor(Math.random() * testQueries.length)];
        
        this.elements.promptInput.value = randomQuery;
        
        const engineConfig = this.engineManager.getEngineConfig(this.engineManager.getCurrentEngine());
        this.elements.outputDisplay.innerHTML = `<p class="text-blue-400">🧪 Testowanie unified system: ${engineConfig.name}...</p>`;
        
        await this.processQuery(randomQuery);
    }
    
    // Główna funkcja przetwarzania zapytań
    async processQuery(query) {
        const engineConfig = this.engineManager.getEngineConfig(this.engineManager.getCurrentEngine());
        
        // UI feedback
        this.elements.outputDisplay.innerHTML = `<p class="text-gray-400">Analizowanie przez ${engineConfig.name}... <span class="loader ml-2"></span></p>`;
        this.elements.sendBtn.disabled = true;
        this.elements.promptInput.disabled = true;
        
        try {
            const response = await this.engineManager.processQuery(query);
            this.elements.outputDisplay.innerHTML = response;
        } catch (error) {
            this.elements.outputDisplay.innerHTML = `
                <div class="border-l-4 border-red-500 pl-4">
                    <p class="text-red-400">Błąd systemu: ${error.message}</p>
                    <p class="text-yellow-400 mt-2">Sprawdź konfigurację unified ecosystem...</p>
                </div>
            `;
        } finally {
            this.elements.sendBtn.disabled = false;
            this.elements.promptInput.disabled = false;
        }
    }
    
    // Cleanup przy zamknięciu
    destroy() {
        this.engineManager.stopDataStream();
    }
}

// Inicjalizacja aplikacji po załadowaniu DOM
document.addEventListener('DOMContentLoaded', () => {
    window.brainApp = new BrainOfGodApp();
});

// Cleanup przy opuszczeniu strony
window.addEventListener('beforeunload', () => {
    if (window.brainApp) {
        window.brainApp.destroy();
    }
});