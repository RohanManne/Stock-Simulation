class Stock:
    
    priceHistory = {}
    "priceHistory is a hashSet with Keys: time and date, and values: price at that key"
    "TODO: add sharesBought, shares Sold"
    def __init__(self, name, ticker, price, sector, type, divs, fees, time):
        self.name = name
        self.ticker = ticker
        self.price = price
        priceHistory.update({time: price})
        self.sector = sector
        self.type = type
        self.divs = divs
        self.fees = fees

    def getInfo(self):
        return [self.name][self.ticker][self.price]

    def UpdatePrice(newTime, newPrice):
        priceHistory.update({newTime:newPrice})
        price = newPrice
        time = newTime
    
    
