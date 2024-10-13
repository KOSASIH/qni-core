import unittest
from core.config import Config
import json

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = Config('config.json')

    def test_get_config(self):
        config = self.config.get_config()
        self.assertIsNotNone(config)

    def test_load_config(self):
        self.config.load_config()
        self.assertIsNotNone(self.config.config)

if __name__ == '__main__':
    unittest.main()
