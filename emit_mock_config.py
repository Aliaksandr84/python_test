import yaml
import json
import random
import string
from datetime import datetime, timedelta

def random_string(length=8):
    """Return a random string of fixed length."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def mock_config():
    config = {
        "mongodb": {
            "uri": "mongodb://localhost:27017",
            "database": f"testdb_{random_string(5)}",
            "username": random_string(7),
            "password": random_string(10),
            "authSource": "admin"
        },
        "user": {
            "username": random_string(6),
            "email": f"{random_string(5)}@example.com"
        },
        "dataset": {
            "name": f"mock_dataset_{random.randint(1, 100)}",
            "path": f"/tmp/{random_string(10)}.csv",
            "uploaded_at": (datetime.utcnow() - timedelta(days=random.randint(1, 30))).isoformat()
        },
        "quality_check": {
            "columns": ["id", "name", "age"],
            "check_nulls": True,
            "min_rows": random.randint(10, 1000)
        },
        "simulation": {
            "run_id": random_string(8),
            "timestamp": datetime.utcnow().isoformat(),
            "parameters": {
                "threshold": round(random.uniform(0.1, 1.0), 2),
                "max_iter": random.randint(5, 50)
            }
        }
    }
    return config

def save_yaml(config, filename="mock_config.yaml"):
    with open(filename, "w") as f:
        yaml.safe_dump(config, f, sort_keys=False)
    print(f"YAML config written to {filename}")

def main():
    config = mock_config()
    print("Python dict:")
    print(config)
    print("\nJSON:")
    print(json.dumps(config, indent=2))
    save_yaml(config)

if __name__ == "__main__":
    main()