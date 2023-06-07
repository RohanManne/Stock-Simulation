import main
from classes import *
from itertools import product
from random import randint
from time import time
from copy import deepcopy

"""
inject placeholder stocks to main sim
"""
def generate_placeholder(length : int = 3):

	# defn
	ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	stocks = dict()
	stock_names = [ ''.join(i) for i in product(ALPHA, repeat=length) ]
	
	# generate stocks with ticker and starting price roughly unif
	for name in stock_names:
		"""
		(self, name, ticker, price, shares, sector, stock_type, divs, fees, time)
		"""
		temp = Stock(name, name, randint(20, 500), randint(40, 4000), "", "", "", "", time())
		stocks[name] = deepcopy(temp)

	# inject to main
	main.stocks = stocks

"""
run simulation
"""
def run_placeholder(examine_list : list):
	while(input() != 'q'):
		main.tick()
		for s in examine_list:
			print("%s: %.2f" % (s, main.stocks[s].price))


if __name__ == "__main__":
	length = int(input("length to generate: "))
	examine_list = input("stocks to watch (caps): ").split()
	generate_placeholder(length)
	run_placeholder(examine_list)