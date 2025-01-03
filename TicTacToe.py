import streamlit as st
import random

# Function to check for a winner
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

# Function to find best move for hard difficulty
def find_best_move(board, player):
    opponent = "O" if player == "X" else "X"
    
    # Check if player can win in the next move
    for i in range(9):
        if board[i] == "":
            board[i] = player
            if check_winner(board, player):
                board[i] = ""
                return i
            board[i] = ""

    # Block opponent's winning move
    for i in range(9):
        if board[i] == "":
            board[i] = opponent
            if check_winner(board, opponent):
                board[i] = ""
                return i
            board[i] = ""

    # Pick center if available
    if board[4] == "":
        return 4

    # Pick a corner if available
    for i in [0, 2, 6, 8]:
        if board[i] == "":
            return i

    # Pick a side if available
    for i in [1, 3, 5, 7]:
        if board[i] == "":
            return i

    return None

# Function to handle computer's move
def computer_move(board, difficulty, computer_symbol):
    if difficulty == "Practice":
        empty_cells = [i for i in range(9) if board[i] == ""]
        return random.choice(empty_cells) if empty_cells else None
    elif difficulty == "Medium":
        return random.choice([
            find_best_move(board, computer_symbol),
            random.choice([i for i in range(9) if board[i] == ""])
        ])
    elif difficulty == "Hard":
        return find_best_move(board, computer_symbol)

# Main function to run the app
def main():
    st.title("Tic Tac Toe")

    # Initialize session state
    if "board" not in st.session_state:
        st.session_state.board = ["" for _ in range(9)]
        st.session_state.player_symbol = None
        st.session_state.computer_symbol = None
        st.session_state.difficulty = None
        st.session_state.current_turn = None
        st.session_state.result = None

    # Game setup
    if st.session_state.player_symbol is None:
        st.subheader("Choose your symbol")
        if st.button("X"):
            st.session_state.player_symbol = "X"
            st.session_state.computer_symbol = "O"
            st.session_state.current_turn = "Player"
        elif st.button("O"):
            st.session_state.player_symbol = "O"
            st.session_state.computer_symbol = "X"
            st.session_state.current_turn = "Computer"

    if st.session_state.difficulty is None and st.session_state.player_symbol:
        st.subheader("Choose difficulty level")
        if st.button("Practice"):
            st.session_state.difficulty = "Practice"
        elif st.button("Medium"):
            st.session_state.difficulty = "Medium"
        elif st.button("Hard"):
            st.session_state.difficulty = "Hard"

    # Game logic
    if st.session_state.difficulty and st.session_state.result is None:
        st.subheader("Tic Tac Toe Board")
        cols = st.columns(3)

        for i, cell in enumerate(st.session_state.board):
            with cols[i % 3]:
                if cell == "":
                    if st.session_state.current_turn == "Player" and st.button(f" ", key=str(i)):
                        st.session_state.board[i] = st.session_state.player_symbol
                        if check_winner(st.session_state.board, st.session_state.player_symbol):
                            st.session_state.result = "You win!"
                        elif all(st.session_state.board):
                            st.session_state.result = "It's a draw!"
                        else:
                            st.session_state.current_turn = "Computer"
                else:
                    st.button(cell, disabled=True, key=str(i))

        if st.session_state.current_turn == "Computer" and st.session_state.result is None:
            move = computer_move(
                st.session_state.board,
                st.session_state.difficulty,
                st.session_state.computer_symbol
            )
            if move is not None:
                st.session_state.board[move] = st.session_state.computer_symbol
                if check_winner(st.session_state.board, st.session_state.computer_symbol):
                    st.session_state.result = "Computer wins!"
                elif all(st.session_state.board):
                    st.session_state.result = "It's a draw!"
                else:
                    st.session_state.current_turn = "Player"

    # Display result
    if st.session_state.result:
        st.subheader(st.session_state.result)
        if st.button("Play Again"):
            st.session_state.board = ["" for _ in range(9)]
            st.session_state.player_symbol = None
            st.session_state.computer_symbol = None
            st.session_state.difficulty = None
            st.session_state.current_turn = None
            st.session_state.result = None

if __name__ == "__main__":
    main()
