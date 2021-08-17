class Ship:
    def __init__(self, size, coord_x, coord_y, direction):
        self.size = size
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.direction = direction

    def get_ship(self, ship_cell):
        self.ship_cell = ship_cell
        return [self.ship_cell] * self.size
