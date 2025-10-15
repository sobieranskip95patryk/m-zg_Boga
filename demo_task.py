from gokai_core.main import Synergy, run_cycle
import yaml

def run_demo():
    with open("gokai_core/config.yml", 'r') as f:
        config = yaml.safe_load(f)
    
    shared_state = {'level': 0, 'n': 1, 'last_success_pct': 0.0, 'history': [], 'weights': config['core_params']['matrix_weights']}
    synergy = Synergy(shared_state, config)

    task = {'payload': 'Zaprojektuj statek kosmiczny.'}
    strategy = synergy.orchestrate(task)
    result, success_pct = run_cycle(task['payload'], config, shared_state['weights'])
    
    print(f"Strategia: {strategy['mode']}")
    print(f"Wynik: {result}")
    print(f"Sukces: {success_pct:.2f}%")

if __name__ == '__main__':
    run_demo()