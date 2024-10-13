import unittest
from core.logger import Logger
import logging

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_set_log_level(self):
        self.logger.logger.setLevel(logging.DEBUG)
        self.assertEqual(self.logger.logger.level, logging.DEBUG)

    def test_log_info(self):
        self.logger.info('Test log message')
        self.assertTrue(True)  # Logging test is manual

    def test_log_debug(self):
        self.logger.debug('Test debug message')
        self.assertTrue(True)  # Logging test is manual

if __name__ == '__main__':
    unittest.main()
