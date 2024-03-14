import streamlit as st
import numpy as np


def initialize_board(size):
    return np.zeros((size, size))
def is_valid_move(board, row, col):
    return board[row][col] == 0
def make_move(board, row, col, player):
    board[row][col] = player
def check_win(board, player):
    if np.any(np.all(board == player, axis=0)) or np.any(np.all(board == player, axis=1)):
        return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False
def ai_move(board):
    valid_moves = np.argwhere(board == 0)
    move = valid_moves[np.random.choice(len(valid_moves))]
    return move
def main():
    st.title("Simple Strategy Game")

    size = st.sidebar.slider("Select Board Size", 3, 10, 3)
    player = st.sidebar.radio("Select Player", ('X', 'O'))

    board = initialize_board(size)
    st.write("Current Board:")
    st.write(board)

    if player == 'X':
        st.write("Player's Turn")
        col, row = st.number_input("Enter row:", min_value=0, max_value=size-1), st.number_input("Enter column:", min_value=0, max_value=size-1)
        if st.button("Make Move"):
            if is_valid_move(board, row, col):
                make_move(board, row, col, 1)
                st.write("Player moved to:", (row, col))
            else:
                st.write("Invalid move! Try again.")

            if check_win(board, 1):
                st.write("Player wins!")
            else:
                st.write("AI's Turn")
                ai_row, ai_col = ai_move(board)
                make_move(board, ai_row, ai_col, -1)
                st.write("AI moved to:", (ai_row, ai_col))

                if check_win(board, -1):
                    st.write("AI wins!")

        st.write("Updated Board:")
        st.write(board)

if __name__ == "__main__":
    main()
