<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic-Tac-Toe AI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        .badges {
            text-align: center;
            margin-bottom: 20px;
        }
        .badge {
            display: inline-block;
            padding: 5px 10px;
            margin: 0 5px;
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            font-size: 0.8em;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>Tic-Tac-Toe AI</h1>

    <div class="badges">
        <span class="badge">Python 3.10</span>
        <span class="badge">CS50's Introduction to AI</span>
        <span class="badge">Intermediate</span>
    </div>

    <p style="text-align: center;">An AI that plays Tic-Tac-Toe optimally using the Minimax algorithm.</p>

    <h2>Description</h2>
    <p>This project implements an AI to play Tic-Tac-Toe optimally using the Minimax algorithm. The AI is designed to make the best possible move in any given game state, ensuring that it never loses a game when playing perfectly.</p>

    <h2>Features</h2>
    <ul>
        <li>Implements the Minimax algorithm for optimal decision-making</li>
        <li>Provides a graphical interface for human vs. AI gameplay</li>
        <li>Includes functions for game logic and state management</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/your-username/tictactoe-ai.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd tictactoe-ai</code></pre>
        </li>
        <li>Install the required dependencies:
            <pre><code>pip3 install -r requirements.txt</code></pre>
        </li>
    </ol>

    <h2>Usage</h2>
    <p>Run the game with the following command:</p>
    <pre><code>python runner.py</code></pre>
    <p>This will start the graphical interface where you can play against the AI.</p>

    <h2>Project Structure</h2>
    <ul>
        <li><code>runner.py</code>: Contains the code for the graphical interface</li>
        <li><code>tictactoe.py</code>: Implements the game logic and AI algorithm</li>
    </ul>

    <h2>Implementation Details</h2>
    <p>The project requires the implementation of the following functions in <code>tictactoe.py</code>:</p>
    <ul>
        <li><code>player(board)</code>: Determines which player's turn it is</li>
        <li><code>actions(board)</code>: Returns a set of all possible actions</li>
        <li><code>result(board, action)</code>: Returns the board that results from making a move</li>
        <li><code>winner(board)</code>: Determines the winner of the game, if any</li>
        <li><code>terminal(board)</code>: Checks if the game has ended</li>
        <li><code>utility(board)</code>: Evaluates the utility of a terminal game state</li>
        <li><code>minimax(board)</code>: Implements the Minimax algorithm to determine the best move</li>
    </ul>

    <h2>Contributing</h2>
    <p>Contributions to improve the AI or add new features are welcome. Please feel free to submit a pull request.</p>

    <h2>License</h2>
    <p>This project is part of CS50's Introduction to Artificial Intelligence with Python course and is subject to the course's licensing terms.</p>

    <h2>Acknowledgments</h2>
    <ul>
        <li>This project is part of CS50's Introduction to Artificial Intelligence with Python course.</li>
        <li>Special thanks to the CS50 team for providing the project specification and distribution code.</li>
        <li>Inspired by the work of Raymond Smullyan on logical puzzles.</li>
    </ul>

    <div class="footer">
        <p>Made with ❤️ by [Your Name]</p>
    </div>
</body>
</html>
