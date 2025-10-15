import unittest
from gokai_core.main import Synergy, run_cycle, simulate_migi_7g_connection
from gokai_core.utils.weights import rebalance_weights

class TestGokaiIntegration(unittest.TestCase):
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
                'active_connection': False,
                'response_delay': 0.5,
                'max_contributors': 1000
            }
        }
        self.shared_state = {'level': 0, 'n': 1, 'last_success_pct': 0.0, 'history': [], 'weights': self.config['core_params']['matrix_weights']}
        self.synergy = Synergy(self.shared_state, self.config)

    def test_full_pipeline(self):
        event = {'payload': 'Zaprojektuj robota.'}
        strategy = self.synergy.orchestrate(event)
        result, success_pct = run_cycle(event['payload'], self.config, self.shared_state['weights'])
        new_weights = rebalance_weights(self.shared_state['weights'], success_pct, self.config['core_params']['risk_tolerance'])
        
        self.assertEqual(strategy['mode'], 'CREATIVE_EXPLORATION')
        self.assertTrue(80 <= success_pct <= 100)
        self.assertEqual(len(new_weights), 6)

    def test_migi_7g_integration(self):
        task = "Testowe zadanie"
        contribution = simulate_migi_7g_connection(self.config, task)
        self.assertTrue(0.5 <= contribution <= 0.95)

if __name__ == '__main__':
    unittest.main()