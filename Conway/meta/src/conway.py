import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_game_of_life(initial_state, generations):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    board = [row[:] for row in initial_state]
    im = ax.imshow(board, cmap='binary')

    def update(frame):
        global board
        board = gameOfLife(board)
        im.set_array(board)
        return im,

    ani = animation.FuncAnimation(fig, update, frames=generations, blit=True)
    plt.show()

def gameOfLife(board):
    m, n = len(board), len(board[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
    for i in range(m):
        for j in range(n):
            live_neighbors = 0
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                    live_neighbors += 1
            if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[i][j] = -1
            if board[i][j] == 0 and live_neighbors == 3:
                board[i][j] = 2
    for i in range(m):
        for j in range(n):
            if board[i][j] == -1:
                board[i][j] = 0
            elif board[i][j] == 2:
                board[i][j] = 1
    return board

def conway_game_of_life(initial_state, generations):
    board = [row[:] for row in initial_state]
    for _ in range(generations):
        board = gameOfLife(board)
    return board

initial_state = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# conway_game_of_life(initial_state, 10)
animate_game_of_life(initial_state, 10)