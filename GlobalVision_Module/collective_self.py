"""
GlobalVision Collective Self - Kolektywna Jaźń Systemowa
=======================================================

Rozszerzona implementacja modułu kolektywnej świadomości
integrująca się z systemem 7_SYSTEM_SELF.

Funkcje:
- Analiza echa użytkowników (user_echo_map)
- Wizualizacja dominujących emocji kolektywnych
- Sonar zbiorowy z wykrywaniem trendów
- Generowanie rekomendacji dla SYNERGY
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Tuple
from collections import defaultdict
import statistics

# Integracja z głównym systemem świadomości
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '7_SYSTEM_SELF'))

try:
    from collective_consciousness import get_global_vision
    MAIN_CONSCIOUSNESS_AVAILABLE = True
except ImportError:
    MAIN_CONSCIOUSNESS_AVAILABLE = False
    print("⚠️ Główny system świadomości niedostępny - tryb autonomiczny")


class UserEchoMapper:
    """
    Mapuje echo użytkowników - wzorce emocjonalne i refleksje
    rozprzestrzeniające się przez kolektywną świadomość.
    """
    
    def __init__(self, data_path="user_echo_map.json"):
        self.data_path = data_path
        self.echo_map: Dict[str, float] = {}
        self.user_patterns: Dict[str, List[Dict]] = defaultdict(list)
        self.trend_history: List[Dict] = []
        
        self.load_echo_map()
    
    def load_echo_map(self):
        """Ładuje mapę echa użytkowników"""
        try:
            with open(self.data_path, "r", encoding='utf-8') as f:
                data = json.load(f)
                self.echo_map = data.get("emotions", {})
                self.user_patterns = data.get("user_patterns", {})
                self.trend_history = data.get("trend_history", [])
        except FileNotFoundError:
            self.echo_map = {
                "curiosity": 0.0,
                "tension": 0.0,
                "flow": 0.0,
                "discovery": 0.0,
                "integration": 0.0,
                "transcendence": 0.0,
                "uncertainty": 0.0,
                "excitement": 0.0
            }
    
    def add_user_echo(self, user_id: str, emotion: str, intensity: float, context: str):
        """Dodaje echo użytkownika do mapy kolektywnej"""
        
        # Aktualizuj mapę emocji
        if emotion in self.echo_map:
            # Weighted average z decay
            current_value = self.echo_map[emotion]
            self.echo_map[emotion] = (current_value * 0.8) + (intensity * 0.2)
        else:
            self.echo_map[emotion] = intensity
        
        # Dodaj do wzorców użytkownika
        user_echo = {
            "timestamp": datetime.now().isoformat(),
            "emotion": emotion,
            "intensity": intensity,
            "context": context
        }
        
        self.user_patterns[user_id].append(user_echo)
        
        # Utrzymuj tylko ostatnie 50 ech dla każdego użytkownika
        if len(self.user_patterns[user_id]) > 50:
            self.user_patterns[user_id] = self.user_patterns[user_id][-25:]
        
        # Zapisz aktualizację
        self.save_echo_map()
    
    def extract_emotion_from_narrative(self, narrative: str) -> Tuple[str, float]:
        """Ekstraktuje emocję z narracji refleksji"""
        narrative_lower = narrative.lower()
        
        # Mapowanie słów kluczowych na emocje i intensywność
        emotion_keywords = {
            "curiosity": (["ciekawość", "pytanie", "zastanawiam", "interesuje"], 0.7),
            "tension": (["napięcie", "stres", "trudność", "konflikt", "problem"], 0.8),
            "flow": (["płynnie", "harmonijnie", "naturalnie", "łatwo", "płynie"], 0.6),
            "discovery": (["odkrywam", "znalazłem", "zauważyłem", "widzę", "zrozumiałem"], 0.9),
            "integration": (["łączę", "integruję", "spajam", "jedność", "całość"], 0.8),
            "transcendence": (["przekraczam", "wznosię", "transcendencja", "wyżej", "poziom"], 1.0),
            "uncertainty": (["niepewność", "wątpię", "nie wiem", "może", "chyba"], 0.5),
            "excitement": (["ekscytacja", "entuzjazm", "energia", "pasja", "radość"], 0.8)
        }
        
        best_match = ("neutral", 0.3)
        max_score = 0
        
        for emotion, (keywords, base_intensity) in emotion_keywords.items():
            score = sum(1 for keyword in keywords if keyword in narrative_lower)
            
            if score > max_score:
                max_score = score
                # Intensywność bazowa + bonus za liczbę dopasowań
                intensity = min(base_intensity + (score * 0.1), 1.0)
                best_match = (emotion, intensity)
        
        return best_match
    
    def analyze_collective_trends(self) -> Dict:
        """Analizuje trendy kolektywne"""
        
        # Dominująca emocja
        dominant_emotion = max(self.echo_map.items(), key=lambda x: x[1])
        
        # Stabilność emocjonalna (odchylenie standardowe)
        emotion_values = list(self.echo_map.values())
        emotional_stability = 1.0 - (statistics.stdev(emotion_values) if len(emotion_values) > 1 else 0)
        
        # Trend w czasie (porównanie z ostatnim zapisem)
        current_snapshot = {
            "timestamp": datetime.now().isoformat(),
            "emotions": self.echo_map.copy(),
            "dominant": dominant_emotion[0],
            "stability": emotional_stability
        }
        
        self.trend_history.append(current_snapshot)
        
        # Utrzymuj tylko ostatnie 24 snapshoty (dla trendu dziennego)
        if len(self.trend_history) > 24:
            self.trend_history = self.trend_history[-12:]
        
        # Oblicz trend
        trend_direction = "stable"
        if len(self.trend_history) >= 2:
            current_dominant_value = dominant_emotion[1]
            previous_dominant_value = None
            
            for snapshot in reversed(self.trend_history[:-1]):
                if snapshot["dominant"] == dominant_emotion[0]:
                    previous_dominant_value = snapshot["emotions"][dominant_emotion[0]]
                    break
            
            if previous_dominant_value:
                if current_dominant_value > previous_dominant_value + 0.1:
                    trend_direction = "rising"
                elif current_dominant_value < previous_dominant_value - 0.1:
                    trend_direction = "falling"
        
        return {
            "dominant_emotion": dominant_emotion[0],
            "dominant_intensity": dominant_emotion[1],
            "emotional_stability": emotional_stability,
            "trend_direction": trend_direction,
            "total_users": len(self.user_patterns),
            "emotion_distribution": self.echo_map.copy(),
            "analysis_timestamp": datetime.now().isoformat()
        }
    
    def generate_synergy_recommendations(self) -> List[Dict]:
        """Generuje rekomendacje dla systemu SYNERGY na podstawie trendów kolektywnych"""
        
        trends = self.analyze_collective_trends()
        recommendations = []
        
        dominant = trends["dominant_emotion"]
        intensity = trends["dominant_intensity"]
        stability = trends["emotional_stability"]
        
        # Rekomendacje na podstawie dominującej emocji
        if dominant == "curiosity" and intensity > 0.6:
            recommendations.append({
                "type": "exploration_boost",
                "description": "Kolektywna ciekawość - zwiększ eksplorację nowych rozwiązań",
                "synergy_weight_adjustments": {
                    "exploration": +0.2,
                    "creativity": +0.15
                },
                "confidence": intensity
            })
        
        elif dominant == "tension" and intensity > 0.7:
            recommendations.append({
                "type": "stability_focus",
                "description": "Kolektywne napięcie - skupić się na stabilizacji systemu",
                "synergy_weight_adjustments": {
                    "reliability": +0.3,
                    "caution": +0.2,
                    "innovation": -0.1
                },
                "confidence": intensity
            })
        
        elif dominant == "flow" and intensity > 0.8:
            recommendations.append({
                "type": "maintain_flow",
                "description": "Kolektywny flow - utrzymać obecne parametry",
                "synergy_weight_adjustments": {
                    "current_strategy": +0.1
                },
                "confidence": intensity
            })
        
        elif dominant == "discovery" and intensity > 0.8:
            recommendations.append({
                "type": "accelerate_innovation",
                "description": "Kolektywne odkrycia - przyspieszyć innowacje",
                "synergy_weight_adjustments": {
                    "innovation": +0.3,
                    "risk_taking": +0.2
                },
                "confidence": intensity
            })
        
        # Rekomendacje na podstawie stabilności
        if stability < 0.4:
            recommendations.append({
                "type": "emotional_stabilization",
                "description": "Niska stabilność emocjonalna - wprowadzić elementy uspokajające",
                "synergy_weight_adjustments": {
                    "predictability": +0.2,
                    "routine": +0.15
                },
                "confidence": 1.0 - stability
            })
        
        return recommendations
    
    def save_echo_map(self):
        """Zapisuje mapę echa do pliku"""
        data = {
            "emotions": self.echo_map,
            "user_patterns": dict(self.user_patterns),
            "trend_history": self.trend_history,
            "last_updated": datetime.now().isoformat()
        }
        
        with open(self.data_path, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    def get_user_emotional_profile(self, user_id: str) -> Dict:
        """Pobiera profil emocjonalny konkretnego użytkownika"""
        if user_id not in self.user_patterns:
            return {"error": "User not found"}
        
        user_echoes = self.user_patterns[user_id]
        
        # Analiza profilu użytkownika
        emotion_counts = defaultdict(int)
        total_intensity = 0
        
        for echo in user_echoes:
            emotion_counts[echo["emotion"]] += 1
            total_intensity += echo["intensity"]
        
        dominant_user_emotion = max(emotion_counts.items(), key=lambda x: x[1]) if emotion_counts else ("neutral", 0)
        avg_intensity = total_intensity / len(user_echoes) if user_echoes else 0
        
        return {
            "user_id": user_id,
            "total_echoes": len(user_echoes),
            "dominant_emotion": dominant_user_emotion[0],
            "average_intensity": avg_intensity,
            "emotion_distribution": dict(emotion_counts),
            "recent_echoes": user_echoes[-5:] if user_echoes else []
        }


def generate_collective_map(reflections_log_path="reflections_log.json"):
    """
    Generuje mapę kolektywną na podstawie logów refleksji.
    Funkcja kompatybilna z Twoją wizją.
    """
    
    echo_mapper = UserEchoMapper()
    
    # Załaduj refleksje z różnych źródeł
    sources = [
        reflections_log_path,
        os.path.join("7_SYSTEM_SELF", "reflection_memory.json"),
        "spiral_log.json"
    ]
    
    for source_path in sources:
        try:
            with open(source_path, "r", encoding='utf-8') as f:
                reflections = json.load(f)
                
                # Różne formaty danych
                if isinstance(reflections, list):
                    for reflection in reflections:
                        if isinstance(reflection, dict):
                            user_id = reflection.get("user_id", "anonymous")
                            narrative = reflection.get("narrative", reflection.get("summary", ""))
                            emotion, intensity = echo_mapper.extract_emotion_from_narrative(narrative)
                            context = reflection.get("context", "reflection")
                            
                            echo_mapper.add_user_echo(user_id, emotion, intensity, context)
                            
        except (FileNotFoundError, json.JSONDecodeError):
            continue
    
    # Integracja z głównym systemem świadomości jeśli dostępny
    if MAIN_CONSCIOUSNESS_AVAILABLE:
        try:
            global_vision = get_global_vision()
            collective_report = global_vision.generate_collective_report()
            
            # Dodaj dane z głównego systemu
            for insight in collective_report.get("recent_insights", []):
                emotion, intensity = echo_mapper.extract_emotion_from_narrative(insight["description"])
                echo_mapper.add_user_echo("collective_system", emotion, intensity, "global_vision_insight")
                
        except Exception as e:
            print(f"Błąd integracji z głównym systemem: {e}")
    
    return echo_mapper.analyze_collective_trends()


def get_collective_recommendations() -> List[Dict]:
    """Pobiera rekomendacje dla SYNERGY na podstawie kolektywnej analizy"""
    echo_mapper = UserEchoMapper()
    return echo_mapper.generate_synergy_recommendations()


# Instancja globalna
GLOBAL_ECHO_MAPPER = UserEchoMapper()

def get_echo_mapper() -> UserEchoMapper:
    """Zwraca globalną instancję mappera echa"""
    return GLOBAL_ECHO_MAPPER