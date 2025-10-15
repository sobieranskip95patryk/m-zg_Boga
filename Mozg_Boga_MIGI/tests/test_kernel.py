import unittest
from core.kernel.AGI_Kernel import AGI_Kernel

class TestAGIKernel(unittest.TestCase):

    def setUp(self):
        self.kernel = AGI_Kernel()

    def test_initialization(self):
        self.assertIsNotNone(self.kernel)

    def test_decision_making(self):
        input_data = {"context": "test", "goal": "maximize efficiency"}
        decision = self.kernel.make_decision(input_data)
        self.assertIn("decision", decision)

    def test_audit_trail(self):
        input_data = {"context": "test", "goal": "minimize risk"}
        self.kernel.make_decision(input_data)
        audit_trail = self.kernel.get_audit_trail()
        self.assertGreater(len(audit_trail), 0)

    def test_adaptation(self):
        initial_weight = self.kernel.weights.copy()
        self.kernel.adapt_weights({"feedback": "positive"})
        self.assertNotEqual(initial_weight, self.kernel.weights)

if __name__ == '__main__':
    unittest.main()