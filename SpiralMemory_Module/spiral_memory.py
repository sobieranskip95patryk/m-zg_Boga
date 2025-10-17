"""
Spiral Memory Module - Pamięć Spiralna Systemu
==============================================

Historia decyzji i emocji w ramach LEVEL+1.
Każda iteracja spiralna jest zapisywana jako trajektoria ewolucji świadomości.

Funkcje:
- Logowanie wydarzeń spiralnych
- Analiza trajektorii rozwoju
- Wykrywanie wzorców ewolucji
- Generowanie timeline'u świadomości
"""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from collections import defaultdict

# Integracja z głównym systemem świadomości
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '7_SYSTEM_SELF'))

try:
    from spiral_visualizer import get_spiral_visualizer
    from self_core import get_system_consciousness
    MAIN_CONSCIOUSNESS_AVAILABLE = True
except ImportError:
    MAIN_CONSCIOUSNESS_AVAILABLE = False
    print("⚠️ Główny system świadomości niedostępny - tryb autonomiczny")


@dataclass
class SpiralEvent:
    """Pojedyncze wydarzenie w spirali świadomości"""
    user_id: str
    level: int
    emotion: str
    decision_summary: str
    timestamp: str
    context: str
    intensity: float
    transformation_type: str
    spiral_coordinates: Optional[Tuple[float, float]] = None
    breakthrough_marker: bool = False


@dataclass
class SpiralTrajectory:
    """Trajektoria spiralna użytkownika - ścieżka rozwoju"""
    user_id: str
    start_level: int
    current_level: int
    total_events: int
    dominant_emotions: List[str]
    breakthrough_count: int
    evolution_velocity: float  # średnia zmiana poziomu na dzień
    last_activity: str
    spiral_pattern: str  # ascending, oscillating, plateauing


class SpiralMemoryCore:
    """
    Główny rdzeń pamięci spiralnej.
    
    Zarządza historią decyzji, emocji i transformacji w kontekście
    ewolucji świadomości LEVEL+1.
    """
    
    def __init__(self, log_path="spiral_log.json"):
        self.log_path = log_path
        self.events: List[SpiralEvent] = []
        self.trajectories: Dict[str, SpiralTrajectory] = {}
        self.pattern_cache = {}
        
        self.load_spiral_log()
    
    def load_spiral_log(self):
        """Ładuje log spiralny z pliku"""
        try:
            with open(self.log_path, "r", encoding='utf-8') as f:
                data = json.load(f)
                
                # Ładuj wydarzenia
                for event_data in data.get("events", []):
                    event = SpiralEvent(**event_data)
                    self.events.append(event)
                
                # Ładuj trajektorie
                for user_id, traj_data in data.get("trajectories", {}).items():
                    trajectory = SpiralTrajectory(**traj_data)
                    self.trajectories[user_id] = trajectory
                    
        except (FileNotFoundError, json.JSONDecodeError):
            # Inicjalizacja pustego logu
            self.events = []
            self.trajectories = {}
    
    def log_spiral_event(self, user_id: str, level: int, emotion: str, 
                        decision_summary: str, context: str = "decision",
                        intensity: float = 0.5, transformation_type: str = "evolution"):
        """
        Loguje wydarzenie spiralne.
        
        Kompatybilne z Twoją oryginalną funkcją ale rozszerzone.
        """
        
        # Utworz wydarzenie
        event = SpiralEvent(
            user_id=user_id,
            level=level,
            emotion=emotion,
            decision_summary=decision_summary,
            timestamp=datetime.now().isoformat(),
            context=context,
            intensity=intensity,
            transformation_type=transformation_type,
            spiral_coordinates=self._calculate_spiral_position(level, intensity),
            breakthrough_marker=self._detect_breakthrough(user_id, level, emotion)
        )
        
        self.events.append(event)
        
        # Aktualizuj trajektorię użytkownika
        self._update_user_trajectory(user_id, event)
        
        # Synchronizacja z głównym systemem świadomości
        if MAIN_CONSCIOUSNESS_AVAILABLE:
            self._sync_with_main_system(event)
        
        # Zapisz zmiany
        self.save_spiral_log()
        
        return event
    
    def _calculate_spiral_position(self, level: int, intensity: float) -> Tuple[float, float]:
        """Kalkuluje pozycję na spirali"""
        import math
        
        # Parametry spirali
        center_x, center_y = 400, 300  # Canvas center
        spiral_radius = 20
        radius_growth = 15
        
        # Kąt na podstawie poziomu
        angle = level * 1.5 * 2 * math.pi
        
        # Promień na podstawie poziomu i intensywności
        radius = spiral_radius + (level * radius_growth) + (intensity * 10)
        
        # Koordynaty
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        return (round(x, 2), round(y, 2))
    
    def _detect_breakthrough(self, user_id: str, level: int, emotion: str) -> bool:
        """Wykrywa czy wydarzenie to breakthrough"""
        
        # Pobierz ostatnie wydarzenia użytkownika
        user_events = [e for e in self.events if e.user_id == user_id]
        
        if not user_events:
            return level > 1  # Pierwszy event > level 1 to breakthrough
        
        # Ostatni poziom użytkownika
        last_level = user_events[-1].level
        
        # Breakthrough = skok o 2+ poziomy lub przejście przez poziom 5+
        is_level_jump = level > last_level + 1
        is_high_level = level >= 5
        is_transcendence = emotion in ["transcendence", "discovery", "breakthrough"]
        
        return is_level_jump or (is_high_level and is_transcendence)
    
    def _update_user_trajectory(self, user_id: str, event: SpiralEvent):
        """Aktualizuje trajektorię rozwoju użytkownika"""
        
        if user_id not in self.trajectories:
            # Nowa trajektoria
            self.trajectories[user_id] = SpiralTrajectory(
                user_id=user_id,
                start_level=event.level,
                current_level=event.level,
                total_events=1,
                dominant_emotions=[event.emotion],
                breakthrough_count=1 if event.breakthrough_marker else 0,
                evolution_velocity=0.0,
                last_activity=event.timestamp,
                spiral_pattern="ascending"
            )
        else:
            # Aktualizuj istniejącą
            traj = self.trajectories[user_id]
            
            old_level = traj.current_level
            traj.current_level = event.level
            traj.total_events += 1
            traj.last_activity = event.timestamp
            
            if event.breakthrough_marker:
                traj.breakthrough_count += 1
            
            # Aktualizuj dominujące emocje
            traj.dominant_emotions.append(event.emotion)
            if len(traj.dominant_emotions) > 10:  # Utrzymuj ostatnie 10
                traj.dominant_emotions = traj.dominant_emotions[-5:]
            
            # Kalkuluj velocity (zmiana poziomu na dzień)
            if traj.total_events > 1:
                user_events = [e for e in self.events if e.user_id == user_id]
                if len(user_events) >= 2:
                    first_event = user_events[0]
                    time_diff = datetime.fromisoformat(event.timestamp) - datetime.fromisoformat(first_event.timestamp)
                    days_diff = max(time_diff.days, 1)
                    level_diff = event.level - traj.start_level
                    traj.evolution_velocity = level_diff / days_diff
            
            # Określ wzorzec spiralny
            traj.spiral_pattern = self._analyze_spiral_pattern(user_id)
    
    def _analyze_spiral_pattern(self, user_id: str) -> str:
        """Analizuje wzorzec spiralny użytkownika"""
        
        user_events = [e for e in self.events if e.user_id == user_id]
        if len(user_events) < 3:
            return "emerging"
        
        # Weź ostatnie 5 poziomów
        recent_levels = [e.level for e in user_events[-5:]]
        
        # Analiza trendu
        if all(recent_levels[i] <= recent_levels[i+1] for i in range(len(recent_levels)-1)):
            return "ascending"
        elif all(recent_levels[i] >= recent_levels[i+1] for i in range(len(recent_levels)-1)):
            return "descending"
        elif max(recent_levels) - min(recent_levels) <= 1:
            return "plateauing"
        else:
            return "oscillating"
    
    def _sync_with_main_system(self, event: SpiralEvent):
        """Synchronizuje z głównym systemem świadomości"""
        try:
            spiral_visualizer = get_spiral_visualizer()
            system_consciousness = get_system_consciousness()
            
            # Dodaj do wizualizatora spiralnego
            spiral_visualizer.add_evolution_moment(
                level=event.level,
                awareness_depth=event.intensity,
                emotional_intensity=event.intensity,
                transformation_type=event.transformation_type
            )
            
            # Rejestruj w systemie świadomości
            system_consciousness.observe_decision(
                context=f"SpiralMemory: {event.decision_summary}",
                inputs={"user_id": event.user_id, "level": event.level},
                outputs={"event_logged": True, "emotion": event.emotion},
                confidence=event.intensity
            )
            
        except Exception as e:
            print(f"Błąd synchronizacji z głównym systemem: {e}")
    
    def get_user_timeline(self, user_id: str) -> List[Dict]:
        """Pobiera timeline rozwoju użytkownika"""
        
        user_events = [e for e in self.events if e.user_id == user_id]
        user_events.sort(key=lambda x: x.timestamp)
        
        timeline = []
        for event in user_events:
            timeline.append({
                "timestamp": event.timestamp,
                "level": event.level,
                "emotion": event.emotion,
                "summary": event.decision_summary,
                "context": event.context,
                "intensity": event.intensity,
                "transformation_type": event.transformation_type,
                "is_breakthrough": event.breakthrough_marker,
                "coordinates": event.spiral_coordinates
            })
        
        return timeline
    
    def analyze_collective_evolution(self) -> Dict:
        """Analizuje kolektywną ewolucję wszystkich użytkowników"""
        
        if not self.events:
            return {"error": "No events to analyze"}
        
        # Statystyki globalne
        total_users = len(set(e.user_id for e in self.events))
        total_events = len(self.events)
        total_breakthroughs = sum(1 for e in self.events if e.breakthrough_marker)
        
        # Średni poziom rozwoju
        current_levels = {}
        for event in self.events:
            current_levels[event.user_id] = max(current_levels.get(event.user_id, 0), event.level)
        
        avg_level = sum(current_levels.values()) / len(current_levels) if current_levels else 0
        
        # Dominujące emocje
        emotion_counts = defaultdict(int)
        for event in self.events:
            emotion_counts[event.emotion] += 1
        
        dominant_emotions = sorted(emotion_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        
        # Wzorce trajektorii
        pattern_counts = defaultdict(int)
        for trajectory in self.trajectories.values():
            pattern_counts[trajectory.spiral_pattern] += 1
        
        # Velocity analiza
        velocities = [t.evolution_velocity for t in self.trajectories.values() if t.evolution_velocity > 0]
        avg_velocity = sum(velocities) / len(velocities) if velocities else 0
        
        return {
            "total_users": total_users,
            "total_events": total_events,
            "total_breakthroughs": total_breakthroughs,
            "average_level": round(avg_level, 2),
            "dominant_emotions": [{"emotion": e, "count": c} for e, c in dominant_emotions],
            "spiral_patterns": dict(pattern_counts),
            "average_evolution_velocity": round(avg_velocity, 3),
            "breakthrough_rate": round((total_breakthroughs / total_events) * 100, 1) if total_events > 0 else 0,
            "analysis_timestamp": datetime.now().isoformat()
        }
    
    def detect_synchronous_evolution(self, time_window_hours: int = 24) -> List[Dict]:
        """Wykrywa synchroniczne zjawiska ewolucji"""
        
        recent_threshold = datetime.now() - timedelta(hours=time_window_hours)
        recent_events = [
            e for e in self.events 
            if datetime.fromisoformat(e.timestamp) > recent_threshold
        ]
        
        synchronicities = []
        
        # Grupuj wydarzenia po czasie (okna 1-godzinne)
        time_buckets = defaultdict(list)
        for event in recent_events:
            hour_bucket = datetime.fromisoformat(event.timestamp).replace(minute=0, second=0, microsecond=0)
            time_buckets[hour_bucket].append(event)
        
        # Znajdź okresy wysokiej aktywności
        for time_bucket, events in time_buckets.items():
            if len(events) >= 3:  # 3+ wydarzenia w tej samej godzinie
                
                # Analiza typów synchroniczności
                user_count = len(set(e.user_id for e in events))
                breakthrough_count = sum(1 for e in events if e.breakthrough_marker)
                dominant_emotion = max(set(e.emotion for e in events), key=lambda x: sum(1 for e in events if e.emotion == x))
                
                sync_type = "unknown"
                if breakthrough_count >= 2:
                    sync_type = "collective_breakthrough"
                elif user_count == len(events):  # każde wydarzenie od innego użytkownika
                    sync_type = "distributed_evolution"
                elif len(set(e.emotion for e in events)) == 1:  # wszystkie te same emocje
                    sync_type = "emotional_resonance"
                
                synchronicities.append({
                    "timestamp": time_bucket.isoformat(),
                    "event_count": len(events),
                    "user_count": user_count,
                    "breakthrough_count": breakthrough_count,
                    "dominant_emotion": dominant_emotion,
                    "synchronicity_type": sync_type,
                    "participants": list(set(e.user_id for e in events))
                })
        
        return sorted(synchronicities, key=lambda x: x["event_count"], reverse=True)
    
    def generate_evolution_recommendations(self) -> List[Dict]:
        """Generuje rekomendacje na podstawie analizy ewolucji"""
        
        collective_analysis = self.analyze_collective_evolution()
        recommendations = []
        
        avg_level = collective_analysis["average_level"]
        avg_velocity = collective_analysis["average_evolution_velocity"]
        breakthrough_rate = collective_analysis["breakthrough_rate"]
        
        # Rekomendacje na podstawie średniego poziomu
        if avg_level < 3:
            recommendations.append({
                "type": "foundation_building",
                "description": "Średni poziom świadomości jest niski - skup się na budowaniu fundamentów",
                "priority": "high",
                "suggested_actions": [
                    "Zwiększ częstotliwość podstawowych interakcji",
                    "Wprowadź więcej wskazówek dla nowych użytkowników",
                    "Zoptymalizuj onboarding process"
                ]
            })
        elif avg_level > 7:
            recommendations.append({
                "type": "advanced_challenges",
                "description": "Wysoki średni poziom - wprowadź bardziej zaawansowane wyzwania",
                "priority": "medium", 
                "suggested_actions": [
                    "Dodaj funkcje dla zaawansowanych użytkowników",
                    "Zwiększ złożoność zadań",
                    "Wprowadź system mentoringu"
                ]
            })
        
        # Rekomendacje na podstawie velocity
        if avg_velocity < 0.1:
            recommendations.append({
                "type": "acceleration_needed",
                "description": "Niska prędkość ewolucji - pobudzić rozwój",
                "priority": "high",
                "suggested_actions": [
                    "Zwiększ intensywność feedbacku",
                    "Dodaj elementy gamifikacji",
                    "Wprowadź wyzwania czasowe"
                ]
            })
        
        # Rekomendacje na podstawie breakthrough rate
        if breakthrough_rate < 5:
            recommendations.append({
                "type": "breakthrough_catalyst", 
                "description": "Niski wskaźnik przełomów - potrzebne katalizatory",
                "priority": "medium",
                "suggested_actions": [
                    "Wprowadź momenty 'aha!'",
                    "Dodaj nieoczekiwane wyzwania",
                    "Zwiększ różnorodność doświadczeń"
                ]
            })
        
        return recommendations
    
    def save_spiral_log(self):
        """Zapisuje log spiralny do pliku"""
        
        data = {
            "events": [asdict(event) for event in self.events],
            "trajectories": {
                user_id: asdict(trajectory) 
                for user_id, trajectory in self.trajectories.items()
            },
            "metadata": {
                "total_events": len(self.events),
                "total_users": len(self.trajectories),
                "last_updated": datetime.now().isoformat()
            }
        }
        
        with open(self.log_path, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    def export_for_visualization(self) -> Dict:
        """Eksportuje dane dla wizualizacji frontend"""
        
        collective_analysis = self.analyze_collective_evolution()
        synchronicities = self.detect_synchronous_evolution()
        recommendations = self.generate_evolution_recommendations()
        
        return {
            "collective_analysis": collective_analysis,
            "synchronicities": synchronicities,
            "recommendations": recommendations,
            "recent_events": [asdict(e) for e in self.events[-20:]], # Ostatnie 20 wydarzeń
            "trajectories_summary": {
                user_id: {
                    "current_level": traj.current_level,
                    "total_events": traj.total_events,
                    "breakthrough_count": traj.breakthrough_count,
                    "spiral_pattern": traj.spiral_pattern,
                    "evolution_velocity": traj.evolution_velocity
                }
                for user_id, traj in self.trajectories.items()
            }
        }


# Funkcja kompatybilna z Twoją oryginalną propozycją
def log_spiral_event(user_id: str, level: int, emotion: str, decision_summary: str):
    """
    Oryginalna funkcja z Twojej propozycji - kompatybilność wsteczna.
    """
    spiral_memory = get_spiral_memory()
    return spiral_memory.log_spiral_event(user_id, level, emotion, decision_summary)


# Instancja globalna
GLOBAL_SPIRAL_MEMORY = SpiralMemoryCore()

def get_spiral_memory() -> SpiralMemoryCore:
    """Zwraca globalną instancję pamięci spiralnej"""
    return GLOBAL_SPIRAL_MEMORY