import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GameOfLife:
    def __init__(self, initial_state):
        self.board = [row[:] for row in initial_state]

    def gameOfLife(self):
        m, n = len(self.board), len(self.board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < m and 0 <= nj < n and abs(self.board[ni][nj]) == 1:
                        live_neighbors += 1
                if self.board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    self.board[i][j] = -1
                if self.board[i][j] == 0 and live_neighbors == 3:
                    self.board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if self.board[i][j] == -1:
                    self.board[i][j] = 0
                elif self.board[i][j] == 2:
                    self.board[i][j] = 1

    def animate(self, generations):
        fig, ax = plt.subplots()
        ax.set_axis_off()
        im = ax.imshow(self.board, cmap='binary')

        def update(frame):
            self.gameOfLife()
            im.set_array(self.board)
            return im,

        ani = animation.FuncAnimation(fig, update, frames=generations, blit=True)
        plt.show()

initial_state = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

game = GameOfLife(initial_state)
game.animate(10)