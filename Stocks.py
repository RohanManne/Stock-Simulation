import User

class Stock:
    
    priceHistory = {}
    "priceHistory is a hashSet with Keys: time and date, and values: price at that key"
    "TODO: add sharesBought, shares Sold"
    def __init__(self, name, ticker, price, sector, stock_type, divs, fees, time):
        self.name = name
        self.ticker = ticker
        self.price = price
        self.priceHistory.update({time: price})
        self.sector = sector
        self.type = stock_type
        self.bought = 0
        self.sold = 0
        self.unique_inter = set()
        self.shares = 0
        self.available_shares
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

    def sell(self, user : User.User):
        self.sold += 1
        self.available_shares += 1
        self.unique_inter.add(user)

    def sellShares(self, user : User.User, num_shares : int):
        self.sold += num_shares
        self.available_shares += num_shares
        self.unique_inter.add(user)

    def buy(self, user : User.User):
        if self.available_shares > 0:
            self.bought += 1
            self.available_shares -= 1
            self.unique_inter.add(user)
        else:
            raise Exception("No shares available")

    def buyShares(self, user : User.User, num_shares : int):
        if self.available_shares >= num_shares:
            self.bought += num_shares
            self.available_shares -= num_shares
            self.unique_inter.add(user)
        else:
            raise Exception("Not enough shares available")