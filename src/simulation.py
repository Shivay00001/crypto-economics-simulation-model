import random
import pandas as pd
from src.bonding_curve import BondingCurve

class MarketSimulation:
    def __init__(self, steps: int = 100):
        self.steps = steps
        self.curve = BondingCurve(reserve_ratio=0.2) # 20% Reserve Ratio (Steep curve)
        self.supply = 1000.0
        self.reserve = 200.0 # Initial seeding
        self.history = []

    def run(self):
        print("Starting Simulation...")
        
        for i in range(self.steps):
            action = random.choice(['BUY', 'SELL'])
            amount = random.uniform(10, 100)
            
            price_before = self.curve.get_spot_price(self.supply, self.reserve)
            
            if action == 'BUY':
                tokens_minted = self.curve.calculate_purchase_return(self.supply, self.reserve, amount)
                self.reserve += amount
                self.supply += tokens_minted
                print(f"Step {i}: BUY  ${amount:.2f} -> +{tokens_minted:.2f} Tokens | Price: ${price_before:.2f}")
            else:
                # Sell
                if self.supply > amount: # Ensure we don't drain everything
                    reserve_returned = self.curve.calculate_sale_return(self.supply, self.reserve, amount)
                    self.reserve -= reserve_returned
                    self.supply -= amount
                    print(f"Step {i}: SELL {amount:.2f} Tokens -> -${reserve_returned:.2f} | Price: ${price_before:.2f}")
            
            self.history.append({
                'step': i,
                'supply': self.supply,
                'reserve': self.reserve,
                'price': self.curve.get_spot_price(self.supply, self.reserve)
            })

    def export_data(self, filename="simulation_data.csv"):
        df = pd.DataFrame(self.history)
        df.to_csv(filename, index=False)
        print(f"Data exported to {filename}")
