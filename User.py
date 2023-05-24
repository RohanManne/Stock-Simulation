import Position

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
