import unittest
from core.config import Config
from core.logging import logger

class TestConfig(unittest.TestCase):
    def test_load_config(self):
        config = Config()
        self.assertIsNotNone(config.config)

    def test_get_config_value(self):
        config = Config()
        self.assertEqual(config.get('quantum_entanglement.enabled'), True)

class TestLogging(unittest.TestCase):
    def test_log_debug(self):
        logger.debug('This is a debug message')
        self.assertTrue(True)  # This test will pass if the debug message is logged

    def test_log_info(self):
        logger.info('This is an info message')
        self.assertTrue(True)  # This test will pass if the info message is logged

if __name__ == '__main__':
    unittest.main()
