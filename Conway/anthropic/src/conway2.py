import numpy as np
from typing import List
import unittest

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        # Convert to numpy array for efficient operations
        board_np = np.array(board)
        
        # Pad the board with zeros
        padded = np.pad(board_np, ((1, 1), (1, 1)), mode='constant')
        
        # Count live neighbors using convolution
        neighbors = np.zeros((m+2, n+2), dtype=int)
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                neighbors += np.roll(padded, (i-1, j-1), (0, 1))
        
        # Apply Game of Life rules
        new_board = np.zeros((m+2, n+2), dtype=int)
        new_board[1:-1, 1:-1] = ((neighbors[1:-1, 1:-1] == 3) | 
                                 ((board_np == 1) & (neighbors[1:-1, 1:-1] == 2)))
        
        # Update the original board in-place
        board[:] = new_board[1:-1, 1:-1].tolist()

class GameOfLife:
    def __init__(self, initial_state: List[List[int]]):
        self.board = np.array(initial_state)
        self.solution = Solution()

    def next_generation(self) -> None:
        self.solution.gameOfLife(self.board.tolist())

    def get_board(self) -> List[List[int]]:
        return self.board.tolist()

class TestGameOfLife(unittest.TestCase):
    def test_leetcode_example1(self):
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        expected = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        solution = Solution()
        solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_leetcode_example2(self):
        board = [[1,1],[1,0]]
        expected = [[1,1],[1,1]]
        solution = Solution()
        solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_empty_board(self):
        board = []
        expected = []
        solution = Solution()
        solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_single_cell_board(self):
        board = [[1]]
        expected = [[0]]
        solution = Solution()
        solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_multiple_generations(self):
        initial_state = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        game = GameOfLife(initial_state)
        
        # First generation
        game.next_generation()
        self.assertEqual(game.get_board(), [[0,0,0],[1,0,1],[0,1,1],[0,1,0]])
        
        # Second generation
        game.next_generation()
        self.assertEqual(game.get_board(), [[0,0,0],[0,0,1],[1,1,1],[0,1,0]])

if __name__ == '__main__':
    unittest.main()