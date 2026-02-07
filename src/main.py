import argparse
from src.simulation import MarketSimulation

def main():
    parser = argparse.ArgumentParser(description="Crypto Economics Simulator")
    parser.add_argument("--steps", type=int, default=50, help="Number of simulation steps")
    
    args = parser.parse_args()
    
    sim = MarketSimulation(steps=args.steps)
    sim.run()
    sim.export_data()

if __name__ == "__main__":
    main()
