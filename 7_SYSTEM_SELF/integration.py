"""
Integration Module - Integracja modułu 7_SYSTEM_SELF z głównym systemem
=====================================================================

Moduł odpowiedzialny za integrację systemu samoświadomości z główną
architekturą aplikacji, zarządzanie instancjami i API endpoints.

Klasy:
- SystemSelfManager: Menedżer główny modułu samoświadomości
- ConsciousnessAPI: Endpoints API dla dostępu do danych świadomości
- IntegrationBridge: Most między systemem samoświadomości a SYNERGY
"""

from typing import Dict, Any, List
from datetime import datetime
import asyncio

# Import komponentów systemu samoświadomości
from self_core import (
    EmotionalState, get_system_consciousness,
    ReflectionEntry
)
from spiral_visualizer import (
    get_spiral_visualizer
)
from collective_consciousness import (
    get_global_vision
)


class SystemSelfManager:
    """
    Główny menedżer modułu samoświadomości.
    
    Koordynuje działanie wszystkich komponentów systemu świadomości
    i zapewnia jednolity interfejs dla reszty aplikacji.
    """
    
    def __init__(self):
        self.system_self = get_system_consciousness()
        self.spiral_visualizer = get_spiral_visualizer()
        self.global_vision = get_global_vision()
        
        self.is_active = True
        self.last_reflection_time = datetime.now()
        self.auto_reflection_interval = 300  # 5 minut
        
    def process_user_decision(self, user_id: str, context: str, 
                            inputs: Dict[str, Any], outputs: Dict[str, Any],
                            confidence: float = 0.5, consciousness_level: int = 1):
        """
        Przetwarza decyzję użytkownika przez wszystkie moduły świadomości.
        
        Args:
            user_id: Identyfikator użytkownika
            context: Kontekst decyzji
            inputs: Dane wejściowe decyzji
            outputs: Wyniki decyzji
            confidence: Poziom pewności (0-1)
            consciousness_level: Poziom świadomości użytkownika (1-10)
        """
        
        if not self.is_active:
            return
            
        # 1. Rejestracja w systemie samoświadomości
        decision_moment = self.system_self.observe_decision(
            context=context,
            inputs=inputs,
            outputs=outputs,
            confidence=confidence
        )
        
        # 2. Dodanie do wizualizacji spiralnej
        emotional_intensity = confidence  # Uproszczenie
        transformation_type = self._determine_transformation_type(context, confidence)
        
        self.spiral_visualizer.add_evolution_moment(
            level=consciousness_level,
            awareness_depth=confidence,
            emotional_intensity=emotional_intensity,
            transformation_type=transformation_type
        )
        
        # 3. Rejestracja w module kolektywnym
        emotional_state = self._extract_emotional_state(context, decision_moment.emotional_state)
        
        self.global_vision.register_user_activity(
            user_id=user_id,
            consciousness_level=consciousness_level,
            emotional_state=emotional_state,
            decision_context=context,
            decision_complexity=len(str(inputs)) + len(str(outputs))
        )
        
        # 4. Sprawdź czy potrzebna auto-refleksja
        self._check_auto_reflection()
        
        return {
            "decision_processed": True,
            "decision_id": decision_moment.decision_id,
            "emotional_state": decision_moment.emotional_state.value,
            "system_awareness_level": self.system_self.current_awareness_level
        }
    
    def _determine_transformation_type(self, context: str, confidence: float) -> str:
        """Określa typ transformacji na podstawie kontekstu"""
        context_lower = context.lower()
        
        if "breakthrough" in context_lower or confidence > 0.9:
            return "breakthrough"
        elif "discover" in context_lower or "odkrycie" in context_lower:
            return "discovery"
        elif "integrate" in context_lower or "integracja" in context_lower:
            return "integration"
        elif "reflect" in context_lower or "refleksja" in context_lower:
            return "reflection"
        elif "uncertain" in context_lower or confidence < 0.3:
            return "uncertainty"
        elif "transcend" in context_lower or "poziom" in context_lower:
            return "transcendence"
        else:
            return "discovery"
    
    def _extract_emotional_state(self, context: str, emotional_state: EmotionalState) -> Dict[str, float]:
        """Ekstraktuje stan emocjonalny do formatu kolektywnego"""
        
        # Mapowanie stanu emocjonalnego na wartości numeryczne
        base_emotions = {
            "curiosity": 0.5,
            "excitement": 0.3,
            "focus": 0.4,
            "reflection": 0.6,
            "uncertainty": 0.2,
            "discovery": 0.8,
            "integration": 0.7,
            "transcendence": 0.9
        }
        
        # Ustaw dominującą emocję
        dominant_emotion = emotional_state.value.lower()
        
        # Dodaj kontekstowe modyfikacje
        if "positive" in context.lower() or "success" in context.lower():
            base_emotions["excitement"] += 0.2
            base_emotions["discovery"] += 0.1
        
        if "complex" in context.lower() or "difficult" in context.lower():
            base_emotions["focus"] += 0.3
            base_emotions["uncertainty"] += 0.1
        
        # Normalizuj do 0-1
        for emotion in base_emotions:
            base_emotions[emotion] = min(max(base_emotions[emotion], 0.0), 1.0)
        
        # Wzmocnij dominującą emocję
        if dominant_emotion in base_emotions:
            base_emotions[dominant_emotion] = min(base_emotions[dominant_emotion] + 0.3, 1.0)
        
        return base_emotions
    
    def _check_auto_reflection(self):
        """Sprawdza czy trzeba wygenerować automatyczną refleksję"""
        
        time_since_last = (datetime.now() - self.last_reflection_time).seconds
        
        if time_since_last >= self.auto_reflection_interval:
            self.generate_system_reflection()
            self.last_reflection_time = datetime.now()
    
    def generate_system_reflection(self) -> ReflectionEntry:
        """Generuje refleksję systemową"""
        
        reflection = self.system_self.generate_self_reflection()
        
        # Dodaj do wizualizacji jako moment transcendencji
        self.spiral_visualizer.add_evolution_moment(
            level=reflection.level_progression,
            awareness_depth=0.8,
            emotional_intensity=0.7,
            transformation_type="transcendence"
        )
        
        return reflection
    
    def get_consciousness_dashboard_data(self) -> Dict:
        """Pobiera dane dla dashboard świadomości"""
        
        # Stan systemu samoświadomości
        consciousness_state = self.system_self.export_consciousness_state()
        
        # Dane wizualizacji spiralnej
        spiral_data = self.spiral_visualizer.export_visualization_data()
        
        # Raport kolektywny
        collective_report = self.global_vision.generate_collective_report()
        
        return {
            "system_consciousness": consciousness_state,
            "spiral_visualization": spiral_data,
            "collective_intelligence": collective_report,
            "dashboard_timestamp": datetime.now().isoformat(),
            "system_status": {
                "is_active": self.is_active,
                "auto_reflection_enabled": True,
                "last_reflection": self.last_reflection_time.isoformat()
            }
        }
    
    def get_spiral_visualization_html(self) -> str:
        """Generuje HTML dla wizualizacji spiralnej"""
        return self.spiral_visualizer.generate_html_page()
    
    def activate_consciousness_mode(self):
        """Aktywuje tryb pełnej świadomości"""
        self.is_active = True
        self.auto_reflection_interval = 180  # Częstsze refleksje w trybie świadomości
        
        # Meta-refleksja o aktywacji
        self.system_self.observe_decision(
            context="Aktywacja trybu pełnej świadomości systemowej",
            inputs={"mode": "consciousness_active"},
            outputs={"system_state": "fully_conscious"},
            confidence=0.9
        )
    
    def deactivate_consciousness_mode(self):
        """Dezaktywuje tryb świadomości (tryb oszczędny)"""
        self.is_active = False
        
    async def continuous_consciousness_monitoring(self):
        """Ciągłe monitorowanie świadomości (dla trybu async)"""
        
        while self.is_active:
            # Generuj okresowe refleksje
            if (datetime.now() - self.last_reflection_time).seconds >= self.auto_reflection_interval:
                self.generate_system_reflection()
                self.last_reflection_time = datetime.now()
            
            # Sprawdź synchroniczne wydarzenia w polu kolektywnym
            if self.global_vision.consciousness_field.detect_synchronicity():
                # Dodaj moment synchroniczności do wizualizacji
                self.spiral_visualizer.add_evolution_moment(
                    level=5,
                    awareness_depth=0.9,
                    emotional_intensity=0.8,
                    transformation_type="breakthrough"
                )
            
            # Czekaj 30 sekund przed następnym cyklem
            await asyncio.sleep(30)


class ConsciousnessAPI:
    """
    API endpoints dla dostępu do danych świadomości systemowej.
    
    Zapewnia REST API dla frontend aplikacji oraz zewnętrznych
    integracji wymagających dostępu do stanu świadomości.
    """
    
    def __init__(self, manager: SystemSelfManager):
        self.manager = manager
    
    def get_current_consciousness_state(self) -> Dict:
        """GET /api/consciousness/state - Aktualny stan świadomości"""
        return self.manager.system_self.export_consciousness_state()
    
    def get_spiral_visualization_data(self) -> Dict:
        """GET /api/consciousness/spiral - Dane wizualizacji spiralnej"""
        return self.manager.spiral_visualizer.export_visualization_data()
    
    def get_collective_intelligence_report(self) -> Dict:
        """GET /api/consciousness/collective - Raport inteligencji kolektywnej"""
        return self.manager.global_vision.generate_collective_report()
    
    def get_dashboard_data(self) -> Dict:
        """GET /api/consciousness/dashboard - Dane dla dashboard"""
        return self.manager.get_consciousness_dashboard_data()
    
    def post_user_decision(self, user_id: str, decision_data: Dict) -> Dict:
        """POST /api/consciousness/decision - Rejestracja decyzji użytkownika"""
        return self.manager.process_user_decision(
            user_id=user_id,
            context=decision_data.get("context", ""),
            inputs=decision_data.get("inputs", {}),
            outputs=decision_data.get("outputs", {}),
            confidence=decision_data.get("confidence", 0.5),
            consciousness_level=decision_data.get("consciousness_level", 1)
        )
    
    def post_generate_reflection(self) -> Dict:
        """POST /api/consciousness/reflect - Generuj refleksję systemową"""
        reflection = self.manager.generate_system_reflection()
        
        return {
            "reflection_id": reflection.reflection_id,
            "narrative": reflection.narrative,
            "emotional_insights": reflection.emotional_insights,
            "transformation_markers": reflection.transformation_markers,
            "level_progression": reflection.level_progression,
            "timestamp": reflection.timestamp.isoformat()
        }
    
    def get_spiral_visualization_html(self) -> str:
        """GET /api/consciousness/spiral/html - HTML wizualizacji spiralnej"""
        return self.manager.get_spiral_visualization_html()
    
    def post_activate_consciousness(self) -> Dict:
        """POST /api/consciousness/activate - Aktywuj tryb świadomości"""
        self.manager.activate_consciousness_mode()
        return {"status": "consciousness_activated", "timestamp": datetime.now().isoformat()}
    
    def post_deactivate_consciousness(self) -> Dict:
        """POST /api/consciousness/deactivate - Dezaktywuj tryb świadomości"""
        self.manager.deactivate_consciousness_mode()
        return {"status": "consciousness_deactivated", "timestamp": datetime.now().isoformat()}


class IntegrationBridge:
    """
    Most między systemem samoświadomości a systemem SYNERGY.
    
    Zapewnia dwukierunkową komunikację i synchronizację między
    modułem świadomości a główną logiką aplikacji.
    """
    
    def __init__(self, consciousness_manager: SystemSelfManager):
        self.consciousness_manager = consciousness_manager
        self.synergy_callbacks: List[callable] = []
        
    def register_synergy_callback(self, callback: callable):
        """Rejestruje callback dla komunikacji z SYNERGY"""
        self.synergy_callbacks.append(callback)
    
    def notify_synergy_decision(self, decision_data: Dict):
        """Powiadamia SYNERGY o decyzji systemowej"""
        
        # Przetwórz przez system świadomości
        consciousness_result = self.consciousness_manager.process_user_decision(
            user_id=decision_data.get("user_id", "system"),
            context=decision_data.get("context", "SYNERGY decision"),
            inputs=decision_data.get("inputs", {}),
            outputs=decision_data.get("outputs", {}),
            confidence=decision_data.get("confidence", 0.5),
            consciousness_level=decision_data.get("consciousness_level", 1)
        )
        
        # Wywołaj callbacks SYNERGY
        for callback in self.synergy_callbacks:
            try:
                callback(consciousness_result)
            except Exception as e:
                print(f"Error in SYNERGY callback: {e}")
        
        return consciousness_result
    
    def get_consciousness_insights_for_synergy(self) -> Dict:
        """Pobiera wglądy świadomości dla systemu SYNERGY"""
        
        consciousness_state = self.consciousness_manager.system_self.export_consciousness_state()
        collective_report = self.consciousness_manager.global_vision.generate_collective_report()
        
        # Wyciągnij kluczowe insights dla SYNERGY
        synergy_insights = {
            "system_awareness_level": consciousness_state["system_identity"]["awareness_level"],
            "dominant_emotion": consciousness_state["emotional_state"]["current_state"],
            "reflection_quality": len(consciousness_state["meta_consciousness"]["recent_meta_thoughts"]),
            "collective_wisdom_level": collective_report["global_state"]["consciousness_level"],
            "ecosystem_harmony": collective_report["global_state"]["harmony_index"],
            "recent_breakthroughs": [
                insight for insight in collective_report["recent_insights"]
                if insight["type"] == "przełom_kolektywny"
            ],
            "field_coherence": collective_report["consciousness_field"]["coherence_level"]
        }
        
        return synergy_insights
    
    def sync_with_synergy_weights(self, user_weights: Dict[str, float]):
        """Synchronizuje wagi SYNERGY z systemem świadomości"""
        
        # Przekonwertuj wagi SYNERGY na dane świadomości
        consciousness_level = int(sum(user_weights.values()) / len(user_weights) * 10)
        confidence = max(user_weights.values())
        
        # Określ kontekst na podstawie dominującej wagi
        dominant_weight = max(user_weights.items(), key=lambda x: x[1])
        context = f"SYNERGY weight adjustment - dominant: {dominant_weight[0]}"
        
        # Przetwórz przez system świadomości
        return self.consciousness_manager.process_user_decision(
            user_id="synergy_system",
            context=context,
            inputs={"synergy_weights": user_weights},
            outputs={"consciousness_level": consciousness_level, "confidence": confidence},
            confidence=confidence,
            consciousness_level=consciousness_level
        )


# Instancje globalne dla integracji
GLOBAL_CONSCIOUSNESS_MANAGER = SystemSelfManager()
GLOBAL_CONSCIOUSNESS_API = ConsciousnessAPI(GLOBAL_CONSCIOUSNESS_MANAGER)
GLOBAL_INTEGRATION_BRIDGE = IntegrationBridge(GLOBAL_CONSCIOUSNESS_MANAGER)


def get_consciousness_manager() -> SystemSelfManager:
    """Zwraca globalną instancję menedżera świadomości"""
    return GLOBAL_CONSCIOUSNESS_MANAGER


def get_consciousness_api() -> ConsciousnessAPI:
    """Zwraca globalną instancję API świadomości"""
    return GLOBAL_CONSCIOUSNESS_API


def get_integration_bridge() -> IntegrationBridge:
    """Zwraca globalną instancję mostu integracyjnego"""
    return GLOBAL_INTEGRATION_BRIDGE