
class Position:
    def __init__(self, initial_price, num_shares, ticker):
        self.initial_price = initial_price
        self.num_shares = num_shares
        self.ticker = ticker
        self.__stock_ref
    
class User:
    def __init__(self, name):
        self.name = name
        self.cash = 1000
        self.positions = dict()
        self.net = self.cash

    def add_position(self, position: Position.Position):
        self.positions[position.ticker] = position

    def edit_position(self, ticker : str, change : int):
        self.positions[ticker].num_shares += change

    def remove_position(self, ticker : str):
        del self.positions[ticker]

    def update_positions(self):
        for (ticker, position) in self.positions:
            pass

class Stock:
    
    priceHistory = {}
    "priceHistory is a hashSet with Keys: time and date, and values: price at that key"
    "TODO: add sharesBought, shares Sold"
    def __init__(self, name, ticker, price, shares,
                 sector, stock_type, divs, fees, time):
        self.name = name
        self.ticker = ticker
        self.price = price
        self.priceHistory.update({time: price})
        self.sector = sector
        self.type = stock_type
        self.bought = 0
        self.sold = 0
        self.unique_inter = set()
        self.shares = shares
        self.available_shares = shares
        self.divs = divs
        self.fees = fees

    def getInfo(self):
        return [self.name, self.ticker, self.price]

    def updatePrice(self, newTime, newPrice):
        self.priceHistory.update({newTime:newPrice})
        self.price = newPrice

    """
    TODO implement custom exception type for buying error to catch in other methods.
    """

    def sell(self, user : User.User, num_shares : int):
        self.sold += num_shares
        self.available_shares += num_shares
        self.unique_inter.add(user)

    def buy(self, user : User.User, num_shares : int):
        if self.available_shares >= num_shares:
            self.bought += num_shares
            self.available_shares -= num_shares
            self.unique_inter.add(user)
        else:
            raise Exception("Not enough shares available")
