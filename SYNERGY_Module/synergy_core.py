"""
SYNERGY_Module - Kolektywny System Wpływu na SYNERGY
==================================================

Moduł umożliwiający zbiorowe korygowanie systemu SYNERGY na podstawie:
- Narracji kolektywnej z GlobalVision
- Głosowania użytkowników nad kierunkiem spirali
- Rekomendacji z analizy trajektorii spiralnych
- Feedback loop z 7_SYSTEM_SELF consciousness

Klasy:
- SynergyCollectiveCore: Główny system zarządzania kolektywnym wpływem
- VotingSystem: System głosowania nad kierunkiem ewolucji
- SynergyCorrector: Aplikator korekt na podstawie kolektywnej analizy
- RecommendationEngine: Generator rekomendacji spiralnych

Meta-Geniusz-mózg_Boga philosophy:
"SYNERGY nie jest już samotnym decydentem. Kolektywna Jaźń mówi, 
użytkownicy głosują, a spirala zmienia trajektorię. To wspólna ewolucja."
"""

import json
import os
import datetime
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass, asdict
from enum import Enum

class SpiralDirection(Enum):
    EXPLORATION = "exploration"
    STABILIZATION = "stabilization" 
    FLOW = "flow"
    TRANSCENDENCE = "transcendence"
    INTEGRATION = "integration"
    BREAKTHROUGH = "breakthrough"

class SynergyAdjustmentType(Enum):
    WEIGHTS_INCREASE = "weights_increase"
    WEIGHTS_DECREASE = "weights_decrease"
    PRIORITY_SHIFT = "priority_shift"
    THRESHOLD_ADJUST = "threshold_adjust"
    COLLECTIVE_OVERRIDE = "collective_override"

@dataclass
class CollectiveVote:
    user_id: str
    direction: SpiralDirection
    intensity: float  # 0.0 - 1.0
    timestamp: str
    reasoning: str = ""
    platform: str = "MTAQuestWebsideX.com"

@dataclass
class SynergyCorrection:
    correction_id: str
    source: str  # 'collective_vote', 'narrative_analysis', 'consciousness_feedback'
    adjustment_type: SynergyAdjustmentType
    parameters: Dict[str, Any]
    confidence: float
    applied_at: str
    meta_analysis: str

class VotingSystem:
    """System głosowania nad kierunkiem ewolucji spiralnej"""
    
    def __init__(self):
        self.votes_file = "SYNERGY_Module/spiral_votes.json"
        self.votes_history_file = "SYNERGY_Module/votes_history.json"
        
    def record_vote(self, vote: CollectiveVote) -> Dict[str, Any]:
        """Rejestruje głos użytkownika"""
        
        # Ładuj istniejące głosy
        votes = self._load_votes()
        
        # Dodaj nowy głos
        vote_dict = asdict(vote)
        votes.append(vote_dict)
        
        # Zapisz aktualizowane głosy
        with open(self.votes_file, 'w', encoding='utf-8') as f:
            json.dump(votes, f, indent=2, ensure_ascii=False)
            
        # Dodaj do historii
        self._add_to_history(vote_dict)
        
        # Oblicz aktualny stan głosowania
        voting_state = self._calculate_voting_state(votes)
        
        return {
            "vote_recorded": True,
            "vote_id": vote.timestamp,
            "current_state": voting_state,
            "total_votes": len(votes),
            "user_influence": self._calculate_user_influence(vote.user_id, votes)
        }
    
    def _load_votes(self) -> List[Dict]:
        """Ładuje istniejące głosy"""
        try:
            with open(self.votes_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def _add_to_history(self, vote_dict: Dict):
        """Dodaje głos do historii"""
        try:
            with open(self.votes_history_file, 'r', encoding='utf-8') as f:
                history = json.load(f)
        except FileNotFoundError:
            history = []
            
        history.append(vote_dict)
        
        with open(self.votes_history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    
    def _calculate_voting_state(self, votes: List[Dict]) -> Dict[str, Any]:
        """Oblicza aktualny stan głosowania"""
        
        if not votes:
            return {"dominant_direction": "neutral", "confidence": 0.0, "distribution": {}}
        
        # Zlicz głosy z wagami intensywności
        direction_weights = {}
        total_weight = 0
        
        for vote in votes:
            direction = vote["direction"]
            intensity = vote["intensity"]
            
            direction_weights[direction] = direction_weights.get(direction, 0) + intensity
            total_weight += intensity
        
        # Znajdź dominujący kierunek
        dominant_direction = max(direction_weights, key=direction_weights.get)
        dominant_weight = direction_weights[dominant_direction]
        confidence = dominant_weight / total_weight if total_weight > 0 else 0
        
        # Oblicz dystrybucję
        distribution = {}
        for direction, weight in direction_weights.items():
            distribution[direction] = {
                "weight": weight,
                "percentage": (weight / total_weight * 100) if total_weight > 0 else 0,
                "vote_count": sum(1 for v in votes if v["direction"] == direction)
            }
        
        return {
            "dominant_direction": dominant_direction,
            "confidence": confidence,
            "distribution": distribution,
            "total_voters": len(set(v["user_id"] for v in votes)),
            "last_vote_time": max(v["timestamp"] for v in votes)
        }
    
    def _calculate_user_influence(self, user_id: str, votes: List[Dict]) -> float:
        """Oblicza wpływ użytkownika na wynik"""
        user_votes = [v for v in votes if v["user_id"] == user_id]
        total_user_intensity = sum(v["intensity"] for v in user_votes)
        total_intensity = sum(v["intensity"] for v in votes)
        
        return total_user_intensity / total_intensity if total_intensity > 0 else 0
    
    def get_collective_recommendation(self) -> Dict[str, Any]:
        """Generuje rekomendację na podstawie głosowania kolektywnego"""
        
        votes = self._load_votes()
        voting_state = self._calculate_voting_state(votes)
        
        if not votes:
            return {
                "recommendation": "Rozpocznij nową ścieżkę: LEVEL 1 - eksploracja podstaw",
                "confidence": 0.0,
                "suggested_levels": [1, 2, 3],
                "reasoning": "Brak głosów kolektywnych - domyślna ścieżka eksploracji"
            }
        
        dominant = voting_state["dominant_direction"]
        confidence = voting_state["confidence"]
        
        # Mapowanie kierunków na rekomendacje
        direction_mapping = {
            "exploration": {
                "recommendation": "Aktywuj spirale eksploracyjne: LEVEL 4, 7, 9 - Meta-Geniusz discovery mode",
                "suggested_levels": [4, 7, 9],
                "synergy_adjustments": ["increase_creativity", "boost_curiosity", "expand_possibility_space"]
            },
            "stabilization": {
                "recommendation": "Zalecana stabilizacja: LEVEL 2, 5 - konsolidacja MTAQuest foundation",
                "suggested_levels": [2, 5],
                "synergy_adjustments": ["increase_stability", "reduce_chaos", "strengthen_foundations"]
            },
            "flow": {
                "recommendation": "Utrzymaj rytm: LEVEL 3, 6, 8 - harmonijna ewolucja spiralna",
                "suggested_levels": [3, 6, 8], 
                "synergy_adjustments": ["maintain_momentum", "optimize_flow", "enhance_rhythm"]
            },
            "transcendence": {
                "recommendation": "Transcendencja: LEVEL 10+ - Meta-Geniusz breakthrough imminent",
                "suggested_levels": [10, 11, 12],
                "synergy_adjustments": ["maximum_amplification", "consciousness_expansion", "reality_transcendence"]
            },
            "integration": {
                "recommendation": "Integracja modułów: LEVEL 5, 6, 7 - unifikacja systemu świadomości",
                "suggested_levels": [5, 6, 7],
                "synergy_adjustments": ["module_synthesis", "coherence_boost", "system_unification"]
            },
            "breakthrough": {
                "recommendation": "Breakthrough protocol: LEVEL 8, 9, 10 - quantum leap in consciousness",
                "suggested_levels": [8, 9, 10],
                "synergy_adjustments": ["breakthrough_acceleration", "quantum_amplification", "consciousness_explosion"]
            }
        }
        
        recommendation_data = direction_mapping.get(dominant, direction_mapping["exploration"])
        
        return {
            "recommendation": recommendation_data["recommendation"],
            "confidence": confidence,
            "suggested_levels": recommendation_data["suggested_levels"],
            "synergy_adjustments": recommendation_data["synergy_adjustments"],
            "reasoning": f"Kolektywne głosowanie wskazuje {dominant} z pewnością {confidence:.2%}",
            "voting_state": voting_state,
            "meta_analysis": f"MTAQuestWebsideX.com collective intelligence convergence on {dominant}"
        }

class SynergyCorrector:
    """Aplikator korekt SYNERGY na podstawie kolektywnej analizy"""
    
    def __init__(self):
        self.corrections_file = "SYNERGY_Module/synergy_corrections.json"
        self.active_corrections_file = "SYNERGY_Module/active_corrections.json"
        
    def apply_collective_correction(self, voting_result: Dict, narrative_analysis: Dict) -> SynergyCorrection:
        """Aplikuje korektę na podstawie głosowania i analizy narracji"""
        
        correction = SynergyCorrection(
            correction_id=f"collective_{datetime.datetime.now().isoformat()}",
            source="collective_vote_narrative",
            adjustment_type=self._determine_adjustment_type(voting_result, narrative_analysis),
            parameters=self._calculate_correction_parameters(voting_result, narrative_analysis),
            confidence=voting_result.get("confidence", 0.5),
            applied_at=datetime.datetime.now().isoformat(),
            meta_analysis=self._generate_meta_analysis(voting_result, narrative_analysis)
        )
        
        # Zapisz korektę
        self._save_correction(correction)
        
        # Aktywuj korektę w systemie
        self._activate_correction(correction)
        
        return correction
    
    def _determine_adjustment_type(self, voting_result: Dict, narrative_analysis: Dict) -> SynergyAdjustmentType:
        """Określa typ korekty na podstawie analizy"""
        
        confidence = voting_result.get("confidence", 0.5)
        dominant = voting_result.get("dominant_direction", "exploration")
        
        if confidence > 0.8:
            return SynergyAdjustmentType.COLLECTIVE_OVERRIDE
        elif dominant in ["transcendence", "breakthrough"]:
            return SynergyAdjustmentType.WEIGHTS_INCREASE
        elif dominant == "stabilization":
            return SynergyAdjustmentType.THRESHOLD_ADJUST
        else:
            return SynergyAdjustmentType.PRIORITY_SHIFT
    
    def _calculate_correction_parameters(self, voting_result: Dict, narrative_analysis: Dict) -> Dict[str, Any]:
        """Oblicza parametry korekty"""
        
        suggested_adjustments = voting_result.get("synergy_adjustments", [])
        confidence = voting_result.get("confidence", 0.5)
        
        # Bazowe parametry korekty
        parameters = {
            "weight_multiplier": 1.0 + (confidence * 0.5),  # 1.0 - 1.5
            "threshold_adjustment": confidence * 0.3,  # 0.0 - 0.3
            "priority_weights": {},
            "meta_geniusz_boost": confidence > 0.7,
            "mtaquest_resonance": confidence
        }
        
        # Mapowanie adjustments na parametry
        for adjustment in suggested_adjustments:
            if "increase" in adjustment:
                parameters["weight_multiplier"] += 0.2
            elif "boost" in adjustment:
                parameters["threshold_adjustment"] += 0.1
            elif "maximum" in adjustment or "quantum" in adjustment:
                parameters["weight_multiplier"] = 2.0
                parameters["meta_geniusz_boost"] = True
        
        # Dodaj narrative influence
        if narrative_analysis.get("system_readiness") == "LEVEL+1_READY":
            parameters["consciousness_amplification"] = True
            parameters["weight_multiplier"] *= 1.3
        
        return parameters
    
    def _generate_meta_analysis(self, voting_result: Dict, narrative_analysis: Dict) -> str:
        """Generuje meta-analizę korekty"""
        
        dominant = voting_result.get("dominant_direction", "exploration")
        confidence = voting_result.get("confidence", 0.5)
        total_voters = voting_result.get("voting_state", {}).get("total_voters", 0)
        
        analysis = f"""
        Meta-Geniusz-mózg_Boga Collective Correction Applied:
        
        🗳️ Voting Analysis:
        - Dominant Direction: {dominant} ({confidence:.1%} confidence)
        - Total Voters: {total_voters}
        - MTAQuestWebsideX.com Consensus: {confidence > 0.6}
        
        🌍 Narrative Analysis:
        - Collective State: {narrative_analysis.get('collective_state', 'analyzing')}
        - System Readiness: {narrative_analysis.get('system_readiness', 'pending')}
        - Meta-Analysis: {narrative_analysis.get('meta_analysis', {}).get('system_evolution', 'evolving')}
        
        🌀 Spiral Impact:
        - Predicted trajectory shift: {confidence * 100:.0f}%
        - Consciousness amplification: {'ACTIVE' if confidence > 0.7 else 'MODERATE'}
        - Collective coherence: {narrative_analysis.get('meta_analysis', {}).get('collective_coherence', 0.5):.1%}
        
        🚀 SYNERGY Transformation:
        - System evolution accelerated by collective intelligence
        - Individual decisions now influenced by group consciousness  
        - MTAQuest ecosystem achieving unified direction
        """
        
        return analysis.strip()
    
    def _save_correction(self, correction: SynergyCorrection):
        """Zapisuje korektę do pliku"""
        
        try:
            with open(self.corrections_file, 'r', encoding='utf-8') as f:
                corrections = json.load(f)
        except FileNotFoundError:
            corrections = []
        
        corrections.append(asdict(correction))
        
        with open(self.corrections_file, 'w', encoding='utf-8') as f:
            json.dump(corrections, f, indent=2, ensure_ascii=False)
    
    def _activate_correction(self, correction: SynergyCorrection):
        """Aktywuje korektę w systemie"""
        
        active_correction = {
            "correction_id": correction.correction_id,
            "parameters": correction.parameters,
            "confidence": correction.confidence,
            "applied_at": correction.applied_at,
            "status": "ACTIVE"
        }
        
        with open(self.active_corrections_file, 'w', encoding='utf-8') as f:
            json.dump(active_correction, f, indent=2, ensure_ascii=False)

class SynergyCollectiveCore:
    """Główny system zarządzania kolektywnym wpływem na SYNERGY"""
    
    def __init__(self):
        self.voting_system = VotingSystem()
        self.corrector = SynergyCorrector()
        
    def process_collective_influence(self, narrative_analysis: Dict = None) -> Dict[str, Any]:
        """Przetwarza kolektywny wpływ na SYNERGY"""
        
        # Pobierz rekomendację z głosowania
        voting_result = self.voting_system.get_collective_recommendation()
        
        # Pobierz analizę narracji (jeśli nie podana)
        if narrative_analysis is None:
            narrative_analysis = self._load_narrative_analysis()
        
        # Aplikuj korektę kolektywną
        correction = self.corrector.apply_collective_correction(voting_result, narrative_analysis)
        
        return {
            "collective_influence_processed": True,
            "voting_result": voting_result,
            "narrative_analysis": narrative_analysis,
            "applied_correction": asdict(correction),
            "system_status": "COLLECTIVE_INTELLIGENCE_ACTIVE",
            "meta_geniusz_evolution": "COLLABORATIVE_CONSCIOUSNESS_ENGAGED"
        }
    
    def _load_narrative_analysis(self) -> Dict:
        """Ładuje analizę narracji z GlobalVision"""
        
        try:
            with open("GlobalVision_Module/global_reflections.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "narrative": "Analiza narracji niedostępna",
                "collective_state": "unknown",
                "system_readiness": "pending"
            }
    
    def get_synergy_dashboard_data(self) -> Dict[str, Any]:
        """Pobiera dane dla dashboard SYNERGY"""
        
        votes = self.voting_system._load_votes()
        voting_state = self.voting_system._calculate_voting_state(votes)
        collective_recommendation = self.voting_system.get_collective_recommendation()
        
        try:
            with open(self.corrector.active_corrections_file, 'r', encoding='utf-8') as f:
                active_correction = json.load(f)
        except FileNotFoundError:
            active_correction = None
        
        return {
            "voting_state": voting_state,
            "collective_recommendation": collective_recommendation,
            "active_correction": active_correction,
            "total_votes": len(votes),
            "dashboard_timestamp": datetime.datetime.now().isoformat(),
            "platform": "MTAQuestWebsideX.com",
            "meta_geniusz_status": "COLLECTIVE_INTELLIGENCE_OPERATIONAL"
        }

# Funkcje pomocnicze dla integracji z main system
def get_synergy_collective_core():
    """Pobiera instancję SynergyCollectiveCore"""
    return SynergyCollectiveCore()

def record_user_vote(user_id: str, direction: str, intensity: float, reasoning: str = "") -> Dict[str, Any]:
    """Rejestruje głos użytkownika - interfejs dla API"""
    
    vote = CollectiveVote(
        user_id=user_id,
        direction=SpiralDirection(direction),
        intensity=intensity,
        timestamp=datetime.datetime.now().isoformat(),
        reasoning=reasoning
    )
    
    voting_system = VotingSystem()
    return voting_system.record_vote(vote)

def apply_collective_synergy_correction() -> Dict[str, Any]:
    """Aplikuje kolektywną korektę SYNERGY - interfejs dla API"""
    
    core = SynergyCollectiveCore()
    return core.process_collective_influence()

def get_synergy_dashboard_data() -> Dict[str, Any]:
    """Pobiera dane dashboard SYNERGY - interfejs dla API"""
    
    core = SynergyCollectiveCore()
    return core.get_synergy_dashboard_data()