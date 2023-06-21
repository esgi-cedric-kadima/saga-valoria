class Map:
    def __init__(self, lines, columns):
        self.grid = []
        for i in range(lines):
            for j in range(columns):
                self.grid.append([i, j])
