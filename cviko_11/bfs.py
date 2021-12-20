from graphs import Board
from collections import deque


def bfs(board, start_x, start_y, value_to_find=1):
    first = {
        'indices': (start_x, start_y),
        'length': 0,
        'n_ones': 0,
        'prev': []
    }

    queue = deque([first])
    visited = set()

    while len(queue):
        # visit next state
        curr_dict = queue.pop()
        next_elem_x, next_elem_y = curr_dict['indices']
        next_length = curr_dict['length']

        visited.add((next_elem_x, next_elem_y))

        # check if it's what we're looking for
        value = board.get_elem(next_elem_x, next_elem_y)
        if value == value_to_find:
            return curr_dict
        elif value == 1:
            curr_dict['n_ones'] += 1

        neighbors = board.get_neighbors(next_elem_x, next_elem_y)
        # dead end
        if not len(neighbors):
            continue

        for n in neighbors:
            # add only unvisited neighbors to the stack
            if n in visited:
                continue
            else:
                next_elem = {
                    'indices': n,
                    'length': next_length + 1,
                    'n_ones': curr_dict['n_ones'],
                    'prev': curr_dict['prev'].copy() + [curr_dict['indices']]
                }
                queue.appendleft(next_elem)  # enqueue

    return None


if __name__ == "__main__":
    test_board = [
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [1, 1, 0, 2]
    ]

    board = Board(test_board)
    print(bfs(board, 0, 0, value_to_find=2))

    board = Board(test_board, diagonal_neighbors=True)
    print(bfs(board, 0, 0, value_to_find=2))

    # (x) add path length to queue
    # todo - find path to 2 and count number of ones on the way
    # todo (hard exercise) - find the path to 2 with the most ones (no repeated visits on one path)

