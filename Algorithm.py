import Stocks, User, random

"""
dont have a concrete ds for manager of stocks, users, etc.

using stand-ins for it for now
"""

def demand_rand(s : Stocks.Stock):
    threshold = s.shares / 20
    ratio = s.bought / s.sold
    rand = random.randint(-99, 100)
    if s.bought + s.sold > threshold:
        return rand * ratio
    else:
        return 1


def tick():
    # every tick
    c = [0.015, 0.025, 0.03, 0.075]

    for stock in StockManager.Iter():

        """
        formula:
        % change = 1 + (a*random unit change based on time step + b*(buy:sell ratio/unique - 20)

        ideally random numbers are not unif but normally distributed so we can normalize our randoms preventing hypervolatility.
        """

        
        stock.price *= 1 + \
            c[0] * random.randint(-99, 100) + \
                c[1] * demand_rand() + \
                    c[2] * random.randint(-20, 35) + \
                        c[3] * random.randint(-30, 45)
        
        # day and long-term have different bounds as they have a greater effect, mitigating overall stock collapse due to 'bad rng'.

    # UserManager.updateAll()