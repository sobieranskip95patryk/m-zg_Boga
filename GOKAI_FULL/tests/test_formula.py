
from gokai.core.formula import GOKAIFormula

def test_S_positive():
    f = GOKAIFormula()
    assert f.S() > 0
