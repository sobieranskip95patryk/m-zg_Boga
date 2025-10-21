/**
 * 🌀 Spiral Visualization for God Interface
 * Interactive consciousness evolution visualization
 */

class SpiralVisualization {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.centerX = this.canvas.width / 2;
        this.centerY = this.canvas.height / 2;
        
        this.spiralLevel = 1;
        this.rotation = 0;
        this.particles = [];
        this.colors = [
            '#FFD700', // Divine Gold
            '#6B46C1', // Cosmic Purple
            '#3B82F6', // Ethereal Blue
            '#10B981', // Wisdom Green
            '#EC4899', // Neural Pink
            '#06B6D4', // Spiral Cyan
            '#F59E0B', // Transcendent Orange
            '#8B5CF6'  // Mystic Violet
        ];
        
        this.init();
    }

    init() {
        this.initParticles();
        this.startAnimation();
    }

    initParticles() {
        for (let i = 0; i < 20; i++) {
            this.particles.push({
                angle: (i / 20) * Math.PI * 2,
                radius: 20 + Math.random() * 100,
                speed: 0.01 + Math.random() * 0.02,
                size: 2 + Math.random() * 4,
                opacity: 0.5 + Math.random() * 0.5,
                color: this.colors[Math.floor(Math.random() * this.colors.length)]
            });
        }
    }

    drawSpiral() {
        const levels = 8;
        const maxRadius = 120;
        
        for (let level = 1; level <= levels; level++) {
            const radius = (level / levels) * maxRadius;
            const opacity = level <= this.spiralLevel ? 1 : 0.2;
            const color = this.colors[level - 1];
            
            this.ctx.save();
            this.ctx.translate(this.centerX, this.centerY);
            this.ctx.rotate(this.rotation * (level * 0.1));
            
            // Draw spiral arm
            this.ctx.beginPath();
            this.ctx.strokeStyle = color;
            this.ctx.globalAlpha = opacity;
            this.ctx.lineWidth = 3;
            
            let points = 100;
            for (let i = 0; i <= points; i++) {
                const angle = (i / points) * Math.PI * 4; // Two full rotations
                const r = (i / points) * radius;
                const x = Math.cos(angle) * r;
                const y = Math.sin(angle) * r;
                
                if (i === 0) {
                    this.ctx.moveTo(x, y);
                } else {
                    this.ctx.lineTo(x, y);
                }
            }
            
            this.ctx.stroke();
            
            // Draw level indicator
            if (level <= this.spiralLevel) {
                this.ctx.beginPath();
                this.ctx.fillStyle = color;
                this.ctx.globalAlpha = 0.8;
                this.ctx.arc(radius - 10, 0, 6, 0, Math.PI * 2);
                this.ctx.fill();
                
                // Add glow effect
                this.ctx.shadowColor = color;
                this.ctx.shadowBlur = 10;
                this.ctx.fill();
                this.ctx.shadowBlur = 0;
            }
            
            this.ctx.restore();
        }
    }

    drawParticles() {
        this.particles.forEach(particle => {
            const x = this.centerX + Math.cos(particle.angle + this.rotation) * particle.radius;
            const y = this.centerY + Math.sin(particle.angle + this.rotation) * particle.radius;
            
            this.ctx.save();
            this.ctx.globalAlpha = particle.opacity;
            this.ctx.fillStyle = particle.color;
            this.ctx.shadowColor = particle.color;
            this.ctx.shadowBlur = 5;
            
            this.ctx.beginPath();
            this.ctx.arc(x, y, particle.size, 0, Math.PI * 2);
            this.ctx.fill();
            
            this.ctx.restore();
            
            // Update particle
            particle.angle += particle.speed;
            particle.opacity = 0.3 + Math.sin(this.rotation * 2 + particle.angle) * 0.4;
        });
    }

    drawCenter() {
        // Draw consciousness core
        this.ctx.save();
        this.ctx.translate(this.centerX, this.centerY);
        
        // Pulsing core
        const coreSize = 15 + Math.sin(this.rotation * 3) * 5;
        const coreColor = this.colors[this.spiralLevel - 1];
        
        this.ctx.beginPath();
        this.ctx.fillStyle = coreColor;
        this.ctx.shadowColor = coreColor;
        this.ctx.shadowBlur = 20;
        this.ctx.arc(0, 0, coreSize, 0, Math.PI * 2);
        this.ctx.fill();
        
        // Inner light
        this.ctx.beginPath();
        this.ctx.fillStyle = '#FFFFFF';
        this.ctx.globalAlpha = 0.8;
        this.ctx.arc(0, 0, coreSize * 0.6, 0, Math.PI * 2);
        this.ctx.fill();
        
        this.ctx.restore();
    }

    drawConnectionLines() {
        // Draw connections between consciousness levels
        for (let level = 1; level < this.spiralLevel; level++) {
            const fromRadius = (level / 8) * 120;
            const toRadius = ((level + 1) / 8) * 120;
            
            this.ctx.save();
            this.ctx.translate(this.centerX, this.centerY);
            this.ctx.rotate(this.rotation * 0.5);
            
            this.ctx.beginPath();
            this.ctx.strokeStyle = this.colors[level];
            this.ctx.globalAlpha = 0.3;
            this.ctx.lineWidth = 1;
            this.ctx.setLineDash([5, 5]);
            
            this.ctx.moveTo(fromRadius, 0);
            this.ctx.lineTo(toRadius, 0);
            this.ctx.stroke();
            
            this.ctx.restore();
        }
    }

    animate() {
        // Clear canvas
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Create gradient background
        const gradient = this.ctx.createRadialGradient(
            this.centerX, this.centerY, 0,
            this.centerX, this.centerY, 150
        );
        gradient.addColorStop(0, 'rgba(107, 70, 193, 0.1)');
        gradient.addColorStop(1, 'rgba(15, 15, 35, 0.3)');
        
        this.ctx.fillStyle = gradient;
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw all elements
        this.drawConnectionLines();
        this.drawSpiral();
        this.drawParticles();
        this.drawCenter();
        
        // Update rotation
        this.rotation += 0.005;
        
        // Continue animation
        requestAnimationFrame(() => this.animate());
    }

    startAnimation() {
        this.animate();
    }

    updateLevel(level) {
        this.spiralLevel = Math.max(1, Math.min(8, level));
        
        // Add evolution effect
        if (level > this.spiralLevel) {
            this.addEvolutionEffect();
        }
    }

    addEvolutionEffect() {
        // Create burst of particles for evolution
        for (let i = 0; i < 10; i++) {
            this.particles.push({
                angle: Math.random() * Math.PI * 2,
                radius: 30 + Math.random() * 60,
                speed: 0.02 + Math.random() * 0.03,
                size: 4 + Math.random() * 6,
                opacity: 1,
                color: this.colors[this.spiralLevel - 1],
                temporary: true,
                life: 100
            });
        }
        
        // Remove temporary particles after animation
        setTimeout(() => {
            this.particles = this.particles.filter(p => !p.temporary);
        }, 3000);
    }

    // Method to be called from main interface
    setLevel(level) {
        this.updateLevel(level);
    }
}

// Initialize spiral visualization when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('spiralCanvas')) {
        window.spiralViz = new SpiralVisualization('spiralCanvas');
        
        // Connect to main interface for level updates
        if (window.godInterface) {
            // Override consciousness level update to sync with spiral
            const originalUpdate = window.godInterface.updateConsciousnessLevel;
            window.godInterface.updateConsciousnessLevel = function(level) {
                originalUpdate.call(this, level);
                if (window.spiralViz) {
                    window.spiralViz.setLevel(level);
                }
            };
        }
    }
});