import pdb
import logging
from core.logger import Logger

class Debug:
    def __init__(self):
        self.logger = Logger()
        self.debugger = pdb.Pdb()

    def debug(self, module):
        self.logger.info(f"Debugging {module}...")
        self.debugger.set_trace()

    def debug_quantum(self):
        self.debug("Quantum Entanglement")
        from qni_core.quantum.entanglement import Entanglement
        entanglement = Entanglement(particles=2)
        entanglement.entangle()

    def debug_cultural_integration(self):
        self.debug("Cultural Integration")
        from ai.cultural_integration import CulturalIntegration
        data = [{"feature1": 1, "feature2": 2}, {"feature1": 3, "feature2": 4}]
        ci = CulturalIntegration(data)
        ci.integrate()

    def debug_cli(self):
        self.debug("CLI")
        from qni_cli.cli import CLI
        cli = CLI()
        cli.run()

if __name__ == '__main__':
    debug = Debug()
    debug.debug_quantum()
    debug.debug_cultural_integration()
    debug.debug_cli()
