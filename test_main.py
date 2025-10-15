import unittest
from gokai_core.main import Synergy, rebalance_weights, simulate_migi_7g_connection
from gokai_core.models.entropy_model import EntropyModel

class TestGokaiCore(unittest.TestCase):
    def setUp(self):
        self.config = {
            'synergy_config': {
                'entropy_threshold': 0.8,
                'creative_keywords': ['zaprojektuj', 'napisz', 'stworz'],
                'base_alpha': 0.9
            },
            'core_params': {
                'matrix_weights': [3, 4, 7, 7, 4, 3],
                'risk_tolerance': 0.15
            },
            'migi_7g': {
                'dev_pool_size': 90000000,
                'active_connection': False
            }
        }
        self.shared_state = {'level': 0, 'n': 1, 'last_success_pct': 0.0, 'history': [], 'weights': self.config['core_params']['matrix_weights']}
        self.synergy = Synergy(self.shared_state, self.config)

    def test_synergy_creative_task(self):
        event = {'payload': 'Zaprojektuj robota.'}
        result = self.synergy.orchestrate(event)
        self.assertEqual(result['mode'], 'CREATIVE_EXPLORATION')
        self.assertEqual(result['pipelines'], ['GOK:AI'])

    def test_rebalance_weights_high_success(self):
        weights = [3, 4, 7, 7, 4, 3]
        success_pct = 95.0
        risk_tolerance = 0.15
        new_weights = rebalance_weights(weights, success_pct, risk_tolerance)
        expected = [4, 5, 7, 7, 5, 4]
        self.assertEqual(new_weights, expected)

    def test_rebalance_weights_low_success(self):
        weights = [3, 4, 7, 7, 4, 3]
        success_pct = 60.0
        risk_tolerance = 1.0
        new_weights = rebalance_weights(weights, success_pct, risk_tolerance)
        self.assertTrue(new_weights[2] <= 7 and new_weights[3] <= 7)

    def test_migi_7g_simulation_inactive(self):
        task = "Testowe zadanie"
        result = simulate_migi_7g_connection(self.config, task)
        self.assertTrue(0.5 <= result <= 0.95)

    def test_entropy_model_fallback(self):
        event = {'payload': 'Proste zadanie'}
        entropy = self.synergy._calculate_entropy(event['payload'])
        self.assertGreater(entropy, 0.0)

if __name__ == '__main__':
    unittest.main()