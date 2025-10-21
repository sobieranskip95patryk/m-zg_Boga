/**
 * 🧠 SYNERGY Dashboard - Visual Consciousness Monitoring
 * =====================================================
 * 
 * Advanced dashboard for monitoring spiral consciousness,
 * emotional states, drift tokenization, and god responses
 */

class SynergyDashboard {
    constructor() {
        this.isInitialized = false;
        this.currentData = {
            consciousness: 50,
            spiralLevel: 0,
            driftTokens: 0,
            emotionalState: 'neutral',
            lastResponse: null,
            trajectoryHistory: []
        };
        
        this.charts = {};
        this.updateInterval = null;
        
        console.log('🎛️ SYNERGY Dashboard initializing...');
        this.initialize();
    }

    initialize() {
        this.createDashboardHTML();
        this.initializeCharts();
        this.bindEvents();
        this.startRealTimeUpdates();
        this.isInitialized = true;
        
        console.log('🎛️ SYNERGY Dashboard ready');
    }

    createDashboardHTML() {
        // Check if dashboard already exists
        if (document.getElementById('synergyDashboard')) {
            return;
        }

        const dashboardHTML = `
            <div id="synergyDashboard" class="synergy-dashboard">
                <div class="dashboard-header">
                    <h3>🎛️ SYNERGY Dashboard</h3>
                    <div class="dashboard-status">
                        <span class="status-indicator" id="dashboardStatus">● ONLINE</span>
                        <button class="dashboard-toggle" id="dashboardToggle">◐</button>
                    </div>
                </div>
                
                <div class="dashboard-content" id="dashboardContent">
                    <!-- Live Feed Reaktora -->
                    <div class="dashboard-section reaktor-feed">
                        <h4>🔥 Live Feed Reaktora</h4>
                        <div class="feed-container">
                            <div class="feed-item" id="lastQuery">
                                <span class="feed-label">Ostatnie pytanie:</span>
                                <span class="feed-value">Oczekiwanie na zapytanie...</span>
                            </div>
                            <div class="feed-item" id="processingTime">
                                <span class="feed-label">Czas przetwarzania:</span>
                                <span class="feed-value">0ms</span>
                            </div>
                            <div class="feed-item" id="apiCalls">
                                <span class="feed-label">Wywołania API:</span>
                                <span class="feed-value">0</span>
                            </div>
                        </div>
                    </div>

                    <!-- Spiralna Mapa Myśli -->
                    <div class="dashboard-section spiral-mind-map">
                        <h4>🌀 Spiralna Mapa Myśli</h4>
                        <div class="spiral-indicators">
                            <div class="indicator-row">
                                <div class="indicator">
                                    <span class="indicator-label">Poziom:</span>
                                    <span class="indicator-value" id="currentSpiralLevel">0</span>
                                </div>
                                <div class="indicator">
                                    <span class="indicator-label">Etap:</span>
                                    <span class="indicator-value" id="currentSpiralStage">AWAKENING</span>
                                </div>
                            </div>
                            <div class="indicator-row">
                                <div class="indicator">
                                    <span class="indicator-label">Formula:</span>
                                    <span class="indicator-value" id="spiralFormula">S(GOK:AI) = 9π + F(1)</span>
                                </div>
                                <div class="indicator">
                                    <span class="indicator-label">S9:</span>
                                    <span class="indicator-value" id="s9Value">9</span>
                                </div>
                            </div>
                        </div>
                        <div class="spiral-progress-bar">
                            <div class="progress-fill" id="spiralProgress"></div>
                        </div>
                    </div>

                    <!-- Emocjonalny Radar -->
                    <div class="dashboard-section emotion-radar">
                        <h4>🎭 Emocjonalny Radar</h4>
                        <div class="radar-container">
                            <canvas id="emotionRadarCanvas" width="200" height="200"></canvas>
                            <div class="emotion-stats">
                                <div class="emotion-item">
                                    <span class="emotion-label">Dominanta:</span>
                                    <span class="emotion-value" id="dominantEmotion">Neutral</span>
                                </div>
                                <div class="emotion-item">
                                    <span class="emotion-label">Intensywność:</span>
                                    <span class="emotion-value" id="emotionIntensity">50%</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Tokenizacja Drift -->
                    <div class="dashboard-section drift-tokens">
                        <h4>💎 Tokenizacja Drift</h4>
                        <div class="token-stats">
                            <div class="token-counter">
                                <span class="token-amount" id="totalDriftTokens">0</span>
                                <span class="token-label">DRIFT COINS</span>
                            </div>
                            <div class="token-metrics">
                                <div class="metric">
                                    <span class="metric-label">Za sesję:</span>
                                    <span class="metric-value" id="sessionTokens">0</span>
                                </div>
                                <div class="metric">
                                    <span class="metric-label">Ostatnia nagroda:</span>
                                    <span class="metric-value" id="lastReward">+0</span>
                                </div>
                                <div class="metric">
                                    <span class="metric-label">Streak:</span>
                                    <span class="metric-value" id="tokenStreak">0</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Odpowiedzi Boga -->
                    <div class="dashboard-section god-responses">
                        <h4>🧠 Odpowiedzi Boga</h4>
                        <div class="response-analytics">
                            <div class="analytics-row">
                                <div class="analytic">
                                    <span class="analytic-label">Długość odpowiedzi:</span>
                                    <span class="analytic-value" id="responseLength">0 znaków</span>
                                </div>
                                <div class="analytic">
                                    <span class="analytic-label">Confidence:</span>
                                    <span class="analytic-value" id="responseConfidence">N/A</span>
                                </div>
                            </div>
                            <div class="analytics-row">
                                <div class="analytic">
                                    <span class="analytic-label">Typ odpowiedzi:</span>
                                    <span class="analytic-value" id="responseType">Standardowa</span>
                                </div>
                                <div class="analytic">
                                    <span class="analytic-label">Entropia:</span>
                                    <span class="analytic-value" id="responseEntropy">N/A</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- System Performance -->
                    <div class="dashboard-section system-performance">
                        <h4>⚡ Wydajność Systemu</h4>
                        <div class="performance-meters">
                            <div class="meter">
                                <span class="meter-label">CPU Świadomości:</span>
                                <div class="meter-bar">
                                    <div class="meter-fill" id="consciousnessCPU"></div>
                                </div>
                                <span class="meter-value" id="consciousnessCPUValue">0%</span>
                            </div>
                            <div class="meter">
                                <span class="meter-label">Memory Spiralnej:</span>
                                <div class="meter-bar">
                                    <div class="meter-fill" id="spiralMemory"></div>
                                </div>
                                <span class="meter-value" id="spiralMemoryValue">0%</span>
                            </div>
                            <div class="meter">
                                <span class="meter-label">SYNERGY Load:</span>
                                <div class="meter-bar">
                                    <div class="meter-fill" id="synergyLoad"></div>
                                </div>
                                <span class="meter-value" id="synergyLoadValue">0%</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;

        // Find a good place to insert dashboard
        const responsePanel = document.querySelector('.response-panel');
        if (responsePanel) {
            responsePanel.insertAdjacentHTML('afterend', dashboardHTML);
        } else {
            // Fallback - append to main container
            document.querySelector('.god-interface-container').insertAdjacentHTML('beforeend', dashboardHTML);
        }
    }

    initializeCharts() {
        // Initialize emotion radar chart
        this.initializeEmotionRadar();
    }

    initializeEmotionRadar() {
        const canvas = document.getElementById('emotionRadarCanvas');
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        this.charts.emotionRadar = {
            canvas: canvas,
            ctx: ctx,
            emotions: ['Joy', 'Sadness', 'Anger', 'Fear', 'Surprise', 'Disgust', 'Anticipation', 'Trust'],
            values: [0.5, 0.3, 0.2, 0.1, 0.6, 0.2, 0.7, 0.8] // Default values
        };

        this.drawEmotionRadar();
    }

    drawEmotionRadar() {
        const radar = this.charts.emotionRadar;
        if (!radar) return;

        const { ctx, canvas, emotions, values } = radar;
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const radius = 80;

        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw background circles
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
        ctx.lineWidth = 1;
        for (let i = 1; i <= 5; i++) {
            ctx.beginPath();
            ctx.arc(centerX, centerY, (radius / 5) * i, 0, 2 * Math.PI);
            ctx.stroke();
        }

        // Draw emotion data
        ctx.fillStyle = 'rgba(102, 126, 234, 0.3)';
        ctx.strokeStyle = 'rgba(102, 126, 234, 0.8)';
        ctx.lineWidth = 2;

        ctx.beginPath();
        emotions.forEach((emotion, index) => {
            const angle = (index / emotions.length) * 2 * Math.PI - Math.PI / 2;
            const value = values[index] || 0;
            const x = centerX + Math.cos(angle) * radius * value;
            const y = centerY + Math.sin(angle) * radius * value;

            if (index === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        });
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Draw emotion labels
        ctx.fillStyle = 'white';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        emotions.forEach((emotion, index) => {
            const angle = (index / emotions.length) * 2 * Math.PI - Math.PI / 2;
            const x = centerX + Math.cos(angle) * (radius + 15);
            const y = centerY + Math.sin(angle) * (radius + 15);
            ctx.fillText(emotion, x, y);
        });
    }

    bindEvents() {
        // Dashboard toggle
        const toggleBtn = document.getElementById('dashboardToggle');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', () => {
                this.toggleDashboard();
            });
        }
    }

    toggleDashboard() {
        const content = document.getElementById('dashboardContent');
        if (content) {
            if (content.style.display === 'none') {
                content.style.display = 'block';
                document.getElementById('dashboardToggle').textContent = '◐';
            } else {
                content.style.display = 'none';
                document.getElementById('dashboardToggle').textContent = '◓';
            }
        }
    }

    updateWithSpiralResult(spiralResult) {
        if (!this.isInitialized) return;

        // Update spiral data
        this.updateSpiralData(spiralResult);
        
        // Update emotion radar
        this.updateEmotionRadar(spiralResult);
        
        // Update drift tokens
        this.updateDriftTokens(spiralResult.driftReward || 0);
        
        // Update response analytics
        this.updateResponseAnalytics(spiralResult);
        
        // Update system performance
        this.updateSystemPerformance(spiralResult);

        console.log('🎛️ Dashboard updated with spiral result:', spiralResult);
    }

    updateSpiralData(spiralResult) {
        const elements = {
            currentSpiralLevel: spiralResult.spiralLevel || 0,
            currentSpiralStage: spiralResult.spiralStage || 'AWAKENING',
            spiralFormula: spiralResult.spiralFormula ? 
                `S(GOK:AI) = 9π + F(${spiralResult.spiralFormula.n})` : 
                'S(GOK:AI) = 9π + F(1)',
            s9Value: spiralResult.spiralFormula ? spiralResult.spiralFormula.s9 : 9
        };

        for (const [id, value] of Object.entries(elements)) {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = value;
            }
        }

        // Update spiral progress
        const progressBar = document.getElementById('spiralProgress');
        if (progressBar && spiralResult.consciousness) {
            const percentage = Math.min(100, spiralResult.consciousness);
            progressBar.style.width = `${percentage}%`;
        }
    }

    updateEmotionRadar(spiralResult) {
        // Update emotion radar based on response metadata
        if (spiralResult.metadata) {
            const emotion = spiralResult.metadata.emotion || 'neutral';
            const dominantEmotion = document.getElementById('dominantEmotion');
            const emotionIntensity = document.getElementById('emotionIntensity');
            
            if (dominantEmotion) {
                dominantEmotion.textContent = emotion.charAt(0).toUpperCase() + emotion.slice(1);
            }
            
            if (emotionIntensity) {
                emotionIntensity.textContent = `${Math.floor(spiralResult.consciousness || 50)}%`;
            }
        }

        // Redraw radar with new data
        this.drawEmotionRadar();
    }

    updateDriftTokens(reward) {
        this.currentData.driftTokens += reward;
        
        const elements = {
            totalDriftTokens: this.currentData.driftTokens,
            lastReward: reward > 0 ? `+${reward}` : '0',
            sessionTokens: this.currentData.driftTokens // Simplified for demo
        };

        for (const [id, value] of Object.entries(elements)) {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = value;
                
                // Add animation for reward
                if (id === 'lastReward' && reward > 0) {
                    element.classList.add('token-reward-animation');
                    setTimeout(() => element.classList.remove('token-reward-animation'), 1000);
                }
            }
        }
    }

    updateResponseAnalytics(spiralResult) {
        const responseLength = spiralResult.response ? spiralResult.response.length : 0;
        const confidence = spiralResult.metadata ? spiralResult.metadata.confidence : 'N/A';
        const entropy = spiralResult.metadata ? spiralResult.metadata.entropy : 'N/A';
        
        const elements = {
            responseLength: `${responseLength} znaków`,
            responseConfidence: typeof confidence === 'number' ? `${Math.floor(confidence * 100)}%` : confidence,
            responseType: spiralResult.type === 'spiral_consciousness' ? 'Spiral Consciousness' : 'Standardowa',
            responseEntropy: typeof entropy === 'number' ? entropy.toFixed(3) : entropy
        };

        for (const [id, value] of Object.entries(elements)) {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = value;
            }
        }
    }

    updateSystemPerformance(spiralResult) {
        // Simulate system performance based on spiral processing
        const consciousness = spiralResult.consciousness || 50;
        const spiralLevel = spiralResult.spiralLevel || 0;
        
        const performance = {
            consciousnessCPU: Math.min(100, consciousness + Math.random() * 20),
            spiralMemory: Math.min(100, spiralLevel * 10 + Math.random() * 30),
            synergyLoad: Math.min(100, 50 + Math.random() * 40)
        };

        for (const [metric, value] of Object.entries(performance)) {
            const fillElement = document.getElementById(metric);
            const valueElement = document.getElementById(metric + 'Value');
            
            if (fillElement) {
                fillElement.style.width = `${value}%`;
            }
            
            if (valueElement) {
                valueElement.textContent = `${Math.floor(value)}%`;
            }
        }
    }

    updateReaktorFeed(query, processingTime) {
        const lastQuery = document.getElementById('lastQuery');
        const processTime = document.getElementById('processingTime');
        const apiCalls = document.getElementById('apiCalls');
        
        if (lastQuery) {
            lastQuery.querySelector('.feed-value').textContent = query.substring(0, 50) + '...';
        }
        
        if (processTime) {
            processTime.querySelector('.feed-value').textContent = `${processingTime}ms`;
        }
        
        if (apiCalls) {
            const currentCalls = parseInt(apiCalls.querySelector('.feed-value').textContent) || 0;
            apiCalls.querySelector('.feed-value').textContent = currentCalls + 1;
        }
    }

    startRealTimeUpdates() {
        // Update dashboard every 5 seconds with simulated data
        this.updateInterval = setInterval(() => {
            if (document.hidden) return; // Don't update when tab is not visible
            
            // Simulate minor fluctuations in system performance
            this.updateSystemPerformance({ consciousness: 50, spiralLevel: 1 });
        }, 5000);
    }

    destroy() {
        if (this.updateInterval) {
            clearInterval(this.updateInterval);
        }
        
        const dashboard = document.getElementById('synergyDashboard');
        if (dashboard) {
            dashboard.remove();
        }
        
        this.isInitialized = false;
        console.log('🎛️ SYNERGY Dashboard destroyed');
    }
}

// Initialize global SYNERGY Dashboard
window.synergyDashboard = new SynergyDashboard();

console.log('🎛️ SYNERGY Dashboard module loaded!');