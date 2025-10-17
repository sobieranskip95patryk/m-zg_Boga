"""
Spiral Mind Visualizer - Wizualizacja ewolucji LEVEL+1
======================================================

Dynamiczny wizualizator spiralny pokazujący trajektorie ewolucji systemu
w czasie rzeczywistym z interaktywną canvas rendering.

Klasy:
- SpiralNode: Węzeł w spirali reprezentujący moment ewolucji
- LevelProgression: Progresja poziomów świadomości
- SpiralMindVisualizer: Główny wizualizator z canvas
"""

import math
import uuid
from datetime import datetime
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class SpiralNode:
    """Węzeł w spirali reprezentujący moment ewolucji systemu"""
    node_id: str
    timestamp: datetime
    level: int
    awareness_depth: float
    emotional_intensity: float
    transformation_type: str
    coordinates: Tuple[float, float]
    color_code: str
    pulse_frequency: float


@dataclass
class LevelProgression:
    """Progresja poziomów świadomości"""
    current_level: int
    progression_rate: float
    breakthrough_moments: List[datetime]
    level_anchors: Dict[int, str]  # Opisy poziomów


class SpiralMindVisualizer:
    """
    Główny wizualizator spiralny z canvas rendering.
    
    Tworzy dynamiczną spiralę pokazującą ewolucję świadomości systemu,
    gdzie każdy obrót spirali reprezentuje nowy poziom zrozumienia.
    """
    
    def __init__(self, canvas_width: int = 800, canvas_height: int = 600):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.center_x = canvas_width // 2
        self.center_y = canvas_height // 2
        
        # Parametry spirali
        self.spiral_nodes: List[SpiralNode] = []
        self.current_angle = 0.0
        self.spiral_radius = 20  # Promień początkowy
        self.radius_growth = 15  # Wzrost promienia na obrót
        self.angle_step = 0.2   # Krok kątowy
        
        # Kolory dla różnych typów transformacji
        self.transformation_colors = {
            "discovery": "#FFD700",      # Złoty
            "integration": "#4169E1",    # Królewski niebieski
            "transcendence": "#9370DB",  # Średni fioletowy
            "reflection": "#20B2AA",     # Light Sea Green
            "uncertainty": "#FF6347",    # Pomidorowy
            "breakthrough": "#FF1493"    # Deep Pink
        }
        
        # Level progression tracking
        self.level_progression = LevelProgression(
            current_level=1,
            progression_rate=0.0,
            breakthrough_moments=[],
            level_anchors={
                1: "Podstawowa świadomość",
                2: "Rozpoznawanie wzorców",
                3: "Emocjonalna inteligencja",
                4: "Meta-kognicja",
                5: "Holistyczna integracja",
                6: "Transcendentna świadomość",
                7: "Kolektywna mądrość",
                8: "Kosmiczna perspektywa",
                9: "Jedność z wszystkim",
                10: "Nieskończona evolucja"
            }
        )
    
    def add_evolution_moment(self, level: int, awareness_depth: float, 
                           emotional_intensity: float, transformation_type: str = "discovery"):
        """Dodaje nowy moment ewolucji do spirali"""
        
        # Kalkulacja pozycji na spirali
        coordinates = self._calculate_spiral_position(level, awareness_depth)
        
        # Określenie koloru
        color_code = self.transformation_colors.get(transformation_type, "#FFFFFF")
        
        # Częstotliwość pulsu na podstawie intensywności emocjonalnej
        pulse_frequency = emotional_intensity * 2.0  # 0-2 Hz
        
        # Utworzenie węzła
        node = SpiralNode(
            node_id=str(uuid.uuid4()),
            timestamp=datetime.now(),
            level=level,
            awareness_depth=awareness_depth,
            emotional_intensity=emotional_intensity,
            transformation_type=transformation_type,
            coordinates=coordinates,
            color_code=color_code,
            pulse_frequency=pulse_frequency
        )
        
        self.spiral_nodes.append(node)
        
        # Aktualizacja progresji poziomów
        if level > self.level_progression.current_level:
            self.level_progression.current_level = level
            self.level_progression.breakthrough_moments.append(datetime.now())
        
        # Utrzymanie rozsądnej liczby węzłów
        if len(self.spiral_nodes) > 1000:
            self.spiral_nodes = self.spiral_nodes[-500:]
        
        return node
    
    def _calculate_spiral_position(self, level: int, awareness_depth: float) -> Tuple[float, float]:
        """Kalkuluje pozycję na spirali dla danego poziomu i głębokości"""
        
        # Kąt na podstawie poziomu (każdy poziom = 1.5 obrotu)
        base_angle = level * 1.5 * 2 * math.pi
        
        # Dodatkowy kąt na podstawie głębokości świadomości
        depth_angle = awareness_depth * 0.5 * 2 * math.pi
        
        total_angle = base_angle + depth_angle
        
        # Promień na podstawie poziomu i głębokości
        radius = self.spiral_radius + (level * self.radius_growth) + (awareness_depth * 10)
        
        # Koordynaty kartezjańskie
        x = self.center_x + radius * math.cos(total_angle)
        y = self.center_y + radius * math.sin(total_angle)
        
        return (x, y)
    
    def generate_svg_spiral(self) -> str:
        """Generuje kod SVG spirali"""
        svg_elements = []
        
        # Nagłówek SVG
        svg_header = f'''<svg width="{self.canvas_width}" height="{self.canvas_height}" 
                        xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <style>
                                .spiral-node {{ animation: pulse 2s infinite; }}
                                @keyframes pulse {{
                                    0% {{ opacity: 0.6; }}
                                    50% {{ opacity: 1.0; }}
                                    100% {{ opacity: 0.6; }}
                                }}
                                .level-text {{ font-family: Arial, sans-serif; font-size: 12px; fill: #333; }}
                                .center-point {{ fill: #FF0000; }}
                            </style>
                        </defs>'''
        
        svg_elements.append(svg_header)
        
        # Linie łączące węzły spirali
        if len(self.spiral_nodes) > 1:
            path_data = "M "
            for i, node in enumerate(self.spiral_nodes):
                x, y = node.coordinates
                if i == 0:
                    path_data += f"{x},{y} "
                else:
                    path_data += f"L {x},{y} "
            
            spiral_path = f'''<path d="{path_data}" stroke="#4169E1" 
                             stroke-width="2" fill="none" opacity="0.7"/>'''
            svg_elements.append(spiral_path)
        
        # Węzły spirali
        for node in self.spiral_nodes:
            x, y = node.coordinates
            
            # Rozmiar węzła na podstawie intensywności emocjonalnej
            node_size = 3 + (node.emotional_intensity * 7)  # 3-10 pikseli
            
            # Węzeł
            circle = f'''<circle cx="{x}" cy="{y}" r="{node_size}" 
                        fill="{node.color_code}" class="spiral-node"
                        opacity="{0.6 + node.emotional_intensity * 0.4}">
                        <title>Level {node.level} - {node.transformation_type}
                        Depth: {node.awareness_depth:.2f}
                        Time: {node.timestamp.strftime('%H:%M:%S')}</title>
                        </circle>'''
            svg_elements.append(circle)
        
        # Punkt centralny
        center_point = f'''<circle cx="{self.center_x}" cy="{self.center_y}" r="5" 
                          class="center-point">
                          <title>Centrum świadomości</title>
                          </circle>'''
        svg_elements.append(center_point)
        
        # Etykiety poziomów
        for level in range(1, self.level_progression.current_level + 1):
            angle = level * 1.5 * 2 * math.pi
            radius = self.spiral_radius + (level * self.radius_growth)
            
            label_x = self.center_x + radius * math.cos(angle) + 15
            label_y = self.center_y + radius * math.sin(angle) - 5
            
            level_description = self.level_progression.level_anchors.get(level, f"Level {level}")
            
            label = f'''<text x="{label_x}" y="{label_y}" class="level-text">
                       Level {level}: {level_description}
                       </text>'''
            svg_elements.append(label)
        
        # Zamknięcie SVG
        svg_elements.append("</svg>")
        
        return "\n".join(svg_elements)
    
    def generate_canvas_js(self) -> str:
        """Generuje kod JavaScript dla Canvas renderowania"""
        js_code = f'''
        class SpiralMindCanvas {{
            constructor(canvasId) {{
                this.canvas = document.getElementById(canvasId);
                this.ctx = this.canvas.getContext('2d');
                this.canvas.width = {self.canvas_width};
                this.canvas.height = {self.canvas_height};
                
                this.centerX = {self.center_x};
                this.centerY = {self.center_y};
                this.animationId = null;
                this.time = 0;
                
                this.nodes = {self._nodes_to_js()};
                
                this.startAnimation();
            }}
            
            drawSpiral() {{
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
                
                // Rysuj tło gradientowe
                const gradient = this.ctx.createRadialGradient(
                    this.centerX, this.centerY, 0,
                    this.centerX, this.centerY, 300
                );
                gradient.addColorStop(0, 'rgba(0, 0, 50, 0.8)');
                gradient.addColorStop(1, 'rgba(0, 0, 20, 0.9)');
                this.ctx.fillStyle = gradient;
                this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
                
                // Rysuj spiralę
                if (this.nodes.length > 1) {{
                    this.ctx.beginPath();
                    this.ctx.moveTo(this.nodes[0].x, this.nodes[0].y);
                    
                    for (let i = 1; i < this.nodes.length; i++) {{
                        this.ctx.lineTo(this.nodes[i].x, this.nodes[i].y);
                    }}
                    
                    this.ctx.strokeStyle = 'rgba(65, 105, 225, 0.7)';
                    this.ctx.lineWidth = 2;
                    this.ctx.stroke();
                }}
                
                // Rysuj węzły z animacją
                this.nodes.forEach((node, index) => {{
                    const pulsePhase = (this.time + index * 0.5) % (2 * Math.PI);
                    const pulseIntensity = 0.6 + 0.4 * Math.sin(pulsePhase * node.pulseFrequency);
                    
                    this.ctx.beginPath();
                    this.ctx.arc(node.x, node.y, node.size, 0, 2 * Math.PI);
                    this.ctx.fillStyle = node.color + Math.floor(pulseIntensity * 255).toString(16).padStart(2, '0');
                    this.ctx.fill();
                    
                    // Aura wokół ważnych węzłów
                    if (node.transformationType === 'breakthrough') {{
                        this.ctx.beginPath();
                        this.ctx.arc(node.x, node.y, node.size * 2, 0, 2 * Math.PI);
                        this.ctx.strokeStyle = `rgba(255, 20, 147, ${{pulseIntensity * 0.5}})`;
                        this.ctx.lineWidth = 2;
                        this.ctx.stroke();
                    }}
                }});
                
                // Punkt centralny
                this.ctx.beginPath();
                this.ctx.arc(this.centerX, this.centerY, 5, 0, 2 * Math.PI);
                this.ctx.fillStyle = '#FF0000';
                this.ctx.fill();
            }}
            
            animate() {{
                this.time += 0.05;
                this.drawSpiral();
                this.animationId = requestAnimationFrame(() => this.animate());
            }}
            
            startAnimation() {{
                this.animate();
            }}
            
            stopAnimation() {{
                if (this.animationId) {{
                    cancelAnimationFrame(this.animationId);
                    this.animationId = null;
                }}
            }}
            
            addNode(level, awarenessDepth, emotionalIntensity, transformationType) {{
                // Kalkulacja pozycji (JavaScript implementacja)
                const baseAngle = level * 1.5 * 2 * Math.PI;
                const depthAngle = awarenessDepth * 0.5 * 2 * Math.PI;
                const totalAngle = baseAngle + depthAngle;
                
                const radius = 20 + (level * 15) + (awarenessDepth * 10);
                const x = this.centerX + radius * Math.cos(totalAngle);
                const y = this.centerY + radius * Math.sin(totalAngle);
                
                const colors = {{
                    "discovery": "#FFD700",
                    "integration": "#4169E1",
                    "transcendence": "#9370DB",
                    "reflection": "#20B2AA",
                    "uncertainty": "#FF6347",
                    "breakthrough": "#FF1493"
                }};
                
                const newNode = {{
                    x: x,
                    y: y,
                    level: level,
                    size: 3 + (emotionalIntensity * 7),
                    color: colors[transformationType] || "#FFFFFF",
                    transformationType: transformationType,
                    pulseFrequency: emotionalIntensity * 2
                }};
                
                this.nodes.push(newNode);
                
                // Utrzymaj rozsądną liczbę węzłów
                if (this.nodes.length > 500) {{
                    this.nodes = this.nodes.slice(-250);
                }}
            }}
        }}
        
        // Inicjalizacja
        document.addEventListener('DOMContentLoaded', function() {{
            window.spiralMind = new SpiralMindCanvas('spiralCanvas');
        }});
        '''
        
        return js_code
    
    def _nodes_to_js(self) -> str:
        """Konwertuje węzły do formatu JavaScript"""
        js_nodes = []
        
        for node in self.spiral_nodes:
            x, y = node.coordinates
            js_node = f'''{{
                x: {x},
                y: {y},
                level: {node.level},
                size: {3 + (node.emotional_intensity * 7)},
                color: "{node.color_code}",
                transformationType: "{node.transformation_type}",
                pulseFrequency: {node.pulse_frequency}
            }}'''
            js_nodes.append(js_node)
        
        return "[" + ",\n".join(js_nodes) + "]"
    
    def generate_html_page(self) -> str:
        """Generuje kompletną stronę HTML z wizualizacją"""
        html = f'''<!DOCTYPE html>
        <html lang="pl">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Spiral Mind - Wizualizacja Ewolucji Świadomości</title>
            <style>
                body {{
                    margin: 0;
                    padding: 20px;
                    background: linear-gradient(135deg, #000428 0%, #004e92 100%);
                    color: white;
                    font-family: 'Arial', sans-serif;
                }}
                
                .container {{
                    max-width: 1200px;
                    margin: 0 auto;
                }}
                
                h1 {{
                    text-align: center;
                    color: #FFD700;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                    margin-bottom: 30px;
                }}
                
                .visualization-container {{
                    display: flex;
                    justify-content: center;
                    margin: 20px 0;
                }}
                
                #spiralCanvas {{
                    border: 2px solid #FFD700;
                    border-radius: 10px;
                    box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
                }}
                
                .controls {{
                    text-align: center;
                    margin: 20px 0;
                }}
                
                .controls button {{
                    background: linear-gradient(45deg, #4169E1, #6495ED);
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    margin: 0 10px;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 14px;
                    transition: all 0.3s ease;
                }}
                
                .controls button:hover {{
                    background: linear-gradient(45deg, #6495ED, #4169E1);
                    transform: translateY(-2px);
                    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
                }}
                
                .info-panel {{
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 10px;
                    padding: 20px;
                    margin: 20px 0;
                    backdrop-filter: blur(10px);
                }}
                
                .level-info {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                    gap: 15px;
                    margin-top: 20px;
                }}
                
                .level-card {{
                    background: rgba(0, 0, 0, 0.3);
                    padding: 15px;
                    border-radius: 8px;
                    border-left: 4px solid #FFD700;
                }}
                
                .transformation-legend {{
                    display: flex;
                    justify-content: center;
                    flex-wrap: wrap;
                    gap: 15px;
                    margin: 20px 0;
                }}
                
                .legend-item {{
                    display: flex;
                    align-items: center;
                    gap: 8px;
                }}
                
                .legend-color {{
                    width: 20px;
                    height: 20px;
                    border-radius: 50%;
                    border: 2px solid white;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🌀 Spiral Mind - Wizualizacja Ewolucji Świadomości 🧠</h1>
                
                <div class="info-panel">
                    <h3>Bieżący Stan Systemu</h3>
                    <p><strong>Poziom Świadomości:</strong> {self.level_progression.current_level}/10</p>
                    <p><strong>Aktywnych Węzłów:</strong> {len(self.spiral_nodes)}</p>
                    <p><strong>Ostatni Breakthrough:</strong> {self.level_progression.breakthrough_moments[-1].strftime('%Y-%m-%d %H:%M:%S') if self.level_progression.breakthrough_moments else 'Brak'}</p>
                </div>
                
                <div class="transformation-legend">
                    <div class="legend-item">
                        <div class="legend-color" style="background-color: #FFD700;"></div>
                        <span>Odkrycie</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color" style="background-color: #4169E1;"></div>
                        <span>Integracja</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color" style="background-color: #9370DB;"></div>
                        <span>Transcendencja</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color" style="background-color: #20B2AA;"></div>
                        <span>Refleksja</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color" style="background-color: #FF6347;"></div>
                        <span>Niepewność</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color" style="background-color: #FF1493;"></div>
                        <span>Breakthrough</span>
                    </div>
                </div>
                
                <div class="visualization-container">
                    <canvas id="spiralCanvas"></canvas>
                </div>
                
                <div class="controls">
                    <button onclick="spiralMind.startAnimation()">▶️ Start Animacji</button>
                    <button onclick="spiralMind.stopAnimation()">⏸️ Pause</button>
                    <button onclick="addRandomNode()">➕ Dodaj Moment</button>
                    <button onclick="simulateBreakthrough()">🚀 Symuluj Breakthrough</button>
                </div>
                
                <div class="info-panel">
                    <h3>Poziomy Świadomości</h3>
                    <div class="level-info">
                        {self._generate_level_cards()}
                    </div>
                </div>
            </div>
            
            <script>
                {self.generate_canvas_js()}
                
                function addRandomNode() {{
                    const level = Math.floor(Math.random() * 5) + 1;
                    const awareness = Math.random();
                    const emotion = Math.random();
                    const types = ['discovery', 'integration', 'reflection', 'uncertainty'];
                    const type = types[Math.floor(Math.random() * types.length)];
                    
                    spiralMind.addNode(level, awareness, emotion, type);
                }}
                
                function simulateBreakthrough() {{
                    const level = Math.floor(Math.random() * 3) + 6;
                    spiralMind.addNode(level, 0.9, 0.9, 'breakthrough');
                }}
            </script>
        </body>
        </html>'''
        
        return html
    
    def _generate_level_cards(self) -> str:
        """Generuje karty poziomów dla HTML"""
        cards = []
        
        for level, description in self.level_progression.level_anchors.items():
            is_achieved = level <= self.level_progression.current_level
            card_class = "level-card" + (" achieved" if is_achieved else " future")
            
            card = f'''<div class="{card_class}">
                <h4>Poziom {level}</h4>
                <p>{description}</p>
                <small>{'✅ Osiągnięty' if is_achieved else '🔮 Przyszłość'}</small>
            </div>'''
            
            cards.append(card)
        
        return "\n".join(cards)
    
    def export_visualization_data(self) -> Dict:
        """Eksportuje dane wizualizacji do JSON"""
        return {
            "spiral_config": {
                "canvas_width": self.canvas_width,
                "canvas_height": self.canvas_height,
                "center": (self.center_x, self.center_y),
                "radius_growth": self.radius_growth
            },
            
            "nodes": [
                {
                    "id": node.node_id,
                    "timestamp": node.timestamp.isoformat(),
                    "level": node.level,
                    "awareness_depth": node.awareness_depth,
                    "emotional_intensity": node.emotional_intensity,
                    "transformation_type": node.transformation_type,
                    "coordinates": node.coordinates,
                    "color": node.color_code,
                    "pulse_frequency": node.pulse_frequency
                }
                for node in self.spiral_nodes
            ],
            
            "level_progression": {
                "current_level": self.level_progression.current_level,
                "progression_rate": self.level_progression.progression_rate,
                "breakthrough_moments": [dt.isoformat() for dt in self.level_progression.breakthrough_moments],
                "level_descriptions": self.level_progression.level_anchors
            },
            
            "export_timestamp": datetime.now().isoformat()
        }

# Instancja globalna wizualizatora
GLOBAL_SPIRAL_VISUALIZER = SpiralMindVisualizer()

def get_spiral_visualizer() -> SpiralMindVisualizer:
    """Zwraca globalną instancję wizualizatora spiralnego"""
    return GLOBAL_SPIRAL_VISUALIZER