class Stock:
    
    "priceHistory is a hashSet with Keys: time and date, and values: price at that key"
    def __init__(self, name, ticker, price, priceHistory, sector, type):
        self.name = name
        self.ticker = ticker
        self.price = price
        self.priceHistory = priceHistory
        self.sector = sector
        self.type = type

    def getInfo(self):
        return f"{self.name}({self.ticker}) is currently trading at {self.price}"
    
    
    