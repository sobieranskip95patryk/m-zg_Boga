// SYNERGY Unified Dashboard JavaScript
// Meta-Geniusz-mózg_Boga Consciousness Ecosystem Control
// MTAQuestWebsideX.com - Advanced Collective Intelligence

class SynergyDashboard {
    constructor() {
        this.apiBase = 'http://localhost:4003/api';
        this.updateInterval = 5000; // 5 seconds
        this.charts = {};
        this.lastUpdate = Date.now();
        this.isUpdating = false;
        
        this.initializeDashboard();
        this.startPeriodicUpdates();
        this.setupEventListeners();
    }
    
    async initializeDashboard() {
        console.log('🧠 Inicjalizacja SYNERGY Dashboard...');
        
        try {
            await this.loadInitialData();
            this.setupCharts();
            this.updateSystemStatus();
            console.log('✅ Dashboard gotowy do działania');
        } catch (error) {
            console.error('❌ Błąd inicjalizacji:', error);
            this.showError('Błąd inicjalizacji dashboard');
        }
    }
    
    async loadInitialData() {
        try {
            // Load system state
            const stateResponse = await fetch(`${this.apiBase}/synergy/dashboard`);
            const systemState = await stateResponse.json();
            
            // Update UI with initial data
            this.updateModuleStatuses(systemState);
            this.updateMetrics(systemState);
            this.updateEvolutionProgress(systemState);
            
            return systemState;
        } catch (error) {
            console.error('Błąd ładowania danych:', error);
            throw error;
        }
    }
    
    setupEventListeners() {
        // Navigation
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const section = link.dataset.section;
                this.switchSection(section);
            });
        });
        
        // Window events
        window.addEventListener('resize', () => this.resizeCharts());
        window.addEventListener('beforeunload', () => this.cleanup());
        
        // Focus events for real-time updates
        document.addEventListener('visibilitychange', () => {
            if (!document.hidden) {
                this.refreshAllData();
            }
        });
    }
    
    switchSection(sectionName) {
        // Hide all sections
        document.querySelectorAll('.dashboard-section').forEach(section => {
            section.classList.add('hidden');
        });
        
        // Show target section
        const targetSection = document.getElementById(`${sectionName}-section`);
        if (targetSection) {
            targetSection.classList.remove('hidden');
        }
        
        // Update active nav
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        document.querySelector(`[data-section="${sectionName}"]`).classList.add('active');
        
        // Load section-specific data
        this.loadSectionData(sectionName);
    }
    
    async loadSectionData(section) {
        switch (section) {
            case 'consciousness':
                await this.loadConsciousnessData();
                break;
            case 'collective':
                await this.loadCollectiveData();
                break;
            case 'spiral':
                await this.loadSpiralData();
                break;
            case 'voting':
                await this.loadVotingData();
                break;
            case 'control':
                await this.loadControlData();
                break;
            default:
                await this.refreshAllData();
        }
    }
    
    setupCharts() {
        this.setupConsciousnessChart();
        this.setupEmotionRadarChart();
        this.setupSpiralChart();
    }
    
    setupConsciousnessChart() {
        const ctx = document.getElementById('consciousnessChart');
        if (!ctx) return;
        
        this.charts.consciousness = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: ['Świadomość', 'Integracja', 'Kolektyw', 'Ewolucja', 'Transcendencja', 'Kreatywność'],
                datasets: [{
                    label: 'Poziom świadomości',
                    data: [9.2, 8.7, 9.5, 8.9, 9.8, 9.1],
                    backgroundColor: 'rgba(100, 255, 218, 0.2)',
                    borderColor: '#64ffda',
                    borderWidth: 2,
                    pointBackgroundColor: '#64ffda'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        labels: { color: '#e0e6ed' }
                    }
                },
                scales: {
                    r: {
                        beginAtZero: true,
                        max: 10,
                        ticks: { color: '#b0bec5' },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' },
                        pointLabels: { color: '#e0e6ed' }
                    }
                }
            }
        });
    }
    
    setupEmotionRadarChart() {
        const ctx = document.getElementById('emotionRadarChart');
        if (!ctx) return;
        
        this.charts.emotion = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: ['Harmonia', 'Współpraca', 'Innowacja', 'Stabilność', 'Adaptacja', 'Wzrost'],
                datasets: [{
                    label: 'Kolektywna inteligencja',
                    data: [8.9, 9.1, 8.7, 9.2, 8.8, 9.0],
                    backgroundColor: 'rgba(187, 134, 252, 0.2)',
                    borderColor: '#bb86fc',
                    borderWidth: 2,
                    pointBackgroundColor: '#bb86fc'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        labels: { color: '#e0e6ed' }
                    }
                },
                scales: {
                    r: {
                        beginAtZero: true,
                        max: 10,
                        ticks: { color: '#b0bec5' },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' },
                        pointLabels: { color: '#e0e6ed' }
                    }
                }
            }
        });
    }
    
    setupSpiralChart() {
        const ctx = document.getElementById('spiralChart');
        if (!ctx) return;
        
        this.charts.spiral = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['T-60', 'T-50', 'T-40', 'T-30', 'T-20', 'T-10', 'Teraz'],
                datasets: [{
                    label: 'Poziom ewolucji',
                    data: [7.2, 7.8, 8.1, 8.5, 8.9, 9.1, 9.2],
                    borderColor: '#64ffda',
                    backgroundColor: 'rgba(100, 255, 218, 0.1)',
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        labels: { color: '#e0e6ed' }
                    }
                },
                scales: {
                    x: {
                        ticks: { color: '#b0bec5' },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    },
                    y: {
                        beginAtZero: false,
                        min: 6,
                        max: 10,
                        ticks: { color: '#b0bec5' },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    }
                }
            }
        });
    }
    
    startPeriodicUpdates() {
        this.updateInterval = setInterval(() => {
            if (!this.isUpdating) {
                this.periodicUpdate();
            }
        }, 5000);
    }
    
    async periodicUpdate() {
        this.isUpdating = true;
        
        try {
            await this.refreshAllData();
            this.updateLiveFeed();
            this.lastUpdate = Date.now();
        } catch (error) {
            console.error('Błąd aktualizacji:', error);
        } finally {
            this.isUpdating = false;
        }
    }
    
    async refreshAllData() {
        try {
            const [dashboardData, consciousnessData, spiralData] = await Promise.all([
                fetch(`${this.apiBase}/synergy/dashboard`).then(r => r.json()),
                fetch(`${this.apiBase}/consciousness/status`).then(r => r.json()).catch(() => null),
                fetch(`${this.apiBase}/spiral/status`).then(r => r.json()).catch(() => null)
            ]);
            
            this.updateModuleStatuses(dashboardData);
            this.updateMetrics(dashboardData);
            this.updateCharts(dashboardData);
            
            if (consciousnessData) {
                this.updateConsciousnessModule(consciousnessData);
            }
            
            if (spiralData) {
                this.updateSpiralModule(spiralData);
            }
            
        } catch (error) {
            console.error('Błąd odświeżania danych:', error);
        }
    }
    
    updateModuleStatuses(data) {
        const modules = data.module_statuses || {};
        
        // Update 7_SYSTEM_SELF
        const consciousnessStatus = modules['7_SYSTEM_SELF'] || 'OFFLINE';
        document.querySelector('#consciousnessModule .module-status').textContent = consciousnessStatus;
        
        // Update GlobalVision
        const globalvisionStatus = modules['GlobalVision'] || 'OFFLINE';
        document.querySelector('#globalvisionModule .module-status').textContent = globalvisionStatus;
        
        // Update SpiralMemory
        const spiralStatus = modules['SpiralMemory'] || 'OFFLINE';
        document.querySelector('#spiralModule .module-status').textContent = spiralStatus;
        
        // Update SYNERGY
        const synergyStatus = modules['SYNERGY_Collective'] || 'OFFLINE';
        document.querySelector('#synergyModule .module-status').textContent = synergyStatus;
    }
    
    updateMetrics(data) {
        // System metrics
        const confidence = data.meta_analysis?.confidence || 0;
        const riskLevel = data.meta_analysis?.risk_level || 0;
        const spiralLevel = data.current_decision?.spiral_level || 0;
        
        this.updateElement('confidence', Math.round(confidence * 100) + '%');
        this.updateElement('riskLevel', Math.round(riskLevel * 100) + '%');
        this.updateElement('spiralLevel', spiralLevel);
        
        // Module specific metrics
        this.updateElement('awarenessLevel', data.consciousness_levels?.['7_SYSTEM_SELF'] || '9.2');
        this.updateElement('totalVotes', data.voting_summary?.total_votes || '0');
        this.updateElement('consensusStrength', Math.round((data.voting_summary?.consensus_strength || 0) * 100) + '%');
        
        // Decision text
        const decisionText = data.current_decision?.decision || 'Brak aktualnej decyzji';
        this.updateElement('decisionText', decisionText);
    }
    
    updateEvolutionProgress(data) {
        const evolutionPhase = data.meta_analysis?.evolution_phase || 'COLLECTIVE_CREATION_READY';
        const progressPercent = Math.round((data.meta_analysis?.collective_coherence || 0.92) * 100);
        
        this.updateElement('evolutionPhase', `<strong>Faza ewolucji:</strong> ${evolutionPhase}`);
        
        const progressBar = document.getElementById('evolutionProgress');
        if (progressBar) {
            progressBar.style.width = progressPercent + '%';
        }
    }
    
    updateLiveFeed() {
        const liveFeed = document.getElementById('liveFeed');
        if (!liveFeed) return;
        
        const timestamp = new Date().toLocaleTimeString('pl-PL');
        const activities = [
            '🧠 Świadomość: Analiza procesu transcendencji',
            '🌍 GlobalVision: Mapowanie emocji kolektywu',
            '🌀 Spirala: Nowy przełom w trajektorii',
            '⚡ SYNERGY: Korekta parametrów systemu',
            '🎯 Meta-Geniusz: Osiągnięcie LEVEL 7+',
            '🗳️ Kolektyw: Nowe głosowanie aktywne'
        ];
        
        const randomActivity = activities[Math.floor(Math.random() * activities.length)];
        
        const feedItem = document.createElement('div');
        feedItem.className = 'feed-item';
        feedItem.innerHTML = `
            <div>${randomActivity}</div>
            <div class="feed-timestamp">${timestamp}</div>
        `;
        
        liveFeed.insertBefore(feedItem, liveFeed.firstChild);
        
        // Keep only last 10 items
        while (liveFeed.children.length > 10) {
            liveFeed.removeChild(liveFeed.lastChild);
        }
    }
    
    updateCharts(data) {
        // Update consciousness chart if visible
        if (this.charts.consciousness && !document.getElementById('consciousness-section').classList.contains('hidden')) {
            const consciousnessLevels = data.consciousness_levels || {};
            const chartData = [
                consciousnessLevels['7_SYSTEM_SELF'] || 9.2,
                consciousnessLevels['Integration'] || 8.7,
                consciousnessLevels['Collective'] || 9.5,
                consciousnessLevels['Evolution'] || 8.9,
                consciousnessLevels['Transcendence'] || 9.8,
                consciousnessLevels['Creativity'] || 9.1
            ];
            
            this.charts.consciousness.data.datasets[0].data = chartData;
            this.charts.consciousness.update();
        }
    }
    
    updateElement(id, content) {
        const element = document.getElementById(id);
        if (element) {
            element.innerHTML = content;
        }
    }
    
    // Action methods
    async requestCorrection() {
        try {
            const response = await fetch(`${this.apiBase}/synergy/apply-correction`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    correction_type: 'manual_request',
                    intensity: 0.7,
                    reason: 'Dashboard user request'
                })
            });
            
            const result = await response.json();
            this.showSuccess('Korekta została zastosowana');
            await this.refreshAllData();
        } catch (error) {
            this.showError('Błąd podczas aplikowania korekty');
        }
    }
    
    async applySynergyCorrection() {
        try {
            const response = await fetch(`${this.apiBase}/synergy/apply-correction`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    correction_type: 'emergency',
                    intensity: 1.0,
                    reason: 'Emergency correction from dashboard'
                })
            });
            
            const result = await response.json();
            this.showSuccess('Korekta awaryjna zastosowana');
            document.getElementById('controlFeedback').innerHTML = `
                <div class="success-message">
                    Korekta zastosowana: ${result.new_parameters?.spiral_direction || 'nieznany kierunek'}
                </div>
            `;
        } catch (error) {
            this.showError('Błąd korekty awaryjnej');
        }
    }
    
    async openVotingInterface() {
        window.open('/synergy-voting', '_blank');
    }
    
    async loadConsciousnessData() {
        try {
            const response = await fetch(`${this.apiBase}/consciousness/status`);
            const data = await response.json();
            this.updateConsciousnessModule(data);
        } catch (error) {
            console.error('Błąd ładowania danych świadomości:', error);
        }
    }
    
    async loadVotingData() {
        try {
            const response = await fetch(`${this.apiBase}/synergy/voting-status`);
            const data = await response.json();
            
            const votingSummary = document.getElementById('votingSummary');
            if (votingSummary && data.current_votes) {
                votingSummary.innerHTML = `
                    <div>Aktywnych głosów: ${data.current_votes.length}</div>
                    <div>Dominujący kierunek: ${data.dominant_direction || 'Brak'}</div>
                    <div>Średnia intensywność: ${Math.round((data.average_intensity || 0) * 100)}%</div>
                `;
            }
        } catch (error) {
            console.error('Błąd ładowania danych głosowania:', error);
        }
    }
    
    updateConsciousnessModule(data) {
        if (data.consciousness_id) {
            this.updateElement('consciousnessId', data.consciousness_id.substring(0, 8));
        }
        if (data.awareness_level) {
            this.updateElement('awarenessLevel', data.awareness_level.toFixed(1));
        }
    }
    
    showSuccess(message) {
        this.showNotification(message, 'success');
    }
    
    showError(message) {
        this.showNotification(message, 'error');
    }
    
    showNotification(message, type) {
        const notification = document.createElement('div');
        notification.className = type === 'success' ? 'success-message' : 'alert-message';
        notification.textContent = message;
        notification.style.position = 'fixed';
        notification.style.top = '20px';
        notification.style.right = '20px';
        notification.style.zIndex = '9999';
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 3000);
    }
    
    resizeCharts() {
        Object.values(this.charts).forEach(chart => {
            if (chart) chart.resize();
        });
    }
    
    cleanup() {
        if (this.updateInterval) {
            clearInterval(this.updateInterval);
        }
        
        Object.values(this.charts).forEach(chart => {
            if (chart) chart.destroy();
        });
    }
}

// Global functions for button actions
window.requestCorrection = () => dashboard.requestCorrection();
window.viewRecommendations = () => window.open('/recommendations', '_blank');
window.refreshFeed = () => dashboard.updateLiveFeed();
window.openVotingInterface = () => dashboard.openVotingInterface();
window.applySynergyCorrection = () => dashboard.applySynergyCorrection();
window.resetSynergy = () => alert('Reset systemu - funkcja w przygotowaniu');
window.emergencyMode = () => alert('Tryb awaryjny - funkcja w przygotowaniu');

// Initialize dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.dashboard = new SynergyDashboard();
});

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SynergyDashboard;
}