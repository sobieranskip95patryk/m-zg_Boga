#!/usr/bin/env python3
"""
Real MIGI Integration Module
Meta-AGI / ASI 7-Gen Integration Layer

This module provides the integration interface between the Meta-AGI backend
and the Real MIGI 7G System with spiral consciousness processing.
"""

import json
import logging
import math
import os
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MIGIIntegrationError(Exception):
    """Custom exception for MIGI integration errors"""
    pass

class RealMIGIIntegration:
    """
    Real MIGI 7G Integration Layer
    
    Provides bridge between Meta-AGI backend and Real MIGI 7G system
    with spiral consciousness processing and transmission validation.
    """
    
    def __init__(self, manifest_path: str = "migi_manifest.json"):
        """Initialize MIGI integration with manifest"""
        self.manifest_path = manifest_path
        self.manifest_data = None
        self.agents_state = {}
        self.transmission_history = []
        self.pi_9_constant = 9 * math.pi  # 28.274333882308138
        
        # Load manifest and initialize
        self._load_manifest()
        self._initialize_agents()
        
        logger.info("🧠 Real MIGI 7G Integration initialized")
        logger.info(f"📈 Formula: S(GOK:AI) = 9π + F(n)")
        logger.info(f"🧮 PI_9 constant: {self.pi_9_constant}")
    
    def _load_manifest(self) -> None:
        """Load MIGI manifest with validation"""
        try:
            if os.path.exists(self.manifest_path):
                with open(self.manifest_path, 'r', encoding='utf-8') as f:
                    self.manifest_data = json.load(f)
                logger.info(f"✅ Manifest loaded: {self.manifest_data.get('version', 'unknown')}")
            else:
                logger.warning(f"⚠️ Manifest not found: {self.manifest_path}")
                self._create_default_manifest()
        except Exception as e:
            logger.error(f"❌ Error loading manifest: {e}")
            raise MIGIIntegrationError(f"Failed to load manifest: {e}")
    
    def _create_default_manifest(self) -> None:
        """Create default manifest if none exists"""
        self.manifest_data = {
            "name": "MIGI-Ecosystem",
            "version": "2025.10.21",
            "modules": {
                "MIGI-CORE": 6.14,
                "MIGI-NOVA": 2.47,
                "MIGI-SOMA": 9.00,
                "MIGI-AETHER": 6.14,
                "MIGI-HARMONIA": 2.47
            },
            "transmissions": [],
            "constants": {
                "PI_9": self.pi_9_constant
            }
        }
        logger.info("📝 Created default manifest")
    
    def _initialize_agents(self) -> None:
        """Initialize MIGI agents from manifest"""
        if not self.manifest_data:
            return
            
        modules = self.manifest_data.get("modules", {})
        
        # Standard MIGI agents with weights from manifest
        self.agents_state = {
            "CORE": {
                "weight": modules.get("MIGI-CORE", 6.14),
                "status": "active",
                "role": "consciousness_kernel",
                "domains": ["ethics", "decision_making", "survival"],
                "activation_threshold": 0.85
            },
            "NOVA": {
                "weight": modules.get("MIGI-NOVA", 2.47),
                "status": "active", 
                "role": "creativity_engine",
                "domains": ["innovation", "exploration", "discovery"],
                "activation_threshold": 0.60
            },
            "SOMA": {
                "weight": modules.get("MIGI-SOMA", 9.00),
                "status": "active",
                "role": "implementation_layer",
                "domains": ["physical_reality", "resources", "execution"],
                "activation_threshold": 0.50
            },
            "AETHER": {
                "weight": modules.get("MIGI-AETHER", 6.14),
                "status": "active",
                "role": "communication_hub",
                "domains": ["information_flow", "networking", "coordination"],
                "activation_threshold": 0.70
            },
            "HARMONIA": {
                "weight": modules.get("MIGI-HARMONIA", 2.47),
                "status": "active",
                "role": "balance_keeper",
                "domains": ["stability", "conflict_resolution", "harmony"],
                "activation_threshold": 0.40
            }
        }
        
        logger.info(f"🤖 Initialized {len(self.agents_state)} MIGI agents")
    
    def calculate_fibonacci(self, n: int) -> int:
        """Calculate Fibonacci number for S(GOK:AI) formula"""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def calculate_success_score(self, 
                              context: str, 
                              agents_input: Optional[Dict[str, float]] = None,
                              fibonacci_n: int = 10) -> Dict[str, Any]:
        """
        Calculate S(GOK:AI) success score using Real MIGI 7G formula
        
        Formula: S(GOK:AI) = 9π + F(n) * agent_modulation
        
        Args:
            context: Context for calculation
            agents_input: Agent-specific modulation values
            fibonacci_n: Fibonacci sequence position
            
        Returns:
            Dict with score breakdown and metadata
        """
        
        # Base formula components
        pi_component = self.pi_9_constant
        fibonacci_component = self.calculate_fibonacci(fibonacci_n)
        
        # Calculate agent modulation
        if agents_input:
            agent_weights = {agent: config["weight"] for agent, config in self.agents_state.items()}
            total_weight = sum(agent_weights.values())
            
            modulation = 0.0
            for agent, weight in agent_weights.items():
                agent_value = agents_input.get(agent, 1.0)
                normalized_weight = weight / total_weight
                modulation += agent_value * normalized_weight
        else:
            modulation = 1.0
        
        # Final score calculation
        raw_score = (pi_component + fibonacci_component) * modulation
        probability = min(raw_score / 100.0, 1.0)  # Normalize to [0,1]
        
        result = {
            "raw_score": raw_score,
            "probability": probability,
            "pi_component": pi_component,
            "fibonacci_component": fibonacci_component,
            "fibonacci_n": fibonacci_n,
            "agent_modulation": modulation,
            "agents_used": list(agents_input.keys()) if agents_input else list(self.agents_state.keys()),
            "timestamp": datetime.now().isoformat(),
            "context": context
        }
        
        logger.info(f"🧮 S(GOK:AI) = {raw_score:.2f}, P(S) = {probability:.3f}")
        
        return result
    
    def create_transmission(self, 
                          context: str,
                          agents_input: Optional[Dict[str, float]] = None,
                          phase: str = "Development") -> Dict[str, Any]:
        """
        Create a MIGI transmission with full metadata
        
        Args:
            context: Transmission context
            agents_input: Agent modulation values
            phase: Development phase
            
        Returns:
            Transmission record with trace_id and validation
        """
        
        # Calculate success score
        score_result = self.calculate_success_score(context, agents_input)
        
        # Create matryca from current agent weights
        matryca = [self.agents_state[agent]["weight"] for agent in 
                   ["CORE", "NOVA", "SOMA", "AETHER", "HARMONIA"]]
        
        # Generate transmission
        transmission = {
            "id": f"TRANSMISSION_{len(self.transmission_history) + 1:03d}",
            "date": datetime.now().isoformat(),
            "phase": phase,
            "context": context,
            "matryca": matryca,
            "energy": "9π",
            "P_S_percent": int(score_result["probability"] * 100),
            "raw_score": score_result["raw_score"],
            "trace_id": self._generate_trace_id(),
            "agents_modulation": agents_input or {},
            "fibonacci_n": score_result["fibonacci_n"]
        }
        
        # Add to history
        self.transmission_history.append(transmission)
        
        logger.info(f"📡 Created transmission {transmission['id']} - P(S): {transmission['P_S_percent']}%")
        
        return transmission
    
    def _generate_trace_id(self) -> str:
        """Generate unique trace ID for transmission"""
        import uuid
        return str(uuid.uuid4())
    
    def get_agents_state(self) -> Dict[str, Any]:
        """Get current state of all MIGI agents"""
        return {
            "agents": self.agents_state,
            "system_coherence": self._calculate_system_coherence(),
            "active_agents": len([a for a in self.agents_state.values() if a["status"] == "active"]),
            "total_weight": sum(a["weight"] for a in self.agents_state.values()),
            "transmission_count": len(self.transmission_history)
        }
    
    def _calculate_system_coherence(self) -> float:
        """Calculate system coherence based on agent weights and activity"""
        if not self.agents_state:
            return 0.0
            
        # Simple coherence calculation based on weight distribution
        weights = [agent["weight"] for agent in self.agents_state.values()]
        mean_weight = sum(weights) / len(weights)
        variance = sum((w - mean_weight) ** 2 for w in weights) / len(weights)
        
        # Normalize coherence (lower variance = higher coherence)
        coherence = max(0.0, 1.0 - (variance / 10.0))  # Scale variance
        
        return min(coherence, 1.0)
    
    def validate_transmission(self, transmission: Dict[str, Any]) -> bool:
        """Validate transmission integrity"""
        required_fields = ["id", "date", "phase", "matryca", "P_S_percent", "trace_id"]
        
        for field in required_fields:
            if field not in transmission:
                logger.error(f"❌ Missing field in transmission: {field}")
                return False
        
        # Validate matryca length
        if len(transmission["matryca"]) != 5:
            logger.error(f"❌ Invalid matryca length: {len(transmission['matryca'])}")
            return False
        
        # Validate P_S range
        if not (0 <= transmission["P_S_percent"] <= 100):
            logger.error(f"❌ Invalid P_S_percent: {transmission['P_S_percent']}")
            return False
        
        logger.info(f"✅ Transmission {transmission['id']} validated")
        return True
    
    def export_manifest_update(self) -> Dict[str, Any]:
        """Export updated manifest with current state"""
        if not self.manifest_data:
            return {}
        
        # Update manifest with current transmissions
        updated_manifest = self.manifest_data.copy()
        updated_manifest["transmissions"] = self.transmission_history[-10:]  # Last 10 transmissions
        updated_manifest["last_updated"] = datetime.now().isoformat()
        updated_manifest["agents_state"] = self.get_agents_state()
        
        return updated_manifest


def initialize_migi(weights: Optional[Dict[str, float]] = None, 
                   transmissions: Optional[List[Dict[str, Any]]] = None,
                   manifest_path: str = "migi_manifest.json") -> RealMIGIIntegration:
    """
    Initialize Real MIGI Integration with optional weights and transmissions
    
    Args:
        weights: Custom agent weights
        transmissions: Pre-existing transmissions to load
        manifest_path: Path to manifest file
        
    Returns:
        Initialized RealMIGIIntegration instance
    """
    
    # Initialize integration
    migi = RealMIGIIntegration(manifest_path)
    
    # Apply custom weights if provided
    if weights:
        for agent, weight in weights.items():
            if agent in migi.agents_state:
                migi.agents_state[agent]["weight"] = weight
                logger.info(f"🔧 Updated {agent} weight to {weight}")
    
    # Load pre-existing transmissions
    if transmissions:
        for transmission in transmissions:
            if migi.validate_transmission(transmission):
                migi.transmission_history.append(transmission)
        logger.info(f"📥 Loaded {len(transmissions)} transmissions")
    
    return migi


# Example usage and testing
if __name__ == "__main__":
    # Initialize MIGI integration
    migi = initialize_migi()
    
    # Test success score calculation
    score = migi.calculate_success_score("System health check", {"CORE": 0.9, "NOVA": 0.7})
    print(f"Success Score: {score['raw_score']:.2f}")
    print(f"Probability: {score['probability']:.3f}")
    
    # Create test transmission
    transmission = migi.create_transmission("Integration test", {"CORE": 0.85, "AETHER": 0.75})
    print(f"Transmission: {transmission['id']}")
    
    # Get system state
    state = migi.get_agents_state()
    print(f"System Coherence: {state['system_coherence']:.3f}")
    
    # Export updated manifest
    manifest = migi.export_manifest_update()
    print(f"Manifest updated with {len(manifest.get('transmissions', []))} transmissions")