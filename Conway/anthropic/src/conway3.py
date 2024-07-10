import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from conway import GameOfLife  

class GameOfLifeVisualizer:
    def __init__(self, initial_state, generations=100, interval=200, grid_size=(3, 3)):
        self.generations = generations
        self.interval = interval
        self.grid_size = grid_size
        self.games = [GameOfLife(initial_state) for _ in range(np.prod(grid_size))]
        self.fig, self.axes = plt.subplots(grid_size[0], grid_size[1], figsize=(12, 12))
        self.axes = self.axes.flatten()

    def animate(self, frame):
        for i, (game, ax) in enumerate(zip(self.games, self.axes)):
            if i > 0:  # The first game stays at the initial state
                for _ in range(i):  # Advance each subsequent game by one more step
                    game.next_generation()
            ax.clear()
            ax.imshow(game.get_board(), cmap='binary')
            ax.set_title(f'Generation {i}')
            ax.axis('off')
        return self.axes

    def run_animation(self):
        ani = FuncAnimation(self.fig, self.animate, frames=self.generations,
                            interval=self.interval, blit=False)
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == '__main__':
    initial_state = np.random.choice([0, 1], size=(50, 50), p=[0.85, 0.15]).tolist()
    visualizer = GameOfLifeVisualizer(initial_state, generations=100, interval=500, grid_size=(3, 3))
    visualizer.run_animation()