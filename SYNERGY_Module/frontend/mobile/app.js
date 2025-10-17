// SYNERGY Mobile Dashboard - Progressive Web App JavaScript
// Meta-Geniusz-mózg_Boga Mobile Control Center
// MTAQuestWebsideX.com - Advanced Collective Intelligence Mobile Interface

class SynergyMobileApp {
    constructor() {
        this.apiBase = window.location.origin;
        this.updateInterval = 10000; // 10 seconds for mobile
        this.lastUpdate = Date.now();
        this.isUpdating = false;
        this.isOnline = navigator.onLine;
        this.cachedData = {};
        
        console.log('🧠 Inicjalizacja SYNERGY Mobile App...');
        this.initializeApp();
    }
    
    async initializeApp() {
        try {
            // Load cached data first
            this.loadCachedData();
            
            // Update connection status
            this.updateConnectionStatus();
            
            // Load fresh data if online
            if (this.isOnline) {
                await this.loadFreshData();
            } else {
                this.showOfflineMode();
            }
            
            // Start periodic updates
            this.startPeriodicUpdates();
            
            // Setup event listeners
            this.setupEventListeners();
            
            console.log('✅ SYNERGY Mobile App gotowa do działania');
            
        } catch (error) {
            console.error('❌ Błąd inicjalizacji mobile app:', error);
            this.showErrorState();
        }
    }
    
    loadCachedData() {
        try {
            const cached = localStorage.getItem('synergy_mobile_cache');
            if (cached) {
                this.cachedData = JSON.parse(cached);
                this.updateUIWithData(this.cachedData);
                console.log('📱 Załadowano dane z cache');
            }
        } catch (error) {
            console.error('Błąd ładowania cache:', error);
        }
    }
    
    async loadFreshData() {
        try {
            this.setLoadingState(true);
            
            // Load dashboard data
            const dashboardResponse = await fetch(`${this.apiBase}/api/synergy/dashboard`);
            if (dashboardResponse.ok) {
                const dashboardData = await dashboardResponse.json();
                this.cachedData = { ...this.cachedData, ...dashboardData };
                
                // Cache the data
                localStorage.setItem('synergy_mobile_cache', JSON.stringify(this.cachedData));
                
                // Update UI
                this.updateUIWithData(this.cachedData);
                
                // Update timestamp
                this.updateElement('lastUpdate', new Date().toLocaleTimeString('pl-PL'));
                
                console.log('📡 Dane odświeżone z serwera');
            }
            
        } catch (error) {
            console.error('Błąd ładowania świeżych danych:', error);
            if (Object.keys(this.cachedData).length === 0) {
                this.showErrorState();
            }
        } finally {
            this.setLoadingState(false);
        }
    }
    
    updateUIWithData(data) {
        // System status
        const systemStatus = data.meta_analysis?.evolution_phase || 'TRANSCENDENT';
        this.updateElement('systemStatus', systemStatus);
        
        // Current decision
        const currentDecision = data.current_decision;
        if (currentDecision) {
            this.updateElement('decisionText', currentDecision.decision || 'Brak aktualnej decyzji');
            this.updateElement('confidence', Math.round((currentDecision.confidence || 0) * 100) + '%');
            this.updateElement('riskLevel', Math.round((currentDecision.risk_level || 0) * 100) + '%');
            this.updateElement('spiralLevel', currentDecision.spiral_level || '0');
            
            if (currentDecision.timestamp) {
                const time = new Date(currentDecision.timestamp).toLocaleTimeString('pl-PL');
                this.updateElement('decisionTime', time);
            }
        }
        
        // Module statuses
        const moduleStatuses = data.module_statuses || {};
        this.updateModuleStatus('consciousness', moduleStatuses['7_SYSTEM_SELF']);
        this.updateModuleStatus('globalvision', moduleStatuses['GlobalVision']);
        this.updateModuleStatus('spiral', moduleStatuses['SpiralMemory']);
        this.updateModuleStatus('synergyModule', moduleStatuses['SYNERGY_Collective']);
        
        // Module metrics
        const consciousnessLevels = data.consciousness_levels || {};
        this.updateElement('awarenessLevel', consciousnessLevels['7_SYSTEM_SELF'] || '9.2');
        
        // Voting data
        const votingData = data.voting_summary || {};
        this.updateElement('totalVotes', votingData.total_votes || '0');
        this.updateElement('consensusStrength', Math.round((votingData.consensus_strength || 0) * 100) + '%');
        
        // Recommendation
        const recommendation = data.collective_recommendation;
        if (recommendation) {
            this.updateElement('recommendationText', recommendation.meta_analysis || 'Generating spiral recommendation...');
            this.updateElement('targetLevel', 'LEVEL 7+');
        }
        
        // Update last decision in header
        if (currentDecision && currentDecision.decision) {
            const shortDecision = currentDecision.decision.substring(0, 50) + '...';
            this.updateElement('lastDecision', shortDecision);
        }
    }
    
    updateModuleStatus(moduleId, status) {
        const statusElement = document.getElementById(`${moduleId}Status`);
        if (statusElement) {
            statusElement.textContent = status || 'OFFLINE';
            statusElement.className = 'module-status';
            
            if (status === 'SELF_AWARE' || status === 'COLLECTIVE_HARMONY' || status === 'TRACKING' || status === 'DEMOCRACY') {
                statusElement.style.background = '#4caf50';
            } else if (status === 'OFFLINE') {
                statusElement.style.background = '#f44336';
            } else {
                statusElement.style.background = '#ff9800';
            }
        }
    }
    
    updateConnectionStatus() {
        const statusDot = document.getElementById('statusDot');
        const statusText = document.getElementById('statusText');
        const connectionStatus = document.getElementById('connectionStatus');
        
        if (this.isOnline) {
            connectionStatus.className = 'connection-status online';
            statusText.textContent = 'Online';
        } else {
            connectionStatus.className = 'connection-status offline';
            statusText.textContent = 'Offline';
        }
    }
    
    setupEventListeners() {
        // Online/Offline events
        window.addEventListener('online', () => {
            this.isOnline = true;
            this.updateConnectionStatus();
            this.hideOfflineMessage();
            this.loadFreshData();
            this.addActivityItem('🌐 Połączenie przywrócone');
        });
        
        window.addEventListener('offline', () => {
            this.isOnline = false;
            this.updateConnectionStatus();
            this.showOfflineMessage();
            this.addActivityItem('📱 Przełączono w tryb offline');
        });
        
        // Touch events for mobile
        document.addEventListener('touchstart', () => {}, { passive: true });
        
        // Visibility change (app focus)
        document.addEventListener('visibilitychange', () => {
            if (!document.hidden && this.isOnline) {
                this.loadFreshData();
            }
        });
        
        // Pull to refresh simulation
        let startY = 0;
        document.addEventListener('touchstart', (e) => {
            startY = e.touches[0].clientY;
        }, { passive: true });
        
        document.addEventListener('touchmove', (e) => {
            const currentY = e.touches[0].clientY;
            if (startY < 50 && currentY - startY > 100) {
                this.refreshData();
            }
        }, { passive: true });
    }
    
    startPeriodicUpdates() {
        setInterval(() => {
            if (!this.isUpdating && this.isOnline && !document.hidden) {
                this.periodicUpdate();
            }
        }, this.updateInterval);
    }
    
    async periodicUpdate() {
        this.isUpdating = true;
        
        try {
            await this.loadFreshData();
            this.addActivityItem('🔄 Dane automatycznie odświeżone');
        } catch (error) {
            console.error('Błąd aktualizacji:', error);
        } finally {
            this.isUpdating = false;
        }
    }
    
    addActivityItem(text) {
        const activityFeed = document.getElementById('activityFeed');
        if (!activityFeed) return;
        
        const timestamp = new Date().toLocaleTimeString('pl-PL');
        
        const activityItem = document.createElement('div');
        activityItem.className = 'activity-item';
        activityItem.innerHTML = `
            <span class="activity-time">${timestamp}</span>
            <span class="activity-text">${text}</span>
        `;
        
        activityFeed.insertBefore(activityItem, activityFeed.firstChild);
        
        // Keep only last 10 items
        while (activityFeed.children.length > 10) {
            activityFeed.removeChild(activityFeed.lastChild);
        }
    }
    
    setLoadingState(isLoading) {
        const elements = ['currentDecision', 'spiralRecommendation'];
        elements.forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                if (isLoading) {
                    element.classList.add('loading');
                } else {
                    element.classList.remove('loading');
                }
            }
        });
    }
    
    showOfflineMessage() {
        const offlineMessage = document.getElementById('offlineMessage');
        if (offlineMessage) {
            offlineMessage.style.display = 'flex';
        }
    }
    
    hideOfflineMessage() {
        const offlineMessage = document.getElementById('offlineMessage');
        if (offlineMessage) {
            offlineMessage.style.display = 'none';
        }
    }
    
    showErrorState() {
        this.updateElement('systemStatus', 'ERROR');
        this.updateElement('decisionText', 'Błąd połączenia z systemem');
        this.addActivityItem('❌ Błąd inicjalizacji systemu');
    }
    
    updateElement(id, content) {
        const element = document.getElementById(id);
        if (element) {
            element.innerHTML = content;
        }
    }
    
    async refreshData() {
        if (!this.isOnline) {
            this.showNotification('📱 Brak połączenia internetowego', 'warning');
            return;
        }
        
        this.addActivityItem('🔄 Ręczne odświeżanie danych...');
        await this.loadFreshData();
        this.showNotification('✅ Dane odświeżone', 'success');
    }
    
    showNotification(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 80px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            z-index: 200;
            font-size: 0.9em;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(100, 255, 218, 0.3);
        `;
        
        document.body.appendChild(notification);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            if (document.body.contains(notification)) {
                document.body.removeChild(notification);
            }
        }, 3000);
    }
}

// Global action functions
async function requestCorrection() {
    if (!window.mobileApp.isOnline) {
        window.mobileApp.showNotification('📱 Funkcja wymaga połączenia internetowego', 'warning');
        return;
    }
    
    try {
        const response = await fetch(`${window.mobileApp.apiBase}/api/synergy/apply-correction`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                correction_type: 'mobile_request',
                intensity: 0.7,
                reason: 'Mobile dashboard user request'
            })
        });
        
        if (response.ok) {
            window.mobileApp.showNotification('⚡ Korekta została zaproponowana', 'success');
            window.mobileApp.addActivityItem('⚡ Zaproponowano korektę SYNERGY');
            setTimeout(() => window.mobileApp.refreshData(), 2000);
        } else {
            throw new Error('Failed to submit correction');
        }
    } catch (error) {
        window.mobileApp.showNotification('❌ Błąd podczas aplikowania korekty', 'error');
    }
}

async function refreshRecommendation() {
    window.mobileApp.addActivityItem('🌀 Odświeżanie rekomendacji spiralnej...');
    await window.mobileApp.refreshData();
}

function openVotingInterface() {
    if (window.mobileApp.isOnline) {
        window.open('/synergy-voting', '_blank');
        window.mobileApp.addActivityItem('🗳️ Otwarto interface głosowania');
    } else {
        window.mobileApp.showNotification('📱 Głosowanie wymaga połączenia internetowego', 'warning');
    }
}

function viewFullDashboard() {
    if (window.mobileApp.isOnline) {
        window.open('/synergy-dashboard', '_blank');
        window.mobileApp.addActivityItem('📊 Otwarto pełny dashboard');
    } else {
        window.mobileApp.showNotification('📱 Pełny dashboard wymaga połączenia internetowego', 'warning');
    }
}

// Initialize mobile app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.mobileApp = new SynergyMobileApp();
    
    // Add initial activity
    setTimeout(() => {
        window.mobileApp.addActivityItem('🧠 SYNERGY Mobile Dashboard uruchomiony');
    }, 1000);
});

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SynergyMobileApp;
}