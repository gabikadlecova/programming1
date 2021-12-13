class SimpleBoard:
    """
    This board does not check anything and does not understand neighbors.
    """
    def __init__(self, board):
        self.board = board

    def get_elem(self, x, y):
        return self.board[x][y]


class Board(SimpleBoard):
    """
    This board does many cool things like checking bounds for indices or returning neighbors for an index.
    """
    def __init__(self, board, diagonal_neighbors=False):
        super().__init__(board)

        # specific for this board (useless in SimpleBoard)
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
        if not self.check_limits(x, y):
            return None
        
        return super().get_elem(x, y)


if __name__ == "__main__":
    list_board = [
        [1, 0, 1],
        [2, 2, 1],
        [1, 1, 1]
    ]

    print("Testing the simple board...")
    simple_board = SimpleBoard(list_board)
    try:
        print(simple_board.get_elem(0, 0))
        print(simple_board.get_elem(50, 50))  # will crash
    except IndexError as e:
        print("Wrong index passed to board.")
        print(e)

    print("\nTesting the extended board...")
    not_so_simple_board = Board(list_board)
    try:
        print(not_so_simple_board.get_elem(0, 0))
        print(not_so_simple_board.get_elem(50, 50))  # will NOT crash :-)
    except IndexError as e:
        print("Wrong index passed to board.")
        print(e)
