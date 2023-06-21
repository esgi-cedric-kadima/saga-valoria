class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.map = [[None for _ in range(cols)] for _ in range(rows)]

    def generate_map(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = {
                    'row': row,
                    'col': col,
                    'item': None
                }
                self.map[row][col] = cell

    def is_adjacent(self, cell1, cell2):
        row1, col1 = cell1['row'], cell1['col']
        row2, col2 = cell2['row'], cell2['col']

        return (abs(row1 - row2) == 1 and col1 == col2) or (row1 == row2 and abs(col1 - col2) == 1)

    def get_map(self):
        return self.map
