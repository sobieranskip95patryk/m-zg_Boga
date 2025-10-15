import unittest
import numpy as np
from src.pipeline import calculate_S_dec, assess_phase, PsycheNet, fitness
from src.utils import process_input, get_weights

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.data = [7, 6, 5, 4, 8, 6, 0.5, 0.6, 0.4, 0.5]
        self.inputs = [7/8, 6/8, 5/8, 4/8, 8/8, 6/8, 0.5]  # Znormalizowane
        self.env_factors = [0.6/0.6, 0.4/0.6, 0.5/0.6]
        self.T = 0.5
        self.net = PsycheNet()

    def test_process_input(self):
        result = process_input(data=self.data)
        self.assertEqual(len(result['inputs']), 7)
        self.assertEqual(len(result['env_factors']), 3)
        self.assertTrue(all(0 <= x <= 1 for x in result['inputs']))
        with self.assertRaises(ValueError):
            process_input(data=[-1, 6, 5, 4, 8, 6, 0.5, 0.6, 0.4, 0.5])

    def test_get_weights(self):
        weights = get_weights(self.T, variant='linear')
        self.assertEqual(len(weights), 5)
        self.assertAlmostEqual(sum(weights), 1.0, places=5)
        weights_sin = get_weights(self.T, variant='sinusoidal')
        self.assertEqual(len(weights_sin), 5)
        self.assertAlmostEqual(sum(weights_sin), 1.0, places=5)

    def test_calculate_S_dec(self):
        S_dec = calculate_S_dec(self.inputs, self.T, self.env_factors)
        self.assertGreater(S_dec, 0)
        self.assertLess(S_dec, 100)

    def test_assess_phase(self):
        S_dec = calculate_S_dec(self.inputs, self.T, self.env_factors)
        phase = assess_phase(S_dec, self.T)
        self.assertIn(phase, ["Destrukcja", "Punkt 0", "Rozwój"])

    def test_fitness_range(self):
        p_s = fitness(self.net, self.inputs, self.T, self.env_factors)
        self.assertGreaterEqual(p_s, 0)
        self.assertLessEqual(p_s, 100)

if __name__ == '__main__':
    unittest.main()