import os
import json

class GetConfig:
    ROOT_DIR = None

    def __init__(self, ROOT_DIR):
        self.ROOT_DIR = ROOT_DIR

    def get(self):
        config_file = os.path.join(self.ROOT_DIR, 'config', 'app.json')
        with open(config_file) as file:
            config = json.load(file)
        return config
