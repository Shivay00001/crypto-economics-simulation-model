import numpy as np

class BondingCurve:
    def __init__(self, reserve_ratio: float = 0.5):
        self.reserve_ratio = reserve_ratio

    def calculate_purchase_return(self, supply: float, reserve_balance: float, deposit_amount: float) -> float:
        """
        Calculates how many tokens are minted for a given deposit.
        Based on Bancor Formula.
        """
        if supply == 0:
            return deposit_amount # Initial price 1:1

        # T = S * ((1 + D / R) ^ cw - 1)
        # S = supply, D = deposit, R = reserve, cw = reserve_ratio (weight)
        # Actually Bancor formula for purchase return:
        # Return = Supply * ((1 + Deposit/Reserve) ^ ReserveRatio - 1)
        
        return supply * ((1 + deposit_amount / reserve_balance) ** self.reserve_ratio - 1)

    def calculate_sale_return(self, supply: float, reserve_balance: float, sell_amount: float) -> float:
        """
        Calculates how much reserve is returned for selling tokens.
        """
        # Return = Reserve * (1 - (1 - SellAmount/Supply) ^ (1/ReserveRatio))
        
        if sell_amount > supply:
            raise ValueError("Cannot sell more than total supply")

        return reserve_balance * (1 - (1 - sell_amount / supply) ** (1 / self.reserve_ratio))

    def get_spot_price(self, supply: float, reserve_balance: float) -> float:
        """
        Spot Price = Reserve / (Supply * ReserveRatio)
        """
        if supply == 0:
            return 1.0
        return reserve_balance / (supply * self.reserve_ratio)
