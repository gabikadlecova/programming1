from graphs import Board
from collections import deque


def bfs(board, start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited = set()

    while len(queue):
        # visit next state
        next_elem_x, next_elem_y = queue.pop()
        visited.add((next_elem_x, next_elem_y))

        # check if it's what we're looking for
        value = board.get_elem(next_elem_x, next_elem_y)
        if value == 1:
            return (next_elem_x, next_elem_y)

        neighbors = board.get_neighbors(next_elem_x, next_elem_y)
        # dead end
        if not len(neighbors):
            continue

        for n in neighbors:
            # add only unvisited neighbors to the stack
            if n in visited:
                continue
            else:
                queue.appendleft(n)  # enqueue

    return None


if __name__ == "__main__":
    test_board = [
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 2]
    ]

    board = Board(test_board)
    print(bfs(board, 0, 0))

    board = Board(test_board, diagonal_neighbors=True)
    print(bfs(board, 0, 0))

    # todo - add path length to queue
    # todo - find path to 2 and count number of ones on the way
    # todo (hard exercise) - find the path to 2 with the most ones (no repeated visits on one path)
