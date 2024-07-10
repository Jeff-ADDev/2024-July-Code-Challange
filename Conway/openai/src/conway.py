from typing import List
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate_game_of_life(initial_board: List[List[int]], generations: int):
    board = np.array(initial_board)
    
    def update(frame):
        nonlocal board
        new_board = np.copy(board)
        for row in range(board.shape[0]):
            for col in range(board.shape[1]):
                live_neighbors = np.sum(board[max(0, row-1):min(board.shape[0], row+2), max(0, col-1):min(board.shape[1], col+2)]) - board[row, col]
                if board[row, col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    new_board[row, col] = 0
                elif board[row, col] == 0 and live_neighbors == 3:
                    new_board[row, col] = 1
        mat.set_data(new_board)
        board = new_board
        return [mat]
    
    fig, ax = plt.subplots()
    mat = ax.matshow(board, cmap='binary')
    
    ani = animation.FuncAnimation(fig, update, frames=generations, interval=350, blit=True)
    plt.show()

def game_of_life_multigen(board: List[List[int]], generations: int) -> List[List[int]]:
    """
    Evolve the board for a given number of generations.
    """
    def count_live_neighbors(board, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), 
                      (0, -1),         (0, 1), 
                      (1, -1), (1, 0), (1, 1)]
        live_neighbors = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if (0 <= r < len(board)) and (0 <= c < len(board[0])) and board[r][c] == 1:
                live_neighbors += 1
        return live_neighbors
    
    def next_state(board):
        new_board = [row[:] for row in board]
        for row in range(len(board)):
            for col in range(len(board[0])):
                live_neighbors = count_live_neighbors(board, row, col)
                if board[row][col] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_board[row][col] = 0
                else:
                    if live_neighbors == 3:
                        new_board[row][col] = 1
        return new_board

    for _ in range(generations):
        board = next_state(board)
    
    return board

# Example usage:
initial_board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]

generations = 25
animate_game_of_life(initial_board, generations)