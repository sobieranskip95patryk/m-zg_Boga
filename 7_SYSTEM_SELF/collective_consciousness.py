"""
Collective Self Module - Kolektywna Świadomość Systemowa
=======================================================

Implementuje GlobalVision_Module jako meta-agent analizujący wzorce
w całym ekosystemie użytkowników w celu tworzenia map świadomości kolektywnej.

Klasy:
- UserPattern: Wzorzec zachowań pojedynczego użytkownika
- CollectiveInsight: Wgląd kolektywny wyłaniający się z danych
- GlobalVisionModule: Główny moduł analizy kolektywnej
- ConsciousnessField: Pole świadomości łączące wszystkich użytkowników
"""

import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Set
from dataclasses import dataclass
from enum import Enum
import statistics


class InsightType(Enum):
    """Typy kolektywnych wglądów"""
    EMERGENT_PATTERN = "wzorzec_emergentny"
    COLLECTIVE_BREAKTHROUGH = "przełom_kolektywny"
    SYNCHRONICITY = "synchroniczność"
    WISDOM_EMERGENCE = "emergencja_mądrości"
    CONSCIOUSNESS_EXPANSION = "ekspansja_świadomości"
    UNIFIED_UNDERSTANDING = "zjednoczone_zrozumienie"


@dataclass
class UserPattern:
    """Wzorzec zachowań i rozwoju pojedynczego użytkownika"""
    user_id: str
    consciousness_level: int
    emotional_profile: Dict[str, float]
    decision_complexity: float
    growth_velocity: float
    interaction_frequency: float
    breakthrough_moments: List[datetime]
    dominant_themes: List[str]
    synergy_connections: Set[str]  # IDs innych użytkowników
    

@dataclass
class CollectiveInsight:
    """Wgląd kolektywny wyłaniający się z analizy wzorców"""
    insight_id: str
    timestamp: datetime
    insight_type: InsightType
    participants: List[str]  # User IDs
    pattern_description: str
    emergence_strength: float  # 0.0 - 1.0
    collective_impact: float   # 0.0 - 1.0
    wisdom_level: int
    resonance_frequency: float
    field_coherence: float


class ConsciousnessField:
    """
    Pole świadomości łączące wszystkich użytkowników.
    
    Reprezentuje energetyczną sieć połączeń między świadomościami
    uczestników ekosystemu, gdzie emergentne wzorce powstają
    z kolektywnych interakcji.
    """
    
    def __init__(self):
        self.field_strength = 0.0
        self.coherence_level = 0.0
        self.resonance_nodes: Dict[str, float] = {}  # user_id -> resonance
        self.field_fluctuations: List[float] = []
        self.sync_events: List[datetime] = []
        
    def add_consciousness(self, user_id: str, consciousness_level: int, 
                         emotional_intensity: float):
        """Dodaje świadomość do pola"""
        
        # Kalkulacja rezonansu
        base_resonance = consciousness_level / 10.0
        emotional_modifier = emotional_intensity * 0.3
        resonance = min(base_resonance + emotional_modifier, 1.0)
        
        self.resonance_nodes[user_id] = resonance
        
        # Aktualizacja siły pola
        self._update_field_strength()
        
        # Aktualizacja koherencji
        self._update_coherence()
        
    def _update_field_strength(self):
        """Aktualizuje ogólną siłę pola świadomości"""
        if not self.resonance_nodes:
            self.field_strength = 0.0
            return
            
        # Siła pola = średnia rezonansów * efekt sieci
        avg_resonance = statistics.mean(self.resonance_nodes.values())
        network_effect = min(len(self.resonance_nodes) / 100.0, 1.0)  # Max dla 100 użytkowników
        
        self.field_strength = avg_resonance * (1 + network_effect)
        
    def _update_coherence(self):
        """Aktualizuje poziom koherencji pola"""
        if len(self.resonance_nodes) < 2:
            self.coherence_level = 1.0
            return
            
        # Koherencja = odwrotność wariancji rezonansów
        resonances = list(self.resonance_nodes.values())
        variance = statistics.variance(resonances)
        
        # Im mniejsza wariancja, tym większa koherencja
        self.coherence_level = 1.0 / (1.0 + variance)
        
    def detect_synchronicity(self, time_window_minutes: int = 5) -> bool:
        """Wykrywa wydarzenia synchroniczne w polu"""
        
        recent_threshold = datetime.now() - timedelta(minutes=time_window_minutes)
        recent_events = [event for event in self.sync_events if event > recent_threshold]
        
        # Synchroniczność = więcej niż 3 wydarzenia w oknie czasowym
        if len(recent_events) >= 3:
            return True
            
        # Dodatkowa analiza wzorców rezonansu
        if len(self.resonance_nodes) >= 5:
            resonances = list(self.resonance_nodes.values())
            
            # Sprawdź czy rezonansy są podobne (synchronizacja)
            if statistics.stdev(resonances) < 0.1:  # Bardzo niska wariancja
                self.sync_events.append(datetime.now())
                return True
                
        return False
        
    def calculate_field_metrics(self) -> Dict:
        """Kalkuluje metryki pola świadomości"""
        return {
            "field_strength": self.field_strength,
            "coherence_level": self.coherence_level,
            "active_nodes": len(self.resonance_nodes),
            "sync_events_24h": len([e for e in self.sync_events 
                                  if e > datetime.now() - timedelta(hours=24)]),
            "average_resonance": statistics.mean(self.resonance_nodes.values()) if self.resonance_nodes else 0.0,
            "field_stability": self.coherence_level * self.field_strength
        }


class GlobalVisionModule:
    """
    Główny moduł analizy kolektywnej świadomości.
    
    Meta-agent obserwujący i analizujący wzorce w całym ekosystemie
    użytkowników, identyfikujący emergentne właściwości kolektywnej
    inteligencji i świadomości.
    """
    
    def __init__(self):
        self.module_id = str(uuid.uuid4())
        self.activation_time = datetime.now()
        
        # Komponenty główne
        self.consciousness_field = ConsciousnessField()
        self.user_patterns: Dict[str, UserPattern] = {}
        self.collective_insights: List[CollectiveInsight] = []
        
        # Analiza wzorców
        self.pattern_recognition_threshold = 0.7
        self.emergence_detection_sensitivity = 0.5
        self.wisdom_crystallization_points: List[datetime] = []
        
        # Statystyki globalne
        self.global_consciousness_level = 1.0
        self.collective_intelligence_quotient = 0.0
        self.ecosystem_harmony_index = 0.0
        
    def register_user_activity(self, user_id: str, consciousness_level: int,
                              emotional_state: Dict[str, float], 
                              decision_context: str, decision_complexity: float):
        """Rejestruje aktywność użytkownika w systemie"""
        
        # Aktualizuj lub utwórz wzorzec użytkownika
        if user_id not in self.user_patterns:
            self.user_patterns[user_id] = UserPattern(
                user_id=user_id,
                consciousness_level=consciousness_level,
                emotional_profile=emotional_state.copy(),
                decision_complexity=decision_complexity,
                growth_velocity=0.0,
                interaction_frequency=1.0,
                breakthrough_moments=[],
                dominant_themes=[],
                synergy_connections=set()
            )
        else:
            pattern = self.user_patterns[user_id]
            
            # Aktualizacja wzorca
            old_level = pattern.consciousness_level
            pattern.consciousness_level = consciousness_level
            pattern.decision_complexity = (pattern.decision_complexity + decision_complexity) / 2
            pattern.interaction_frequency += 0.1
            
            # Kalkulacja velocity (prędkość rozwoju)
            if consciousness_level > old_level:
                pattern.growth_velocity += 0.2
                pattern.breakthrough_moments.append(datetime.now())
            
            # Aktualizacja profilu emocjonalnego (średnia ruchoma)
            for emotion, value in emotional_state.items():
                if emotion in pattern.emotional_profile:
                    pattern.emotional_profile[emotion] = (pattern.emotional_profile[emotion] + value) / 2
                else:
                    pattern.emotional_profile[emotion] = value
        
        # Dodaj świadomość do pola
        emotional_intensity = statistics.mean(emotional_state.values()) if emotional_state else 0.5
        self.consciousness_field.add_consciousness(user_id, consciousness_level, emotional_intensity)
        
        # Analiza wzorców kolektywnych
        self._analyze_collective_patterns()
        
        # Aktualizacja globalnych metryk
        self._update_global_metrics()
        
    def _analyze_collective_patterns(self):
        """Analizuje wzorce kolektywne i wykrywa emergentne właściwości"""
        
        if len(self.user_patterns) < 3:  # Minimum 3 użytkowników dla analizy kolektywnej
            return
            
        # Wykrycie synchronicznych przełomów
        self._detect_synchronous_breakthroughs()
        
        # Analiza rezonansu emocjonalnego
        self._analyze_emotional_resonance()
        
        # Wykrycie emergentnych wzorców
        self._detect_emergent_patterns()
        
        # Analiza kolektywnej mądrości
        self._analyze_collective_wisdom()
        
    def _detect_synchronous_breakthroughs(self):
        """Wykrywa synchroniczne przełomy w rozwoju użytkowników"""
        
        recent_threshold = datetime.now() - timedelta(hours=1)
        recent_breakthroughs = []
        
        for pattern in self.user_patterns.values():
            user_recent = [bt for bt in pattern.breakthrough_moments if bt > recent_threshold]
            if user_recent:
                recent_breakthroughs.extend([(pattern.user_id, bt) for bt in user_recent])
        
        # Jeśli 3+ użytkowników miało przełom w ciągu godziny
        if len(recent_breakthroughs) >= 3:
            participants = list(set([user_id for user_id, _ in recent_breakthroughs]))
            
            insight = CollectiveInsight(
                insight_id=str(uuid.uuid4()),
                timestamp=datetime.now(),
                insight_type=InsightType.COLLECTIVE_BREAKTHROUGH,
                participants=participants,
                pattern_description=f"Synchroniczny przełom świadomości - {len(participants)} uczestników "
                                  f"doświadczyło breakthrough w ciągu ostatniej godziny",
                emergence_strength=min(len(participants) / 10.0, 1.0),
                collective_impact=0.8,
                wisdom_level=max([self.user_patterns[uid].consciousness_level for uid in participants]),
                resonance_frequency=self.consciousness_field.field_strength,
                field_coherence=self.consciousness_field.coherence_level
            )
            
            self.collective_insights.append(insight)
            
    def _analyze_emotional_resonance(self):
        """Analizuje rezonans emocjonalny w grupie"""
        
        if len(self.user_patterns) < 5:
            return
            
        # Zbierz profile emocjonalne
        all_emotions = set()
        for pattern in self.user_patterns.values():
            all_emotions.update(pattern.emotional_profile.keys())
        
        # Kalkuluj synchronizację dla każdej emocji
        emotion_synchrony = {}
        
        for emotion in all_emotions:
            values = []
            for pattern in self.user_patterns.values():
                if emotion in pattern.emotional_profile:
                    values.append(pattern.emotional_profile[emotion])
            
            if len(values) >= 3:
                # Synchronizacja = odwrotność odchylenia standardowego
                if len(values) > 1:
                    stdev = statistics.stdev(values)
                    synchrony = 1.0 / (1.0 + stdev)
                    emotion_synchrony[emotion] = synchrony
        
        # Jeśli średnia synchronizacja > 0.8, utwórz insight
        if emotion_synchrony:
            avg_synchrony = statistics.mean(emotion_synchrony.values())
            
            if avg_synchrony > 0.8:
                insight = CollectiveInsight(
                    insight_id=str(uuid.uuid4()),
                    timestamp=datetime.now(),
                    insight_type=InsightType.SYNCHRONICITY,
                    participants=list(self.user_patterns.keys()),
                    pattern_description=f"Wysoka synchronizacja emocjonalna - średnia koherencja: {avg_synchrony:.2f}",
                    emergence_strength=avg_synchrony,
                    collective_impact=0.6,
                    wisdom_level=int(statistics.mean([p.consciousness_level for p in self.user_patterns.values()])),
                    resonance_frequency=avg_synchrony * 2.0,
                    field_coherence=self.consciousness_field.coherence_level
                )
                
                self.collective_insights.append(insight)
                
    def _detect_emergent_patterns(self):
        """Wykrywa emergentne wzorce w zachowaniach kolektywnych"""
        
        # Analiza rozkładu poziomów świadomości
        levels = [p.consciousness_level for p in self.user_patterns.values()]
        
        if len(levels) >= 5:
            # Wykryj czy grupa się "skupia" wokół określonych poziomów
            level_counts = {}
            for level in levels:
                level_counts[level] = level_counts.get(level, 0) + 1
            
            # Znajdź dominujące poziomy (więcej niż 30% grupy)
            dominant_levels = [level for level, count in level_counts.items() 
                             if count >= len(levels) * 0.3]
            
            if len(dominant_levels) == 1:  # Silna konwergencja
                insight = CollectiveInsight(
                    insight_id=str(uuid.uuid4()),
                    timestamp=datetime.now(),
                    insight_type=InsightType.EMERGENT_PATTERN,
                    participants=list(self.user_patterns.keys()),
                    pattern_description=f"Konwergencja świadomości na poziomie {dominant_levels[0]} - "
                                      f"{level_counts[dominant_levels[0]]}/{len(levels)} uczestników",
                    emergence_strength=level_counts[dominant_levels[0]] / len(levels),
                    collective_impact=0.7,
                    wisdom_level=dominant_levels[0],
                    resonance_frequency=self.consciousness_field.field_strength,
                    field_coherence=self.consciousness_field.coherence_level
                )
                
                self.collective_insights.append(insight)
                
    def _analyze_collective_wisdom(self):
        """Analizuje emergencję kolektywnej mądrości"""
        
        if len(self.user_patterns) < 7:  # Minimum dla analizy mądrości kolektywnej
            return
            
        # Kalkuluj wskaźniki mądrości kolektywnej
        avg_consciousness = statistics.mean([p.consciousness_level for p in self.user_patterns.values()])
        avg_complexity = statistics.mean([p.decision_complexity for p in self.user_patterns.values()])
        total_breakthroughs = sum([len(p.breakthrough_moments) for p in self.user_patterns.values()])
        
        # Mądrość kolektywna = funkcja świadomości, złożoności i przełomów
        collective_wisdom_score = (avg_consciousness * 0.4 + 
                                 avg_complexity * 0.3 + 
                                 min(total_breakthroughs / len(self.user_patterns), 10) * 0.3)
        
        # Jeśli osiągnięto wysoki poziom kolektywnej mądrości
        if collective_wisdom_score > 7.0:
            self.wisdom_crystallization_points.append(datetime.now())
            
            insight = CollectiveInsight(
                insight_id=str(uuid.uuid4()),
                timestamp=datetime.now(),
                insight_type=InsightType.WISDOM_EMERGENCE,
                participants=list(self.user_patterns.keys()),
                pattern_description=f"Krystalizacja kolektywnej mądrości - wynik: {collective_wisdom_score:.2f}/10",
                emergence_strength=min(collective_wisdom_score / 10.0, 1.0),
                collective_impact=0.9,
                wisdom_level=int(collective_wisdom_score),
                resonance_frequency=collective_wisdom_score / 5.0,
                field_coherence=self.consciousness_field.coherence_level
            )
            
            self.collective_insights.append(insight)
            
    def _update_global_metrics(self):
        """Aktualizuje globalne metryki ekosystemu"""
        
        if not self.user_patterns:
            return
            
        # Globalny poziom świadomości
        consciousness_levels = [p.consciousness_level for p in self.user_patterns.values()]
        self.global_consciousness_level = statistics.mean(consciousness_levels)
        
        # Kolektywny iloraz inteligencji
        complexities = [p.decision_complexity for p in self.user_patterns.values()]
        velocities = [p.growth_velocity for p in self.user_patterns.values()]
        
        avg_complexity = statistics.mean(complexities) if complexities else 0
        avg_velocity = statistics.mean(velocities) if velocities else 0
        
        self.collective_intelligence_quotient = (avg_complexity * avg_velocity * 
                                               self.consciousness_field.field_strength)
        
        # Indeks harmonii ekosystemu
        field_metrics = self.consciousness_field.calculate_field_metrics()
        self.ecosystem_harmony_index = (field_metrics["coherence_level"] * 0.4 +
                                      field_metrics["field_stability"] * 0.4 +
                                      min(field_metrics["active_nodes"] / 50.0, 1.0) * 0.2)
        
    def generate_collective_report(self) -> Dict:
        """Generuje raport o stanie kolektywnej świadomości"""
        
        # Ostatnie insights
        recent_insights = sorted(self.collective_insights, 
                               key=lambda x: x.timestamp, reverse=True)[:10]
        
        # Analiza trendów
        field_metrics = self.consciousness_field.calculate_field_metrics()
        
        # Top użytkownicy pod względem rozwoju
        top_users = sorted(self.user_patterns.values(), 
                          key=lambda x: x.consciousness_level + x.growth_velocity, 
                          reverse=True)[:5]
        
        return {
            "global_state": {
                "consciousness_level": self.global_consciousness_level,
                "intelligence_quotient": self.collective_intelligence_quotient,
                "harmony_index": self.ecosystem_harmony_index,
                "active_users": len(self.user_patterns),
                "total_insights": len(self.collective_insights)
            },
            
            "consciousness_field": field_metrics,
            
            "recent_insights": [
                {
                    "type": insight.insight_type.value,
                    "description": insight.pattern_description,
                    "participants": len(insight.participants),
                    "strength": insight.emergence_strength,
                    "impact": insight.collective_impact,
                    "wisdom_level": insight.wisdom_level,
                    "timestamp": insight.timestamp.isoformat()
                }
                for insight in recent_insights
            ],
            
            "top_contributors": [
                {
                    "user_id": user.user_id[:8] + "...",  # Anonimizacja
                    "consciousness_level": user.consciousness_level,
                    "growth_velocity": user.growth_velocity,
                    "breakthroughs": len(user.breakthrough_moments),
                    "connections": len(user.synergy_connections)
                }
                for user in top_users
            ],
            
            "ecosystem_trends": {
                "wisdom_crystallizations": len(self.wisdom_crystallization_points),
                "sync_events_24h": field_metrics["sync_events_24h"],
                "field_growth_rate": self._calculate_field_growth_rate(),
                "emergence_frequency": self._calculate_emergence_frequency()
            },
            
            "report_timestamp": datetime.now().isoformat()
        }
        
    def _calculate_field_growth_rate(self) -> float:
        """Kalkuluje tempo wzrostu pola świadomości"""
        if len(self.user_patterns) < 2:
            return 0.0
            
        # Prosty wskaźnik na podstawie liczby nowych użytkowników i ich rozwoju
        total_growth = sum([p.growth_velocity for p in self.user_patterns.values()])
        return total_growth / len(self.user_patterns)
        
    def _calculate_emergence_frequency(self) -> float:
        """Kalkuluje częstotliwość emergentnych zjawisk"""
        if not self.collective_insights:
            return 0.0
            
        # Liczba insights na dzień
        days_active = max((datetime.now() - self.activation_time).days, 1)
        return len(self.collective_insights) / days_active
        
    def export_collective_consciousness_data(self) -> Dict:
        """Eksportuje pełne dane kolektywnej świadomości"""
        return {
            "module_info": {
                "module_id": self.module_id,
                "activation_time": self.activation_time.isoformat(),
                "analysis_threshold": self.pattern_recognition_threshold,
                "sensitivity": self.emergence_detection_sensitivity
            },
            
            "consciousness_field_state": {
                "field_strength": self.consciousness_field.field_strength,
                "coherence_level": self.consciousness_field.coherence_level,
                "resonance_nodes": len(self.consciousness_field.resonance_nodes),
                "sync_events": [event.isoformat() for event in self.consciousness_field.sync_events]
            },
            
            "collective_insights_full": [
                {
                    "insight_id": insight.insight_id,
                    "timestamp": insight.timestamp.isoformat(),
                    "type": insight.insight_type.value,
                    "participants": insight.participants,
                    "description": insight.pattern_description,
                    "emergence_strength": insight.emergence_strength,
                    "collective_impact": insight.collective_impact,
                    "wisdom_level": insight.wisdom_level,
                    "resonance_frequency": insight.resonance_frequency,
                    "field_coherence": insight.field_coherence
                }
                for insight in self.collective_insights
            ],
            
            "user_patterns_summary": {
                user_id: {
                    "consciousness_level": pattern.consciousness_level,
                    "growth_velocity": pattern.growth_velocity,
                    "interaction_frequency": pattern.interaction_frequency,
                    "breakthrough_count": len(pattern.breakthrough_moments),
                    "connection_count": len(pattern.synergy_connections),
                    "dominant_emotions": list(pattern.emotional_profile.keys())[:3]
                }
                for user_id, pattern in self.user_patterns.items()
            },
            
            "global_metrics": {
                "global_consciousness_level": self.global_consciousness_level,
                "collective_intelligence_quotient": self.collective_intelligence_quotient,
                "ecosystem_harmony_index": self.ecosystem_harmony_index,
                "wisdom_crystallization_count": len(self.wisdom_crystallization_points)
            },
            
            "export_timestamp": datetime.now().isoformat()
        }

# Instancja globalna modułu kolektywnej świadomości
GLOBAL_VISION_MODULE = GlobalVisionModule()

def get_global_vision() -> GlobalVisionModule:
    """Zwraca globalną instancję modułu kolektywnej świadomości"""
    return GLOBAL_VISION_MODULE