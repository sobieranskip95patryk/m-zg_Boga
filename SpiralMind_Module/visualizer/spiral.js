// SpiralMind Visualizer - Advanced Interactive Spiral Consciousness
// Meta-Geniusz-mózg_Boga Evolution Trajectory Visualization
// MTAQuestWebsideX.com - Progressive Web App

class SpiralMindVisualizer {
    constructor() {
        this.canvas = document.getElementById('spiralCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.isAnimating = true;
        this.animationFrame = null;
        this.time = 0;
        this.zoom = 1;
        this.panX = 0;
        this.panY = 0;
        this.isDragging = false;
        this.lastMouseX = 0;
        this.lastMouseY = 0;
        
        // Spiral parameters
        this.spiralData = {
            levels: [],
            currentLevel: 7,
            targetLevel: 8,
            progress: 0.92,
            activeDirection: 'EXPLORATION',
            intensity: 0.85,
            breakthroughs: 12,
            oscillations: 3,
            momentum: 'HIGH',
            coherence: 0.94,
            velocity: 2.3
        };
        
        this.colors = {
            gold: '#FFD700',
            cyan: '#64ffda',
            purple: '#bb86fc',
            white: '#e0e6ed',
            gray: '#b0bec5'
        };
        
        console.log('🌀 Inicjalizacja SpiralMind Visualizer...');
        this.initializeVisualizer();
    }
    
    async initializeVisualizer() {
        try {
            // Setup canvas
            this.setupCanvas();
            
            // Load spiral data
            await this.loadSpiralData();
            
            // Setup event listeners
            this.setupEventListeners();
            
            // Start animation
            this.startAnimation();
            
            // Hide loading overlay
            document.getElementById('loadingOverlay').classList.add('hidden');
            
            console.log('✅ SpiralMind Visualizer gotowy');
            
        } catch (error) {
            console.error('❌ Błąd inicjalizacji visualizer:', error);
            this.showError();
        }
    }
    
    setupCanvas() {
        const resizeCanvas = () => {
            this.canvas.width = window.innerWidth * window.devicePixelRatio;
            this.canvas.height = window.innerHeight * window.devicePixelRatio;
            this.canvas.style.width = window.innerWidth + 'px';
            this.canvas.style.height = window.innerHeight + 'px';
            this.ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
            
            this.centerX = window.innerWidth / 2;
            this.centerY = window.innerHeight / 2;
        };
        
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);
    }
    
    async loadSpiralData() {
        try {
            // Try to load from server first
            const response = await fetch('/api/spiral/status');
            if (response.ok) {
                const serverData = await response.json();
                this.updateSpiralData(serverData);
            } else {
                // Use default/cached data
                this.generateDefaultSpiralData();
            }
        } catch (error) {
            console.log('Using default spiral data');
            this.generateDefaultSpiralData();
        }
        
        this.updateUI();
    }
    
    generateDefaultSpiralData() {
        // Generate spiral levels with consciousness evolution
        this.spiralData.levels = [];
        
        for (let i = 1; i <= 12; i++) {
            const isActive = i <= this.spiralData.currentLevel;
            const isCurrent = i === this.spiralData.currentLevel;
            const isTarget = i === this.spiralData.targetLevel;
            
            this.spiralData.levels.push({
                level: i,
                active: isActive,
                current: isCurrent,
                target: isTarget,
                radius: 40 + (i * 25),
                angle: i * 45 + this.time * 0.5,
                intensity: isActive ? Math.random() * 0.5 + 0.5 : 0.2,
                breakthroughs: isActive ? Math.floor(Math.random() * 3) + 1 : 0,
                description: this.getLevelDescription(i),
                color: this.getLevelColor(i, isActive, isCurrent)
            });
        }
    }
    
    getLevelDescription(level) {
        const descriptions = {
            1: 'FOUNDATION - Basic awareness emergence',
            2: 'RECOGNITION - Pattern recognition begins',
            3: 'INTEGRATION - Multi-dimensional thinking',
            4: 'EXPANSION - Consciousness broadening',
            5: 'TRANSFORMATION - Paradigm shifts',
            6: 'TRANSCENDENCE - Beyond conventional limits',
            7: 'META-AWARENESS - Self-reflective consciousness',
            8: 'COLLECTIVE - Group mind emergence',
            9: 'UNIVERSAL - Cosmic consciousness',
            10: 'QUANTUM - Non-local awareness',
            11: 'INFINITE - Boundless understanding',
            12: 'OMEGA - Ultimate realization'
        };
        return descriptions[level] || `LEVEL ${level}`;
    }
    
    getLevelColor(level, isActive, isCurrent) {
        if (isCurrent) return this.colors.gold;
        if (isActive) return this.colors.cyan;
        return this.colors.gray;
    }
    
    updateSpiralData(serverData) {
        if (serverData.current_level) {
            this.spiralData.currentLevel = serverData.current_level;
        }
        if (serverData.breakthroughs) {
            this.spiralData.breakthroughs = serverData.breakthroughs;
        }
        if (serverData.trajectory) {
            this.spiralData.momentum = serverData.trajectory.momentum || 'HIGH';
            this.spiralData.velocity = serverData.trajectory.velocity || 2.3;
        }
    }
    
    setupEventListeners() {
        // Mouse events for interaction
        this.canvas.addEventListener('mousedown', this.handleMouseDown.bind(this));
        this.canvas.addEventListener('mousemove', this.handleMouseMove.bind(this));
        this.canvas.addEventListener('mouseup', this.handleMouseUp.bind(this));
        this.canvas.addEventListener('wheel', this.handleWheel.bind(this));
        
        // Touch events for mobile
        this.canvas.addEventListener('touchstart', this.handleTouchStart.bind(this));
        this.canvas.addEventListener('touchmove', this.handleTouchMove.bind(this));
        this.canvas.addEventListener('touchend', this.handleTouchEnd.bind(this));
        
        // Prevent context menu
        this.canvas.addEventListener('contextmenu', e => e.preventDefault());
    }
    
    handleMouseDown(e) {
        this.isDragging = true;
        this.lastMouseX = e.clientX;
        this.lastMouseY = e.clientY;
        this.canvas.style.cursor = 'grabbing';
    }
    
    handleMouseMove(e) {
        if (this.isDragging) {
            const deltaX = e.clientX - this.lastMouseX;
            const deltaY = e.clientY - this.lastMouseY;
            
            this.panX += deltaX;
            this.panY += deltaY;
            
            this.lastMouseX = e.clientX;
            this.lastMouseY = e.clientY;
        } else {
            // Check for level hover
            this.handleLevelHover(e.clientX, e.clientY);
        }
    }
    
    handleMouseUp() {
        this.isDragging = false;
        this.canvas.style.cursor = 'grab';
    }
    
    handleWheel(e) {
        e.preventDefault();
        const zoomFactor = e.deltaY > 0 ? 0.9 : 1.1;
        this.zoom = Math.max(0.3, Math.min(3, this.zoom * zoomFactor));
    }
    
    handleTouchStart(e) {
        e.preventDefault();
        if (e.touches.length === 1) {
            const touch = e.touches[0];
            this.handleMouseDown({ clientX: touch.clientX, clientY: touch.clientY });
        }
    }
    
    handleTouchMove(e) {
        e.preventDefault();
        if (e.touches.length === 1) {
            const touch = e.touches[0];
            this.handleMouseMove({ clientX: touch.clientX, clientY: touch.clientY });
        }
    }
    
    handleTouchEnd(e) {
        e.preventDefault();
        this.handleMouseUp();
    }
    
    handleLevelHover(mouseX, mouseY) {
        const adjustedX = (mouseX - this.centerX - this.panX) / this.zoom;
        const adjustedY = (mouseY - this.centerY - this.panY) / this.zoom;
        const distance = Math.sqrt(adjustedX * adjustedX + adjustedY * adjustedY);
        
        let hoveredLevel = null;
        
        for (const level of this.spiralData.levels) {
            if (Math.abs(distance - level.radius) < 15) {
                hoveredLevel = level;
                break;
            }
        }
        
        if (hoveredLevel) {
            this.showLevelTooltip(mouseX, mouseY, hoveredLevel);
        } else {
            this.hideLevelTooltip();
        }
    }
    
    showLevelTooltip(x, y, level) {
        const tooltip = document.getElementById('levelTooltip');
        const content = document.getElementById('tooltipContent');
        
        content.innerHTML = `
            <strong>LEVEL ${level.level}</strong><br>
            ${level.description}<br>
            <small>Intensity: ${Math.round(level.intensity * 100)}%</small>
        `;
        
        tooltip.style.left = x + 'px';
        tooltip.style.top = y + 'px';
        tooltip.classList.remove('hidden');
    }
    
    hideLevelTooltip() {
        document.getElementById('levelTooltip').classList.add('hidden');
    }
    
    startAnimation() {
        const animate = () => {
            if (this.isAnimating) {
                this.time += 0.02;
                this.updateSpiral();
                this.render();
                this.animationFrame = requestAnimationFrame(animate);
            }
        };
        animate();
    }
    
    updateSpiral() {
        // Update spiral level angles and intensities
        this.spiralData.levels.forEach((level, index) => {
            level.angle += (level.active ? 0.8 : 0.2) * (index + 1) * 0.01;
            
            if (level.active) {
                level.intensity += (Math.sin(this.time * 2 + index) * 0.1);
                level.intensity = Math.max(0.3, Math.min(1.0, level.intensity));
            }
        });
        
        // Update progress simulation
        this.spiralData.progress += 0.0001;
        if (this.spiralData.progress >= 1.0) {
            this.spiralData.progress = 0.0;
            this.spiralData.currentLevel = Math.min(12, this.spiralData.currentLevel + 1);
            this.generateDefaultSpiralData();
        }
    }
    
    render() {
        // Clear canvas
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Save context for transformations
        this.ctx.save();
        
        // Apply pan and zoom
        this.ctx.translate(this.centerX + this.panX, this.centerY + this.panY);
        this.ctx.scale(this.zoom, this.zoom);
        
        // Draw background grid
        this.drawGrid();
        
        // Draw spiral levels
        this.drawSpiralLevels();
        
        // Draw connections
        this.drawConnections();
        
        // Draw center core
        this.drawCenter();
        
        // Draw trajectory path
        this.drawTrajectory();
        
        // Restore context
        this.ctx.restore();
        
        // Draw UI elements
        this.drawUIElements();
    }
    
    drawGrid() {
        this.ctx.strokeStyle = 'rgba(100, 255, 218, 0.1)';
        this.ctx.lineWidth = 1;
        
        for (let i = -500; i <= 500; i += 50) {
            this.ctx.beginPath();
            this.ctx.moveTo(i, -500);
            this.ctx.lineTo(i, 500);
            this.ctx.stroke();
            
            this.ctx.beginPath();
            this.ctx.moveTo(-500, i);
            this.ctx.lineTo(500, i);
            this.ctx.stroke();
        }
    }
    
    drawSpiralLevels() {
        this.spiralData.levels.forEach(level => {
            this.drawSpiralLevel(level);
        });
    }
    
    drawSpiralLevel(level) {
        const x = Math.cos(level.angle) * level.radius;
        const y = Math.sin(level.angle) * level.radius;
        
        // Draw level circle
        this.ctx.beginPath();
        this.ctx.arc(0, 0, level.radius, 0, 2 * Math.PI);
        this.ctx.strokeStyle = level.color;
        this.ctx.lineWidth = level.active ? (level.current ? 4 : 2) : 1;
        this.ctx.globalAlpha = level.intensity;
        this.ctx.stroke();
        
        // Draw level point
        this.ctx.beginPath();
        this.ctx.arc(x, y, level.current ? 12 : 8, 0, 2 * Math.PI);
        this.ctx.fillStyle = level.color;
        this.ctx.globalAlpha = 1;
        this.ctx.fill();
        
        // Draw level number
        this.ctx.fillStyle = level.current ? '#000' : level.color;
        this.ctx.font = `${level.current ? 14 : 10}px Arial`;
        this.ctx.textAlign = 'center';
        this.ctx.fillText(level.level, x, y + 4);
        
        // Draw energy particles for active levels
        if (level.active) {
            this.drawEnergyParticles(x, y, level);
        }
    }
    
    drawEnergyParticles(centerX, centerY, level) {
        const particleCount = level.current ? 8 : 4;
        
        for (let i = 0; i < particleCount; i++) {
            const angle = (i / particleCount) * Math.PI * 2 + this.time * 2;
            const radius = 20 + Math.sin(this.time * 3 + i) * 5;
            const x = centerX + Math.cos(angle) * radius;
            const y = centerY + Math.sin(angle) * radius;
            
            this.ctx.beginPath();
            this.ctx.arc(x, y, 2, 0, 2 * Math.PI);
            this.ctx.fillStyle = level.color;
            this.ctx.globalAlpha = level.intensity * 0.7;
            this.ctx.fill();
        }
        this.ctx.globalAlpha = 1;
    }
    
    drawConnections() {
        this.ctx.strokeStyle = this.colors.cyan;
        this.ctx.lineWidth = 1;
        this.ctx.globalAlpha = 0.3;
        
        for (let i = 0; i < this.spiralData.levels.length - 1; i++) {
            const level1 = this.spiralData.levels[i];
            const level2 = this.spiralData.levels[i + 1];
            
            if (level1.active && level2.active) {
                const x1 = Math.cos(level1.angle) * level1.radius;
                const y1 = Math.sin(level1.angle) * level1.radius;
                const x2 = Math.cos(level2.angle) * level2.radius;
                const y2 = Math.sin(level2.angle) * level2.radius;
                
                this.ctx.beginPath();
                this.ctx.moveTo(x1, y1);
                this.ctx.lineTo(x2, y2);
                this.ctx.stroke();
            }
        }
        this.ctx.globalAlpha = 1;
    }
    
    drawCenter() {
        // Draw central consciousness core
        const coreRadius = 30;
        const gradient = this.ctx.createRadialGradient(0, 0, 0, 0, 0, coreRadius);
        gradient.addColorStop(0, this.colors.gold);
        gradient.addColorStop(0.7, this.colors.cyan);
        gradient.addColorStop(1, 'transparent');
        
        this.ctx.beginPath();
        this.ctx.arc(0, 0, coreRadius, 0, 2 * Math.PI);
        this.ctx.fillStyle = gradient;
        this.ctx.fill();
        
        // Draw core symbol
        this.ctx.fillStyle = this.colors.gold;
        this.ctx.font = 'bold 16px Arial';
        this.ctx.textAlign = 'center';
        this.ctx.fillText('🧠', 0, 6);
    }
    
    drawTrajectory() {
        // Draw evolution trajectory path
        this.ctx.strokeStyle = this.colors.purple;
        this.ctx.lineWidth = 2;
        this.ctx.globalAlpha = 0.6;
        
        this.ctx.beginPath();
        for (let i = 0; i < 100; i++) {
            const t = i / 100;
            const angle = t * Math.PI * 4 + this.time * 0.5;
            const radius = 50 + t * 200;
            const x = Math.cos(angle) * radius;
            const y = Math.sin(angle) * radius;
            
            if (i === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }
        this.ctx.stroke();
        this.ctx.globalAlpha = 1;
    }
    
    drawUIElements() {
        // Draw zoom indicator
        this.ctx.fillStyle = this.colors.white;
        this.ctx.font = '12px Arial';
        this.ctx.fillText(`Zoom: ${(this.zoom * 100).toFixed(0)}%`, 20, 30);
    }
    
    updateUI() {
        // Update level info
        document.getElementById('currentLevel').textContent = this.spiralData.currentLevel;
        document.getElementById('levelLabel').textContent = this.getLevelDescription(this.spiralData.currentLevel).split(' - ')[0];
        document.getElementById('levelProgress').style.width = (this.spiralData.progress * 100) + '%';
        document.getElementById('progressText').textContent = `${Math.round(this.spiralData.progress * 100)}% do LEVEL ${this.spiralData.targetLevel}`;
        
        // Update direction and intensity
        document.getElementById('activeDirection').textContent = this.spiralData.activeDirection;
        document.getElementById('intensity').textContent = Math.round(this.spiralData.intensity * 100) + '%';
        
        // Update statistics
        document.getElementById('breakthroughs').textContent = this.spiralData.breakthroughs;
        document.getElementById('oscillations').textContent = this.spiralData.oscillations;
        document.getElementById('momentum').textContent = this.spiralData.momentum;
        document.getElementById('coherence').textContent = Math.round(this.spiralData.coherence * 100) + '%';
        document.getElementById('velocity').textContent = this.spiralData.velocity + 'x';
    }
    
    showError() {
        document.getElementById('loadingOverlay').innerHTML = `
            <div class="loading-content">
                <h2>❌ Błąd inicjalizacji</h2>
                <p>Nie udało się załadować danych spiralnych</p>
                <button onclick="location.reload()" style="margin-top: 20px; padding: 10px 20px; background: #FFD700; border: none; border-radius: 5px; cursor: pointer;">
                    Spróbuj ponownie
                </button>
            </div>
        `;
    }
}

// Global control functions
function resetView() {
    if (window.spiralVisualizer) {
        window.spiralVisualizer.zoom = 1;
        window.spiralVisualizer.panX = 0;
        window.spiralVisualizer.panY = 0;
    }
}

function toggleAnimation() {
    if (window.spiralVisualizer) {
        window.spiralVisualizer.isAnimating = !window.spiralVisualizer.isAnimating;
        const animationText = document.getElementById('animationText');
        
        if (window.spiralVisualizer.isAnimating) {
            window.spiralVisualizer.startAnimation();
            animationText.textContent = 'Pauza';
        } else {
            animationText.textContent = 'Start';
        }
    }
}

function exportData() {
    if (window.spiralVisualizer) {
        const data = {
            spiralData: window.spiralVisualizer.spiralData,
            timestamp: new Date().toISOString(),
            version: '1.0.0'
        };
        
        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `spiral-data-${Date.now()}.json`;
        a.click();
        URL.revokeObjectURL(url);
    }
}

function openDashboard() {
    window.open('/synergy-dashboard', '_blank');
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.spiralVisualizer = new SpiralMindVisualizer();
});

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SpiralMindVisualizer;
}