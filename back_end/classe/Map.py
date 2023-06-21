import random

class Map:
    def __init__(self, lines, columns):
        self.grid = []
        for i in range(lines):
            row = []
            for j in range(columns):
                row.append(None)
            self.grid.append(row)

    def populate(self, events):
        for line in range(len(self.grid)):
            for column in range(len(self.grid[line])):
                self.grid[line][column] = random.choice(events)
