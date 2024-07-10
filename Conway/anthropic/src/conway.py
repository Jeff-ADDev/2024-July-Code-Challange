import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class GameOfLife:
    def __init__(self, initial_state: List[List[int]]):
        self.grid = np.array(initial_state, dtype=int)
        self.rows, self.cols = self.grid.shape

    def get_neighbors(self, row: int, col: int) -> int:
        return np.sum(self.grid[max(0, row-1):min(row+2, self.rows),
                               max(0, col-1):min(col+2, self.cols)]) - self.grid[row, col]

    def next_generation(self) -> None:
        new_grid = self.grid.copy()
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.get_neighbors(row, col)
                if self.grid[row, col] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[row, col] = 0
                else:
                    if neighbors == 3:
                        new_grid[row, col] = 1
        self.grid = new_grid

    def run_generations(self, generations: int) -> List[List[List[int]]]:
        history = [self.grid.tolist()]
        for _ in range(generations):
            self.next_generation()
            history.append(self.grid.tolist())
        return history

    def animate(self, generations: int, interval: int = 200) -> None:
        fig, ax = plt.subplots()
        img = ax.imshow(self.grid, interpolation='nearest')
        plt.title("Conway's Game of Life")

        def update(frame):
            self.next_generation()
            img.set_array(self.grid)
            return [img]

        anim = FuncAnimation(fig, update, frames=generations, interval=interval, blit=True)
        plt.show()

# LeetCode solution
def gameOfLife(board: List[List[int]]) -> None:
    game = GameOfLife(board)
    game.next_generation()
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = game.grid[i][j]

# Example usage
if __name__ == "__main__":
    initial_state = [
        [1, 1, 0],
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    game = GameOfLife(initial_state)
    
    # Run for 5 generations and print the results
    history = game.run_generations(5)
    for i, state in enumerate(history):
        print(f"Generation {i}:")
        for row in state:
            print(' '.join('■' if cell else '□' for cell in row))
        print()
    
    # Animate for 100 generations
    game = GameOfLife(initial_state)  # Reset the game
    game.animate(100)