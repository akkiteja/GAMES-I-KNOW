from .error import *
from random import randint

class Generator:
    def __init__(self, size_x: int=12, size_y: int=10, blank_id: str=" ", mine_id: str="M"):
        """
        The main generator object in charge of generating grids based on its configuration.
        :param size_x: integer (default 12)
        :param size_y: integer (default 10)
        :param blank_id: string (default " ")
        :param mine_id: string (default "M")
        """
        self.size_x = size_x
        self.size_y = size_y
        self.blank_id = blank_id
        self.mine_id = mine_id

        if self.size_x < 1:
            raise InvalidGridSize("Expected size_x to be an int of value 1+, got: %s" % self.size_x)
        if self.size_y < 1:
            raise InvalidGridSize("Expected size_y to be an int of value 1+, got: %s" % self.size_y)

    @staticmethod
    def check_near(x, y, locations):
        """
        :param x: int
        :param y: int
        :param locations: list
        :return int
        """
        found = 0

        for p in [[x+1, y], [x-1, y], [x, y+1], [x, y-1], [x-1, y-1], [x-1, y+1], [x+1, y-1], [x+1, y+1]]:
            if p in locations:
                found += 1

        return found

    def generate_raw(self, mines: int=5):
        """
        Generates a 2D list containing all the rows of the complete minesweeper grid based on the class
        grid_x and grid_y parameters and the mines entered.
        :param mines: integer (default 5)
        :return list
        """
        if mines < 0:
            raise InvalidMineCount("Expected mines to be an int of value 0+, got %s" % mines)
        if mines > self.size_x * self.size_y:
            raise InvalidMineCount("Expected mines to be an int with max value %s (max grid size), got %s" % (self.size_x * self.size_y, mines))

        grid = []

        # Setup mine locations
        locations = []
        for _ in range(mines):
            # Simple loop to stop multiple mines being in the same cell
            found = False
            while not found:
                pos = [randint(0, self.size_x-1), randint(0, self.size_y-1)]
                if pos not in locations:
                    locations.append(pos)
                    found = True

        # Generate grid
        for row in range(self.size_y):
            row_content = []

            for column in range(self.size_x):
                # If the current cell is a mine location
                if [column, row] in locations:
                    row_content.append(self.mine_id)
                else:
                    nearby_mines = self.check_near(column, row, locations)
                    row_content.append(self.blank_id if nearby_mines == 0 else "%s" % nearby_mines)

            grid.append(row_content)

        return grid

    def generate(self, mines: int=5):
        """
        Generates a grid with the specified amount of mines using generate_raw then outputs the result
        with the IDs of mines and blank cells in a dict object.
        :param mines: integer (default 5)
        :return dict
        """
        return {"grid": self.generate_raw(mines),
                "size_x": self.size_x, "size_y": self.size_y,
                "blank_id": self.blank_id, "mine_id": self.mine_id}

    def config(self, size_x=None, size_y=None, blank_id=None, mine_id=None):
        """
        :param size_x: integer (optional)
        :param size_y: integer (optional)
        :param blank_id: string (optional)
        :param mine_id: string (optional)
        :return None
        """
        self.size_x = size_x if size_x else self.size_x
        self.size_y = size_y if size_y else self.size_y
        self.blank_id = str(blank_id) if blank_id else self.blank_id
        self.mine_id = str(mine_id) if mine_id else self.mine_id
