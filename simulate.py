import yaml
import time

def simulate_run(config_path="mock_config.yaml"):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    print("\n=== Simulation Run ===")
    print(f"User: {config['user']['username']} ({config['user']['email']})")
    print(f"Dataset: {config['dataset']['name']} at {config['dataset']['path']}")
    print(f"Quality Check Columns: {config['quality_check']['columns']}")
    print(f"Simulation parameters: {config['simulation']['parameters']}")
    print("Running simulation...")

    # Simulate time passing
    time.sleep(1)
    print("Simulation complete!")
    print("======================\n")

if __name__ == "__main__":
    simulate_run()