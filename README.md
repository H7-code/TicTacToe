# Tic Tac Toe Game

## Introduction
Tic Tac Toe is a classic two-player game where players take turns to mark spaces on a 3x3 grid with their chosen symbol, either 'X' or 'O'. The goal is to align three of the same symbols in a row, column, or diagonal. This project brings the game to life with an interactive graphical user interface (GUI) built using **Streamlit**. The game also features varying difficulty levels for a more dynamic experience: **Practice**, **Medium**, and **Hard**.

## How to Clone
To clone and run the Tic Tac Toe game on your local machine, follow the steps below:

1. Open your terminal/command prompt.
2. Clone the repository using the following command:
   ```bash
   git clone https://github.com/H7-code/TicTacToe.git
3. Navigate to the project directory:
    ```bash
    cd TicTacToe
## Dependencies
This project requires Python and a few libraries to be installed. You can set up a virtual environment to manage dependencies.
- Install Python (if not already installed).
- Create a virtual environment (optional but recommended):
  ```bash
  python -m venv venv
- Activate the virtual environment:
  ```bash
  .\venv\Scripts\activate
- Install the required libraries:
  ```bash
  pip install -r requirements.txt
4. The requirements.txt file includes:
- streamlit: For the GUI interface.
## How to Play
- Open the game by running the following command:
  ```bash
  streamlit run app.py
- A web browser window will open with the game interface.
- Choose your player symbol (either X or O).
- Select the desired difficulty level:
   Practice: Play against a basic AI.
   Medium: A moderately challenging AI opponent.
   Hard: The hardest AI to challenge your skills.
- The game board will appear, and you can start making moves by clicking on the cells.
- To restart the game, click the "Restart Game" button.
## Game Rules:
- The game is played on a 3x3 grid.
- Players take turns marking their symbol in empty cells.
- The first player to get three of their symbols in a row, column, or diagonal wins.
- If the grid is full and no one wins, the game is a draw.

## Credits
- Creator: Muhammad Hassan
- GitHub Repository: https://github.com/H7-code/TicTacToe
## Closing Message
<span style="color:blue; font-weight:bold;">We hope you enjoy this game! If you have any suggestions, feel free to contribute or reach out. Happy Gaming! 🎮</span>
