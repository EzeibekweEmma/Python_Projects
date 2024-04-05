import random

board_game = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]
reset_board_game = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]
board_nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
is_user_turn = True
is_computer_turn = True
user_score = 0
computer_score = 0
user_sym = ""
computer_sym = ""
is_playing = False


def display_board(board) -> None:
    """
    Displaying the game board in tic toc toe format
    :param board: 2D list - board_game
    :return None: None
    """
    divider = 0
    for row in board:
        for col in row:
            divider += 1
            if divider % 3 == 0:
                print(col)
            else:
                print(col, end=" | ")


def empty_space() -> bool:
    """
    Calculating the remaining spaces
    :return bool: True or False
    """
    count_empty_space = 0
    for i in board_game:
        for j in i:
            if j == "_":
                count_empty_space += 1
    if count_empty_space:
        return True
    else:
        return False


def selecting_position(get_position: int, symbol: str, player: str = "computer") -> None:
    """
    Here! we get players input and update the game board
    :param get_position: players input
    :param symbol: players symbol
    :param player: Identify player
    :selected_position: Getting players position
    :position_pick: selected_position % 3 = 0 - 2
    :return None: None
    """
    selected_position = get_position - 1
    position_pick = selected_position % 3
    global is_user_turn
    global is_computer_turn

    if selected_position < 3 and board_game[0][position_pick] == "_":
        board_game[0][position_pick] = symbol
        is_user_turn = False
        is_computer_turn = False
    elif 3 <= selected_position < 6 and board_game[1][position_pick] == "_":
        board_game[1][position_pick] = symbol
        is_user_turn = False
        is_computer_turn = False
    elif 6 <= selected_position < 9 and board_game[2][position_pick] == "_":
        board_game[2][position_pick] = symbol
        is_user_turn = False
        is_computer_turn = False
    elif selected_position >= 9:
        print("invalid position")
    else:
        if player == "user":
            print("Position have been taken!")


def user_turn() -> None:
    """
    user turn to play
    while is_user_turn is true ->
    pass the position picked by the user to the selecting_position() function
    :return None: None
    """
    while is_user_turn:
        user_input = int(
            input("Enter the position you want to place your game: "))

        # Check if the user's move leads to a win
        if is_winning_move(user_input, user_sym):
            print("You win!")
            display_board(board_game)
            return

        # Check if the user's move leads to a blockable win
        if is_blockable_win(user_input, user_sym):
            print("Blocked by the computer!")
            selecting_position(user_input, user_sym, "user")
            return

        selecting_position(user_input, user_sym, "user")


def is_blockable_win(position: int, symbol: str) -> bool:
    """
    Check if the player's move can be blocked by the computer
    """
    selected_position = position - 1
    row = selected_position // 3
    col = selected_position % 3

    # Check row, column, and diagonal for a potential player win
    potential_win = (
        all(board_game[row][i] == symbol for i in range(3)) or
        all(board_game[i][col] == symbol for i in range(3)) or
        (row == col and all(board_game[i][i] == symbol for i in range(3))) or
        (row + col == 2 and all(board_game[i][2 - i] == symbol for i in range(3)))
    )

    if not potential_win:
        return False

    # Check if the computer can block the player's win by occupying the remaining spot
    return any(
        board_game[r][c] == "_" for r in range(3) for c in range(3)
        if (r != row or c != col) and is_winning_move(r * 3 + c + 1, user_sym)
    )


last_position = 0


def computer_turn() -> None:
    """
    computer turn to play
    """
    global last_position
    computer_input = None

    # Check for a winning move
    for i in range(1, 10):
        if is_valid_move(i):
            if is_winning_move(i, computer_sym):
                computer_input = i
                break

    # Check to block the player
    if computer_input is None:
        for i in range(1, 10):
            if is_valid_move(i):
                if is_winning_move(i, user_sym):
                    computer_input = i
                    break

    # Place the symbol strategically
    if computer_input is None:
        if is_valid_move(5):
            computer_input = 5
        else:
            corners = [1, 3, 7, 9]
            random.shuffle(corners)
            for corner in corners:
                if is_valid_move(corner):
                    computer_input = corner
                    break

    # If no strategic move found, choose any available spot randomly
    if computer_input is None:
        while True:
            computer_input = random.randint(1, 9)
            if is_valid_move(computer_input):
                break

    last_position = computer_input
    selecting_position(computer_input, computer_sym)

def is_valid_move(position: int) -> bool:
    """
    Check if a move is valid (the position is empty)
    """
    selected_position = position - 1
    position_pick = selected_position % 3
    if selected_position < 3 and board_game[0][position_pick] == "_":
        return True
    elif 3 <= selected_position < 6 and board_game[1][position_pick] == "_":
        return True
    elif 6 <= selected_position < 9 and board_game[2][position_pick] == "_":
        return True
    else:
        return False

def is_winning_move(position: int, symbol: str) -> bool:
    """
    Check if placing the symbol at the specified position results in a win
    """
    selected_position = position - 1
    row = selected_position // 3
    col = selected_position % 3

    # Check row, column, and diagonal for a win
    return (
        all(board_game[row][i] == symbol for i in range(3)) or
        all(board_game[i][col] == symbol for i in range(3)) or
        (row == col and all(board_game[i][i] == symbol for i in range(3))) or
        (row + col == 2 and all(board_game[i][2 - i] == symbol for i in range(3)))
    )



def print_win(symbol):
    global is_playing, user_score, computer_score, board_game
    if symbol == user_sym:
        print("you win")
        user_score += 1
    else:
        print("you lose")
        computer_score += 1

    board_game = reset_board_game
    is_playing = False


def check_win(symbol: str) -> None:
    global board_game

    a00 = board_game[0][0]
    a01 = board_game[0][1]
    a02 = board_game[0][2]

    a10 = board_game[1][0]
    a11 = board_game[1][1]
    a12 = board_game[1][2]

    a20 = board_game[2][0]
    a21 = board_game[2][1]
    a22 = board_game[2][2]

    if a00 == a01 == a02 == symbol or a10 == a11 == a12 == symbol or a20 == a21 == a22 == symbol:
        print_win(symbol)
        board_game = reset_board_game
    elif a00 == a10 == a20 == symbol or a01 == a11 == a21 == symbol or a02 == a12 == a22 == symbol:
        print_win(symbol)
        board_game = reset_board_game
    elif a00 == a11 == a22 == symbol or a02 == a11 == a20 == symbol:
        print_win(symbol)
        board_game = reset_board_game
    elif not empty_space():
        print("tie")
        display_board(board_game)
        board_game = reset_board_game


def main_game():
    global is_user_turn, is_computer_turn, user_sym, computer_sym, is_playing, board_game

    print("Positions: ")
    display_board(board_nums)
    print("Board Game")
    display_board(board_game)

    # user_name = input("Enter user name: ").capitalize()
    while True:
        user_sym = input("Choose symbol X/O: ").upper()
        if user_sym in ["X", "O"]:
            break
        print("Symbol must be X or O")

    if user_sym == "X":
        computer_sym = "O"
    else:
        computer_sym = "X"

    # while True:
    is_playing = empty_space()
    board_game = reset_board_game

    while is_playing:
        if is_user_turn:
            user_turn()
            check_win(user_sym)
            is_computer_turn = True
        else:
            computer_turn()
            check_win(computer_sym)
            is_user_turn = True
            display_board(board_game)

        # print(f"{user_name}: {user_score} - Computer: {computer_score}")


main_game()
