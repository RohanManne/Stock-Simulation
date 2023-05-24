from classes import *
import random, time

stocks = []

def demand_rand(s : Stock):
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
    ctime = time.time()

    for stock in stocks:

        """
        formula:
        % change = 1 + (a*random unit change based on time step + b*(buy:sell ratio/unique - 20)

        ideally random numbers are not unif but normally distributed so we can normalize our randoms preventing hypervolatility.
        """

        
        newprice = stock.price + \
            c[0] * random.randint(-99, 100) + \
                c[1] * demand_rand() + \
                    c[2] * random.randint(-20, 35) + \
                        c[3] * random.randint(-30, 45)
        
        stock.updatePrice(newprice, ctime)
        
        # day and long-term have different bounds as they have a greater effect, mitigating overall stock collapse due to 'bad rng'.