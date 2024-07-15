Tic-Tac-Toe AI
<p>This project implements an AI to play Tic-Tac-Toe optimally using the Minimax algorithm. It's part of CS50's Introduction to Artificial Intelligence with Python course.</p>
Project Description
<p>The goal of this project is to create an AI that plays Tic-Tac-Toe perfectly. The AI uses the Minimax algorithm to determine the best possible move in any given game state, ensuring that it never loses a game[2].</p>
Features
Implements the Minimax algorithm for optimal play
Graphical interface for human vs. AI gameplay
Functions to determine game state, possible actions, and game outcomes
Files
tictactoe.py: Contains the game logic and AI implementation
runner.py: Handles the graphical interface and game execution
Requirements
Python 3.10 (recommended for compatibility with the course)
Pygame library
Installation
Clone the repository:
text
git clone https://github.com/lizajivnani/Tic-Tac-Toe-AI.git

Navigate to the project directory:
text
cd Tic-Tac-Toe-AI

Install the required packages:
text
pip3 install -r requirements.txt

Usage
To play against the AI, run:
text
python runner.py

Implementation Details
The tictactoe.py file contains the following key functions:
player(board): Determines which player's turn it is
actions(board): Returns all possible actions for the current board state
result(board, action): Returns the resulting board state after an action
winner(board): Determines the winner of the game, if any
terminal(board): Checks if the game has ended
utility(board): Assigns a utility value to terminal game states
minimax(board): Implements the Minimax algorithm to determine the optimal move
Contributing
Contributions to improve the project are welcome. Please fork the repository and create a pull request with your changes.
License
This project is open source and available under the MIT License. <hr> <p><em>Note: This project is part of CS50's Introduction to Artificial Intelligence with Python. Please refer to the course's academic honesty guidelines before using this code.</em></p>
