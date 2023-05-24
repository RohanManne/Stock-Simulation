import Stocks

class Position:
    def __init__(self, initial_price, num_shares, ticker):
        self.initial_price = initial_price
        self.num_shares = num_shares
        self.ticker = ticker
        self.__stock_ref
