// Konfiguracja silników AI - Unified Brain of God Configuration
const CONFIG = {
    project: {
        name: "Mózg Boga - Unified AI Ecosystem",
        version: "2.0.0",
        description: "Zintegrowany ekosystem silników AI"
    },
    
    api: {
        baseUrl: window.location.origin,
        timeout: 30000
    },
    
    engines: {
        'spiralmind': {
            name: 'SpiralMind-Nexus (GOK:AI)',
            endpoint: 'http://localhost:3000/api/ask',
            description: 'Kwantowy silnik świadomości z algorytmem 9π + F(n)',
            sources: ['GOK:AI Core', 'Quantum Pipeline', 'X Integration', 'Psyche Module'],
            status: 'active'
        },
        'migi': {
            name: 'Apex Infinity MIGI Core',
            endpoint: 'http://localhost:3001/api/process',
            description: 'Globalny rdzeń inteligencji MIGI z perspektywą nieskończoności',
            sources: ['MIGI Core', 'Infinity Engine', 'Global Intelligence', 'Apex Systems'],
            status: 'development'
        },
        'simulation': {
            name: 'Symulacja (Demo)',
            endpoint: null,
            description: 'Symulowany silnik dla celów demonstracyjnych',
            sources: ['Demo Core', 'Symulacja AI', 'Test Pipeline', 'Mock Data'],
            status: 'always_available'
        }
    },
    
    ui: {
        dataStreamInterval: 1500,
        maxLogLines: 20,
        animationDuration: 300
    },
    
    testQueries: [
        "Jaka jest przyszłość sztucznej inteligencji?",
        "Opisz koncepcję świadomości kwantowej",
        "Co to jest algorytm 9π + F(n)?",
        "Jak działa unified ecosystem AI?",
        "Wyjaśnij architekturę Mózgu Boga"
    ]
};

// Export konfiguracji
window.BRAIN_CONFIG = CONFIG;