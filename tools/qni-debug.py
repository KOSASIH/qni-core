import logging
from quantum.entanglement import Entanglement
from quantum.wormhole import Wormhole

def main():
    logging.basicConfig(level=logging.DEBUG)

    # Entanglement debugging
    particles = [Particle(state=np.array([1, 0])), Particle(state=np.array([0, 1]))]
    entanglement = Entanglement(particles, frequency=1000)
    logging.debug('Entanglement state:')
    logging.debug(entanglement.state)

    # Wormhole debugging
    wormhole = Wormhole(throat_radius=10, stability_threshold=0.9)
    logging.debug('Wormhole stability:')
    logging.debug(wormhole.stability)

if __name__ == '__main__':
    main()
