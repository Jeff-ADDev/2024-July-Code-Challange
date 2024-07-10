# 2024-July-Code-Challange
RevLocal Intern Code Challenge

## Approach
Using 3 AI models to complete the code challanges to show their skill and abilities to solve coding problems
OpenAI ChatGPT 4o , Anthropic Claude 3.5 Sonnet, Meta.AI

Each challange will have it's own directory and each AI will have it's directory under the challange
- anthropic
- meta
- openai

In the AI directory's will be
- src directory
- interaction.md: Documentation of the interaction with the AI
- requirements.txt

## Running the different solutions
- Change directory to the AI directory
- Use venv to create a new environemnt: ```python3 -m venv venv```
- Change to that environment: ```source venv/bin/activate```
- Install the required libraries in the environemnt: ```pip install -r requirements.txt```

## Conway
Overview of the problem: Conway’s Game of Life is a cellular automaton created in 1970 by British mathematician John Horton Conway. It’s a zero-player game whose evolution is determined by its initial state, requiring no further input. The game consists of a grid of cells that can be in one of two states: alive or dead. The state of each cell evolves in discrete time steps according to a simple set of rules based on the state of its eight neighbors.
Here are the basic rules:
1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The game begins with an initial configuration of live and dead cells. As the rules are applied repeatedly, patterns emerge, evolve, and sometimes stabilize or disappear. Some patterns can become quite complex and exhibit behaviors similar to those found in natural systems.  

Specifics of the problem: Step 1: Solve the LeetCode problem.
Step 2: Expand your LeetCode solution by accepting an initial grid state, applying the rules of Conway’s Game of Life, and outputting the grid state for multiple generations.
Step 3 (Optional): Create a graphical representation to visualize and animate its evolution.