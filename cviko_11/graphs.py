class Board:
    def __init__(self, board, diagonal_neighbors=False):
        self.board = board
        self.xlim = len(board)
        self.ylim = len(board[0])
        self.diagonal_neighbors = diagonal_neighbors

    def check_limits(self, x, y):
        return 0 <= x < self.xlim and 0 <= y < self.ylim

    def get_neighbors(self, index_x, index_y):
        neighbors = []

        for diff_x in [1, 0, -1]:
            for diff_y in [1, 0, -1]:
                if diff_x == 0 and diff_y == 0:
                    # no change in index
                    continue

                if diff_x * diff_y != 0 and not self.diagonal_neighbors:
                    # skip if one of the indices isn't 0 ... the neighbor is diagonal
                    continue

                new_x, new_y = index_x + diff_x, index_y + diff_y
                if self.check_limits(new_x, new_y):
                    neighbors.append((new_x, new_y))

        return neighbors

    def get_elem(self, x, y):
        return self.board[x][y]
