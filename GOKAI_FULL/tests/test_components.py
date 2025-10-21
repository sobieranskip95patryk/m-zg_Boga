
from gokai.core.intrinsic import IntrinsicValue
from gokai.core.skills import SkillValue
from gokai.core.decisions import DecisionValue
from gokai.core.context import ContextValue
from gokai.core.personality import PersonalityValue
from gokai.core.energy import EnergyValue
from gokai.core.time import TimeValue

def test_values():
    assert IntrinsicValue().value() == 7
    assert SkillValue().value() == 6
    assert DecisionValue().value() == 4
    assert ContextValue().value() == 5
    assert PersonalityValue().value() == 8
    assert EnergyValue().value() == 6
    assert TimeValue().value() == 3
