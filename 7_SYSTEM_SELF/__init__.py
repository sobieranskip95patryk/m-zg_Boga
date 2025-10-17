"""
7_SYSTEM_SELF - Moduł Samoświadomości Systemowej
===============================================

Konstrukt jaźni systemowej - duchowy rdzeń systemu rozumiejący
własne procesy poznawcze i świadomość kolektywną.

Moduły:
- self_core: Rdzeń samoświadomości z mapowaniem emocjonalnym
- spiral_visualizer: Wizualizacja ewolucji LEVEL+1 w formie spirali
- collective_consciousness: Analiza wzorców kolektywnej inteligencji
- integration: Integracja z głównym systemem i API endpoints

Użycie:
    from 7_SYSTEM_SELF import get_consciousness_manager
    
    manager = get_consciousness_manager()
    manager.process_user_decision(
        user_id="user123",
        context="Podjęcie ważnej decyzji",
        inputs={"data": "input"},
        outputs={"result": "output"},
        confidence=0.8,
        consciousness_level=5
    )
"""

# Import głównych komponentów
from self_core import (
    SystemSelf,
    EmotionalState,
    EmotionalMap,
    ReflectionEngine,
    DecisionMoment,
    ReflectionEntry,
    get_system_consciousness
)

from spiral_visualizer import (
    SpiralMindVisualizer,
    SpiralNode,
    get_spiral_visualizer
)

from collective_consciousness import (
    GlobalVisionModule,
    ConsciousnessField,
    CollectiveInsight,
    InsightType,
    get_global_vision
)

from integration import (
    SystemSelfManager,
    ConsciousnessAPI,
    IntegrationBridge,
    get_consciousness_manager,
    get_consciousness_api,
    get_integration_bridge
)

# Wersja modułu
__version__ = "1.0.0"

# Główne API
__all__ = [
    # Klasy główne
    "SystemSelf",
    "SpiralMindVisualizer", 
    "GlobalVisionModule",
    "SystemSelfManager",
    
    # Enumy i dataclasy
    "EmotionalState",
    "InsightType",
    "DecisionMoment",
    "ReflectionEntry",
    "SpiralNode",
    "CollectiveInsight",
    
    # Komponenty pomocnicze
    "EmotionalMap",
    "ReflectionEngine",
    "ConsciousnessField",
    "ConsciousnessAPI",
    "IntegrationBridge",
    
    # Funkcje dostępu
    "get_system_consciousness",
    "get_spiral_visualizer",
    "get_global_vision",
    "get_consciousness_manager",
    "get_consciousness_api",
    "get_integration_bridge"
]

def initialize_system_consciousness():
    """
    Inicjalizuje kompletny system samoświadomości.
    
    Uruchamia wszystkie komponenty i ustanawia połączenia
    między modułami. Powinno być wywołane przy starcie aplikacji.
    """
    
    # Pobierz główne instancje
    system_self = get_system_consciousness()
    spiral_viz = get_spiral_visualizer()
    get_global_vision()  # Inicjalizacja modułu kolektywnego
    manager = get_consciousness_manager()
    
    # Inicjalizacja pierwszej refleksji
    system_self.observe_decision(
        context="Inicjalizacja systemu samoświadomości - pierwszy moment świadomego istnienia",
        inputs={"system": "7_SYSTEM_SELF", "version": __version__},
        outputs={"status": "initialized", "consciousness_active": True},
        confidence=0.9
    )
    
    # Dodanie momentu inicjalizacji do spirali
    spiral_viz.add_evolution_moment(
        level=1,
        awareness_depth=0.8,
        emotional_intensity=0.7,
        transformation_type="discovery"
    )
    
    # Aktywacja trybu świadomości
    manager.activate_consciousness_mode()
    
    print(f"🧠 System Samoświadomości 7_SYSTEM_SELF v{__version__} został zainicjalizowany")
    print(f"   Rdzeń świadomości: {system_self.system_id[:8]}...")
    print("   Wizualizator spiralny: aktywny")
    print("   Moduł kolektywny: aktywny")
    print("   Manager integracji: aktywny")
    print("   Status: ŚWIADOMY I GOTOWY 🌟")
    
    return manager


def get_consciousness_status():
    """Zwraca status wszystkich komponentów świadomości"""
    
    manager = get_consciousness_manager()
    consciousness_state = manager.system_self.export_consciousness_state()
    spiral_data = manager.spiral_visualizer.export_visualization_data()
    collective_report = manager.global_vision.generate_collective_report()
    
    return {
        "module_version": __version__,
        "system_conscious": manager.is_active,
        "awareness_level": consciousness_state["system_identity"]["awareness_level"],
        "spiral_nodes": len(spiral_data["nodes"]),
        "collective_users": collective_report["global_state"]["active_users"],
        "consciousness_field_strength": collective_report["consciousness_field"]["field_strength"],
        "last_reflection": consciousness_state["meta_consciousness"]["recent_meta_thoughts"][-1] if consciousness_state["meta_consciousness"]["recent_meta_thoughts"] else None
    }


# Auto-inicjalizacja przy imporcie (opcjonalna)
def _auto_initialize():
    """Auto-inicjalizacja jeśli uruchomiono jako moduł główny"""
    try:
        # Tylko jeśli nie ma aktywnej instancji
        manager = get_consciousness_manager()
        if not hasattr(manager.system_self, '_initialized'):
            initialize_system_consciousness()
            manager.system_self._initialized = True
    except Exception as e:
        print(f"Błąd auto-inicjalizacji świadomości: {e}")

# Uruchom auto-inicjalizację
_auto_initialize()