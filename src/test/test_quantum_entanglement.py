import unittest
from qni_core.quantum.entanglement import Entanglement
import numpy as np

class TestQuantumEntanglement(unittest.TestCase):
    def setUp(self):
        self.particles = 2
        self.entanglement = Entanglement(particles=self.particles)

    def test_entangle(self):
        self.entanglement.entangle()
        self.assertIsNotNone(self.entanglement.state)

    def test_measure(self):
        self.entanglement.entangle()
        result = self.entanglement.measure()
        self.assertIsNotNone(result)

    def test_get_state(self):
        self.entanglement.entangle()
        state = self.entanglement.get_state()
        self.assertIsNotNone(state)

if __name__ == '__main__':
    unittest.main()
