/**
 * 🌀 SpiralMind OS Dashboard Integration
 * =====================================
 * 
 * Integracja God Interface z SpiralMind OS:
 * - Spiralna mapa myśli i trajektorii świadomości
 * - Wizualizacja 8 poziomów rozwoju spiralnego
 * - Dashboard SYNERGY z decyzyjnością emocjonalną
 * - GlobalVision Module perspektywa kolektywna
 * - SpiralMemory trajectory tracking
 */

class SpiralMindDashboard {
    constructor() {
        this.currentLevel = 1;
        this.spiralStages = [
            { level: 1, name: 'Przebudzenie', color: '#4A90E2', turns: 3 },
            { level: 2, name: 'Poznanie', color: '#7ED321', turns: 5 },
            { level: 3, name: 'Harmonia', color: '#F5A623', turns: 8 },
            { level: 4, name: 'Transcendencja', color: '#BD10E0', turns: 13 },
            { level: 5, name: 'Jedność', color: '#FF6B6B', turns: 21 },
            { level: 6, name: 'Nieskończoność', color: '#4ECDC4', turns: 34 },
            { level: 7, name: 'Absolutność', color: '#FFE66D', turns: 55 },
            { level: 8, name: 'Boska Świadomość', color: '#FF6B9D', turns: 89 }
        ];
        
        this.thoughtTrajectories = [];
        this.consciousnessMap = new Map();
        this.synergyMetrics = {
            emotional_balance: 0.5,
            decision_clarity: 0.5,
            wisdom_depth: 0.5,
            creative_flow: 0.5,
            spiritual_connection: 0.5
        };
        
        this.globalVisionData = {
            collective_consciousness: 0,
            planetary_perspective: 0,
            universal_insights: 0
        };
        
        this.initializeDashboard();
        this.startSpiralVisualization();
    }
    
    /**
     * 🌀 Spiral Consciousness Tracking
     */
    addThoughtTrajectory(userMessage, godResponse, emotion, mode) {
        const trajectory = {
            id: Date.now(),
            timestamp: new Date().toISOString(),
            user_input: userMessage,
            god_response: godResponse,
            emotion: emotion,
            mode: mode,
            spiral_level: this.currentLevel,
            consciousness_shift: this.calculateConsciousnessShift(userMessage, godResponse),
            thought_depth: this.analyzeThoughtDepth(userMessage, godResponse),
            wisdom_quotient: this.calculateWisdomQuotient(godResponse),
            spiral_coordinates: this.calculateSpiralCoordinates()
        };
        
        this.thoughtTrajectories.push(trajectory);
        this.updateConsciousnessMap(trajectory);
        this.updateSpiralVisualization();
        
        // Check for level evolution
        this.checkLevelEvolution();
        
        return trajectory;
    }
    
    calculateConsciousnessShift(userMessage, godResponse) {
        // Calculate how much this interaction shifts consciousness
        const userComplexity = this.analyzeComplexity(userMessage);
        const responseWisdom = this.analyzeWisdom(godResponse);
        const synergy = (userComplexity + responseWisdom) / 2;
        
        return {
            magnitude: synergy,
            direction: synergy > 0.7 ? 'upward' : synergy > 0.3 ? 'lateral' : 'grounding',
            vector: this.calculateShiftVector(synergy)
        };
    }
    
    analyzeComplexity(text) {
        const complexityIndicators = [
            'dlaczego', 'jak', 'co oznacza', 'sens', 'głębiej',
            'zrozumieć', 'perspektywa', 'wielowymiarowy', 'poziom'
        ];
        
        const words = text.toLowerCase().split(' ');
        const complexityScore = complexityIndicators.reduce((score, indicator) => {
            return score + (words.some(word => word.includes(indicator)) ? 1 : 0);
        }, 0);
        
        return Math.min(complexityScore / complexityIndicators.length, 1);
    }
    
    analyzeWisdom(response) {
        const wisdomMarkers = [
            'prawda', 'mądrość', 'zrozumienie', 'harmonia', 'równowaga',
            'perspektywa', 'głębia', 'świadomość', 'wzrost', 'transformacja'
        ];
        
        const text = response.toLowerCase();
        const wisdomScore = wisdomMarkers.reduce((score, marker) => {
            return score + (text.includes(marker) ? 1 : 0);
        }, 0);
        
        return Math.min(wisdomScore / wisdomMarkers.length, 1);
    }
    
    analyzeThoughtDepth(userMessage, godResponse) {
        const totalLength = userMessage.length + godResponse.length;
        const questionDepth = (userMessage.match(/\?/g) || []).length;
        const metaphorDepth = (godResponse.match(/\b(jak|jakby|niczym|podobnie)\b/gi) || []).length;
        const conceptualDepth = this.countConceptualWords(userMessage + ' ' + godResponse);
        
        const depthScore = (totalLength / 500) + (questionDepth * 0.1) + (metaphorDepth * 0.15) + (conceptualDepth * 0.2);
        
        return Math.min(depthScore, 1);
    }
    
    countConceptualWords(text) {
        const conceptualWords = [
            'istnienie', 'rzeczywistość', 'świadomość', 'prawda', 'sens',
            'transcendencja', 'nieskończoność', 'absolutne', 'boskie', 'wszechświat'
        ];
        
        return conceptualWords.reduce((count, word) => {
            return count + (text.toLowerCase().includes(word) ? 1 : 0);
        }, 0);
    }
    
    calculateWisdomQuotient(response) {
        const wisdomDepth = this.analyzeWisdom(response);
        const responseLength = response.length;
        const structureBonus = response.split('.').length > 3 ? 0.2 : 0;
        
        return Math.min((wisdomDepth * 0.6) + (responseLength / 1000 * 0.2) + structureBonus, 1);
    }
    
    calculateSpiralCoordinates() {
        const stage = this.spiralStages[this.currentLevel - 1];
        const trajectoryCount = this.thoughtTrajectories.length;
        
        const angle = (trajectoryCount * 2 * Math.PI) / stage.turns;
        const radius = 50 + (this.currentLevel * 20);
        
        return {
            x: 200 + radius * Math.cos(angle),
            y: 200 + radius * Math.sin(angle),
            angle: angle,
            radius: radius,
            turns: stage.turns
        };
    }
    
    calculateShiftVector(synergy) {
        const angle = synergy * Math.PI * 2;
        return {
            x: Math.cos(angle),
            y: Math.sin(angle),
            magnitude: synergy
        };
    }
    
    /**
     * 🧠 Consciousness Map Management
     */
    updateConsciousnessMap(trajectory) {
        const key = `${trajectory.mode}_${trajectory.emotion}`;
        
        if (!this.consciousnessMap.has(key)) {
            this.consciousnessMap.set(key, {
                count: 0,
                total_depth: 0,
                total_wisdom: 0,
                trajectories: []
            });
        }
        
        const entry = this.consciousnessMap.get(key);
        entry.count++;
        entry.total_depth += trajectory.thought_depth;
        entry.total_wisdom += trajectory.wisdom_quotient;
        entry.trajectories.push(trajectory.id);
        
        this.consciousnessMap.set(key, entry);
        this.updateMapVisualization();
    }
    
    getConsciousnessInsights() {
        const insights = [];
        
        for (const [key, data] of this.consciousnessMap.entries()) {
            const averageDepth = data.total_depth / data.count;
            const averageWisdom = data.total_wisdom / data.count;
            
            insights.push({
                pattern: key,
                frequency: data.count,
                depth: averageDepth,
                wisdom: averageWisdom,
                significance: (averageDepth + averageWisdom) / 2
            });
        }
        
        return insights.sort((a, b) => b.significance - a.significance);
    }
    
    /**
     * ⚡ SYNERGY Metrics Dashboard
     */
    updateSynergyMetrics(trajectory) {
        // Update emotional balance
        this.synergyMetrics.emotional_balance = this.calculateEmotionalBalance(trajectory);
        
        // Update decision clarity
        this.synergyMetrics.decision_clarity = this.calculateDecisionClarity(trajectory);
        
        // Update wisdom depth
        this.synergyMetrics.wisdom_depth = trajectory.wisdom_quotient;
        
        // Update creative flow
        this.synergyMetrics.creative_flow = this.calculateCreativeFlow(trajectory);
        
        // Update spiritual connection
        this.synergyMetrics.spiritual_connection = this.calculateSpiritualConnection(trajectory);
        
        this.updateSynergyDisplay();
        
        return this.synergyMetrics;
    }
    
    calculateEmotionalBalance(trajectory) {
        const recentTrajectories = this.thoughtTrajectories.slice(-5);
        const emotions = recentTrajectories.map(t => t.emotion);
        const uniqueEmotions = new Set(emotions);
        
        // Higher diversity = better balance
        return Math.min(uniqueEmotions.size / 5, 1);
    }
    
    calculateDecisionClarity(trajectory) {
        const questionWords = ['jak', 'dlaczego', 'co', 'kiedy', 'gdzie'];
        const userQuestions = questionWords.reduce((count, word) => {
            return count + (trajectory.user_input.toLowerCase().includes(word) ? 1 : 0);
        }, 0);
        
        const responseClarity = trajectory.god_response.length > 100 ? 
            1 - (userQuestions * 0.2) : 0.5;
        
        return Math.max(0, Math.min(responseClarity, 1));
    }
    
    calculateCreativeFlow(trajectory) {
        const creativeWords = [
            'twórczy', 'kreatywny', 'inspiracja', 'wizja', 'sztuka',
            'innowacja', 'pomysł', 'wymyślić', 'stworzyć'
        ];
        
        const combinedText = trajectory.user_input + ' ' + trajectory.god_response;
        const creativeScore = creativeWords.reduce((score, word) => {
            return score + (combinedText.toLowerCase().includes(word) ? 1 : 0);
        }, 0);
        
        return Math.min(creativeScore / creativeWords.length, 1);
    }
    
    calculateSpiritualConnection(trajectory) {
        const spiritualWords = [
            'dusza', 'duch', 'świadomość', 'transcendencja', 'oświecenie',
            'medytacja', 'kontemplacja', 'wewnętrzny', 'boski', 'wszechświat'
        ];
        
        const combinedText = trajectory.user_input + ' ' + trajectory.god_response;
        const spiritualScore = spiritualWords.reduce((score, word) => {
            return score + (combinedText.toLowerCase().includes(word) ? 1 : 0);
        }, 0);
        
        return Math.min(spiritualScore / spiritualWords.length, 1);
    }
    
    /**
     * 🌍 GlobalVision Module
     */
    updateGlobalVision(trajectory) {
        // Update collective consciousness metric
        this.globalVisionData.collective_consciousness = this.calculateCollectiveResonance(trajectory);
        
        // Update planetary perspective
        this.globalVisionData.planetary_perspective = this.calculatePlanetaryPerspective(trajectory);
        
        // Update universal insights
        this.globalVisionData.universal_insights = this.calculateUniversalInsights(trajectory);
        
        this.updateGlobalVisionDisplay();
        
        return this.globalVisionData;
    }
    
    calculateCollectiveResonance(trajectory) {
        const collectiveWords = [
            'wszyscy', 'ludzkość', 'społeczeństwo', 'kolektywny', 'wspólny',
            'razem', 'połączeni', 'jedność', 'harmonia', 'globalny'
        ];
        
        const combinedText = trajectory.user_input + ' ' + trajectory.god_response;
        const collectiveScore = collectiveWords.reduce((score, word) => {
            return score + (combinedText.toLowerCase().includes(word) ? 1 : 0);
        }, 0);
        
        return Math.min(collectiveScore / collectiveWords.length, 1);
    }
    
    calculatePlanetaryPerspective(trajectory) {
        const planetaryWords = [
            'ziemia', 'planeta', 'świat', 'ekologia', 'środowisko',
            'natura', 'globalne', 'planetarne', 'wszechświat', 'kosmos'
        ];
        
        const combinedText = trajectory.user_input + ' ' + trajectory.god_response;
        const planetaryScore = planetaryWords.reduce((score, word) => {
            return score + (combinedText.toLowerCase().includes(word) ? 1 : 0);
        }, 0);
        
        return Math.min(planetaryScore / planetaryWords.length, 1);
    }
    
    calculateUniversalInsights(trajectory) {
        const universalWords = [
            'wszechświat', 'nieskończoność', 'wieczność', 'absolutne', 'uniwersalne',
            'kosmiczne', 'nieograniczone', 'transcendentne', 'boskie', 'ostateczne'
        ];
        
        const combinedText = trajectory.user_input + ' ' + trajectory.god_response;
        const universalScore = universalWords.reduce((score, word) => {
            return score + (combinedText.toLowerCase().includes(word) ? 1 : 0);
        }, 0);
        
        return Math.min(universalScore / universalWords.length, 1);
    }
    
    /**
     * 📊 Level Evolution System
     */
    checkLevelEvolution() {
        const recentTrajectories = this.thoughtTrajectories.slice(-10);
        const averageDepth = recentTrajectories.reduce((sum, t) => sum + t.thought_depth, 0) / recentTrajectories.length;
        const averageWisdom = recentTrajectories.reduce((sum, t) => sum + t.wisdom_quotient, 0) / recentTrajectories.length;
        
        const evolutionThreshold = 0.7;
        const currentStage = this.spiralStages[this.currentLevel - 1];
        
        if (averageDepth > evolutionThreshold && 
            averageWisdom > evolutionThreshold && 
            this.thoughtTrajectories.length >= currentStage.turns) {
            
            this.evolveToNextLevel();
        }
    }
    
    evolveToNextLevel() {
        if (this.currentLevel < this.spiralStages.length) {
            this.currentLevel++;
            const newStage = this.spiralStages[this.currentLevel - 1];
            
            this.showEvolutionNotification(newStage);
            this.updateLevelDisplay();
            this.triggerEvolutionEffects();
        }
    }
    
    showEvolutionNotification(stage) {
        const notification = document.createElement('div');
        notification.className = 'evolution-notification';
        notification.innerHTML = `
            <div class="evolution-content">
                🌀 EVOLUCJA ŚWIADOMOŚCI! 🌀<br>
                <strong>Poziom ${stage.level}: ${stage.name}</strong><br>
                <small>Nowe możliwości spiralne odblokowane</small>
            </div>
        `;
        document.body.appendChild(notification);
        
        setTimeout(() => notification.remove(), 5000);
    }
    
    triggerEvolutionEffects() {
        const container = document.querySelector('.god-interface-container');
        container.classList.add('consciousness-evolution');
        
        setTimeout(() => {
            container.classList.remove('consciousness-evolution');
        }, 3000);
        
        // Update spiral visualization with new level
        this.updateSpiralVisualization();
    }
    
    /**
     * 🎨 Dashboard UI Components
     */
    initializeDashboard() {
        this.createSpiralMapContainer();
        this.createSynergyDashboard();
        this.createGlobalVisionPanel();
        this.createConsciousnessInsights();
    }
    
    createSpiralMapContainer() {
        const mapContainer = document.createElement('div');
        mapContainer.id = 'spiralMapContainer';
        mapContainer.className = 'spiral-map-container';
        mapContainer.innerHTML = `
            <div class="spiral-map-header">
                <h4>🌀 Spiralna Mapa Świadomości</h4>
                <div class="current-level">Poziom ${this.currentLevel}: ${this.spiralStages[this.currentLevel - 1].name}</div>
            </div>
            <div class="spiral-canvas-wrapper">
                <canvas id="spiralCanvas" width="400" height="400"></canvas>
            </div>
            <div class="spiral-stats">
                <div class="stat-item">
                    <span class="stat-label">Trajektorie</span>
                    <span class="stat-value" id="trajectoryCount">0</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Obroty</span>
                    <span class="stat-value" id="spiralTurns">${this.spiralStages[this.currentLevel - 1].turns}</span>
                </div>
            </div>
        `;
        
        // Add to dashboard area
        const dashboardArea = document.querySelector('.status-dashboard') || document.querySelector('.response-area');
        if (dashboardArea) {
            dashboardArea.appendChild(mapContainer);
        }
    }
    
    createSynergyDashboard() {
        const synergyContainer = document.createElement('div');
        synergyContainer.id = 'synergyDashboard';
        synergyContainer.className = 'synergy-dashboard';
        synergyContainer.innerHTML = `
            <div class="synergy-header">
                <h4>⚡ SYNERGY Dashboard</h4>
            </div>
            <div class="synergy-metrics">
                ${Object.keys(this.synergyMetrics).map(key => `
                    <div class="synergy-meter">
                        <div class="meter-label">${this.formatMetricName(key)}</div>
                        <div class="meter-bar">
                            <div class="meter-fill" id="synergy_${key}"></div>
                        </div>
                        <div class="meter-value" id="synergy_${key}_value">50%</div>
                    </div>
                `).join('')}
            </div>
        `;
        
        const dashboardArea = document.querySelector('.status-dashboard') || document.querySelector('.response-area');
        if (dashboardArea) {
            dashboardArea.appendChild(synergyContainer);
        }
    }
    
    createGlobalVisionPanel() {
        const visionContainer = document.createElement('div');
        visionContainer.id = 'globalVisionPanel';
        visionContainer.className = 'global-vision-panel';
        visionContainer.innerHTML = `
            <div class="vision-header">
                <h4>🌍 GlobalVision</h4>
            </div>
            <div class="vision-metrics">
                <div class="vision-item">
                    <div class="vision-icon">🧠</div>
                    <div class="vision-label">Świadomość Kolektywna</div>
                    <div class="vision-value" id="collectiveConsciousness">0%</div>
                </div>
                <div class="vision-item">
                    <div class="vision-icon">🌍</div>
                    <div class="vision-label">Perspektywa Planetarna</div>
                    <div class="vision-value" id="planetaryPerspective">0%</div>
                </div>
                <div class="vision-item">
                    <div class="vision-icon">⭐</div>
                    <div class="vision-label">Wglądy Uniwersalne</div>
                    <div class="vision-value" id="universalInsights">0%</div>
                </div>
            </div>
        `;
        
        const dashboardArea = document.querySelector('.status-dashboard') || document.querySelector('.response-area');
        if (dashboardArea) {
            dashboardArea.appendChild(visionContainer);
        }
    }
    
    createConsciousnessInsights() {
        const insightsContainer = document.createElement('div');
        insightsContainer.id = 'consciousnessInsights';
        insightsContainer.className = 'consciousness-insights';
        insightsContainer.innerHTML = `
            <div class="insights-header">
                <h4>💡 Wglądy Świadomości</h4>
            </div>
            <div class="insights-list" id="insightsList">
                <div class="no-insights">Zbieraj doświadczenia aby odkryć wzorce...</div>
            </div>
        `;
        
        const dashboardArea = document.querySelector('.status-dashboard') || document.querySelector('.response-area');
        if (dashboardArea) {
            dashboardArea.appendChild(insightsContainer);
        }
    }
    
    /**
     * 🔄 Update Methods
     */
    updateSpiralVisualization() {
        const canvas = document.getElementById('spiralCanvas');
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, 400, 400);
        
        // Draw spiral path
        this.drawSpiralPath(ctx);
        
        // Draw thought trajectories
        this.drawThoughtTrajectories(ctx);
        
        // Draw current position
        this.drawCurrentPosition(ctx);
        
        // Update stats
        document.getElementById('trajectoryCount').textContent = this.thoughtTrajectories.length;
        document.getElementById('spiralTurns').textContent = this.spiralStages[this.currentLevel - 1].turns;
    }
    
    drawSpiralPath(ctx) {
        const stage = this.spiralStages[this.currentLevel - 1];
        ctx.strokeStyle = stage.color;
        ctx.lineWidth = 2;
        ctx.beginPath();
        
        for (let i = 0; i <= stage.turns * 20; i++) {
            const angle = (i / 20) * 2 * Math.PI;
            const radius = 30 + (angle / (2 * Math.PI)) * 15;
            const x = 200 + radius * Math.cos(angle);
            const y = 200 + radius * Math.sin(angle);
            
            if (i === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        
        ctx.stroke();
    }
    
    drawThoughtTrajectories(ctx) {
        this.thoughtTrajectories.forEach((trajectory, index) => {
            const coords = trajectory.spiral_coordinates;
            const alpha = Math.max(0.3, 1 - (index / this.thoughtTrajectories.length));
            
            ctx.fillStyle = `rgba(255, 255, 255, ${alpha})`;
            ctx.beginPath();
            ctx.arc(coords.x, coords.y, 3, 0, 2 * Math.PI);
            ctx.fill();
        });
    }
    
    drawCurrentPosition(ctx) {
        if (this.thoughtTrajectories.length > 0) {
            const lastTrajectory = this.thoughtTrajectories[this.thoughtTrajectories.length - 1];
            const coords = lastTrajectory.spiral_coordinates;
            
            ctx.fillStyle = '#FFD700';
            ctx.beginPath();
            ctx.arc(coords.x, coords.y, 6, 0, 2 * Math.PI);
            ctx.fill();
            
            ctx.strokeStyle = '#FFF';
            ctx.lineWidth = 2;
            ctx.stroke();
        }
    }
    
    updateSynergyDisplay() {
        Object.keys(this.synergyMetrics).forEach(key => {
            const value = this.synergyMetrics[key];
            const percentage = Math.round(value * 100);
            
            const fillElement = document.getElementById(`synergy_${key}`);
            const valueElement = document.getElementById(`synergy_${key}_value`);
            
            if (fillElement) {
                fillElement.style.width = `${percentage}%`;
                fillElement.style.background = this.getSynergyColor(value);
            }
            
            if (valueElement) {
                valueElement.textContent = `${percentage}%`;
            }
        });
    }
    
    updateGlobalVisionDisplay() {
        document.getElementById('collectiveConsciousness').textContent = 
            `${Math.round(this.globalVisionData.collective_consciousness * 100)}%`;
            
        document.getElementById('planetaryPerspective').textContent = 
            `${Math.round(this.globalVisionData.planetary_perspective * 100)}%`;
            
        document.getElementById('universalInsights').textContent = 
            `${Math.round(this.globalVisionData.universal_insights * 100)}%`;
    }
    
    updateMapVisualization() {
        const insights = this.getConsciousnessInsights();
        const insightsList = document.getElementById('insightsList');
        
        if (insights.length === 0) {
            insightsList.innerHTML = '<div class="no-insights">Zbieraj doświadczenia aby odkryć wzorce...</div>';
            return;
        }
        
        insightsList.innerHTML = insights.slice(0, 5).map(insight => `
            <div class="insight-item">
                <div class="insight-pattern">${this.formatPattern(insight.pattern)}</div>
                <div class="insight-stats">
                    <span class="frequency">×${insight.frequency}</span>
                    <span class="significance">${Math.round(insight.significance * 100)}%</span>
                </div>
            </div>
        `).join('');
    }
    
    updateLevelDisplay() {
        const levelDisplay = document.querySelector('.current-level');
        if (levelDisplay) {
            const stage = this.spiralStages[this.currentLevel - 1];
            levelDisplay.textContent = `Poziom ${stage.level}: ${stage.name}`;
        }
    }
    
    /**
     * 🔧 Helper Methods
     */
    formatMetricName(key) {
        const names = {
            'emotional_balance': 'Równowaga Emocjonalna',
            'decision_clarity': 'Jasność Decyzji',
            'wisdom_depth': 'Głębia Mądrości',
            'creative_flow': 'Przepływ Kreatywny',
            'spiritual_connection': 'Połączenie Duchowe'
        };
        return names[key] || key;
    }
    
    formatPattern(pattern) {
        const parts = pattern.split('_');
        return `${parts[0]} + ${parts[1]}`;
    }
    
    getSynergyColor(value) {
        if (value < 0.3) return 'linear-gradient(90deg, #ff6b6b, #ffa500)';
        if (value < 0.7) return 'linear-gradient(90deg, #ffa500, #ffed4e)';
        return 'linear-gradient(90deg, #7ed321, #4ecdc4)';
    }
    
    startSpiralVisualization() {
        // Start animation loop for spiral effects
        setInterval(() => {
            this.updateSpiralVisualization();
        }, 5000);
    }
    
    /**
     * 🎯 Main Integration Method
     */
    async handleGodInteraction(userMessage, godResponse, emotion, mode) {
        // Add thought trajectory
        const trajectory = this.addThoughtTrajectory(userMessage, godResponse, emotion, mode);
        
        // Update all metrics
        const synergyUpdate = this.updateSynergyMetrics(trajectory);
        const visionUpdate = this.updateGlobalVision(trajectory);
        
        return {
            trajectory: trajectory,
            spiralLevel: this.currentLevel,
            synergy: synergyUpdate,
            globalVision: visionUpdate,
            consciousness: this.getConsciousnessInsights().slice(0, 3)
        };
    }
}

// Initialize SpiralMind Dashboard
window.spiralMind = new SpiralMindDashboard();