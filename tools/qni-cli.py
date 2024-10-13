import argparse
import json
from quantum.entanglement import Entanglement
from quantum.wormhole import Wormhole

def main():
    parser = argparse.ArgumentParser(description='QNI CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Entanglement subcommand
    entanglement_parser = subparsers.add_parser('entanglement', help='Manage entanglements')
    entanglement_parser.add_argument('particles', nargs='+', help='Particles to entangle')
    entanglement_parser.add_argument('--frequency', type=int, help='Entanglement frequency')

    # Wormhole subcommand
    wormhole_parser = subparsers.add_parser('wormhole', help='Manage wormholes')
    wormhole_parser.add_argument('throat_radius', type=int, help='Wormhole throat radius')
    wormhole_parser.add_argument('--stability_threshold', type=float, help='Wormhole stability threshold')

    args = parser.parse_args()

    if args.command == 'entanglement':
        particles = [Particle(state=np.array([1, 0])) for _ in args.particles]
        entanglement = Entanglement(particles, frequency=args.frequency)
        print(json.dumps(entanglement.state.tolist()))

    elif args.command == 'wormhole':
        wormhole = Wormhole(throat_radius=args.throat_radius, stability_threshold=args.stability_threshold)
        print(json.dumps({'stability': wormhole.stability}))

if __name__ == '__main__':
    main()
