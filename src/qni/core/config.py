import os
import json

class Config:
    def __init__(self):
        self.config_file = os.path.join(os.path.dirname(__file__), 'config.json')
        self.load_config()

    def load_config(self):
        with open(self.config_file, 'r') as f:
            self.config = json.load(f)

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

config = Config()

# Example config.json file:
# {
#     "quantum_entanglement": {
#         "enabled": true,
#         "frequency": 1000
#     },
#     "wormhole_generation": {
#         "enabled": true,
#         "stability_threshold": 0.9
#     },
#     "cultural_integration": {
#         "enabled": true,
#         "language_models": ["galactic_standard", "zorvathian"]
#     }
# }
