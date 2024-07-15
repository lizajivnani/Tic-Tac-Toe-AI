<h1>Tic-Tac-Toe AI: Unbeatable Intelligence at Play!</h1>

<p>Welcome to the Tic-Tac-Toe challenge! This isn't your average X's and O's game – it's a showdown between human intuition and machine intelligence. Are you ready to match wits with a computer that never loses?</p>

<h2>🚀 Project Description</h2>

<p>This project implements an AI to optimally play Tic-Tac-Toe using the Minimax algorithm. Watch <href src = "https://www.youtube.com/watch?v=3QUrHA7NJHc"> this </href>video for a demo</p>


<h2>Features</h2>

<ul>
  <li>Implements the Minimax algorithm for optimal play</li>
  <li>Graphical interface for human vs. AI gameplay</li>
  <li>Functions to determine game state, possible actions, and game outcomes</li>
</ul>

<h2>Files</h2>

<ul>
  <li><code>tictactoe.py</code>: Contains the game logic and AI implementation</li>
  <li><code>runner.py</code>: Handles the graphical interface and game execution</li>
</ul>

<h2>Requirements</h2>

<ul>
  <li>Python 3.10  or higher</li>
  <li>Pygame library</li>
</ul>

<h2>Installation</h2>

<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/lizajivnani/Tic-Tac-Toe-AI.git</code></pre>
  </li>
  <li>Navigate to the project directory:
    <pre><code>cd Tic-Tac-Toe-AI</code></pre>
  </li>
  <li>Install the required packages:
    <pre><code>pip3 install -r requirements.txt</code></pre>
  </li>
</ol>



<h2>Usage</h2>

<p>To play against the AI, run:</p>

<pre><code>python runner.py</code></pre>

<h2>Implementation Details</h2>

<p>The <code>tictactoe.py</code> file contains the following key functions:</p>

<ul>
  <li><code>player(board)</code>: Determines which player's turn it is</li>
  <li><code>actions(board)</code>: Returns all possible actions for the current board state</li>
  <li><code>result(board, action)</code>: Returns the resulting board state after an action</li>
  <li><code>winner(board)</code>: Determines the winner of the game, if any</li>
  <li><code>terminal(board)</code>: Checks if the game has ended</li>
  <li><code>utility(board)</code>: Assigns a utility value to terminal game states</li>
  <li><code>minimax(board)</code>: Implements the Minimax algorithm to determine the optimal move</li>
</ul>


  <h2>Acknowledgments</h2>
  
  <p>This project was implemented as part of the coursework for Harvard University's CS50 Introduction to Artificial Intelligence with Python.</p>


