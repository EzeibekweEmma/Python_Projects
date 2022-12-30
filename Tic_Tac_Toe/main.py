import random

# Tic Tac Toe Game!!! By Ezeibekwe Emmanuel
# Contact @ https://twitter.com/Ezeibekweemma

is_playing = True
player_letter = ""
computer_letter = ""
player_point = 0
computer_point = 0
pattern = '1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9'
data = {
    1: "_", 2: "_", 3: "_",
    4: "_", 5: "_", 6: "_",
    7: " ", 8: " ", 9: " "
}


# setting up Game Broad Pattern function
def game_broad():
    broad = ""
    is_bar = 0
    for x in range(9):
        x += 1
        broad += data[x]

        if is_bar < 2:
            broad += " | "
            is_bar += 1
        else:
            broad += "\n"
            is_bar = 0

    print(broad)


# setting data back to default function
def default_data():
    for x in data:
        if x < 7:
            data[x] = "_"
        else:
            data[x] = " "


# Checking for wins function
def checking_win():
    data_arr = [data[i] for i in data]
    x11 = data_arr[0]
    x12 = data_arr[1]
    x13 = data_arr[2]
    x21 = data_arr[3]
    x22 = data_arr[4]
    x23 = data_arr[5]
    x31 = data_arr[6]
    x32 = data_arr[7]
    x33 = data_arr[8]
    global player_point, computer_point

    if x11 == x12 == x13 == player_letter or x21 == x22 == x23 == player_letter or x31 == x32 == x33 == player_letter \
            or x11 == x21 == x31 == player_letter or x12 == x22 == x32 == player_letter or x13 == x23 == x33 == \
            player_letter or x11 == x22 == x33 == player_letter or x13 == x22 == x31 == player_letter:
        print("--You Win--")
        game_broad()
        player_point += 1
        print(f"computer - {computer_point} : player - {player_point}")
        to_continue()
    elif x11 == x12 == x13 == computer_letter or x21 == x22 == x23 == computer_letter or x31 == x32 == x33 == \
            computer_letter or x11 == x21 == x31 == computer_letter or x12 == x22 == x32 == computer_letter or x13 == \
            x23 == x33 == computer_letter or x11 == x22 == x33 == computer_letter or x13 == x22 == x31 == \
            computer_letter:
        print("--You Loss--")
        game_broad()
        computer_point += 1
        print(f"computer - {computer_point} : player - {player_point}")
        to_continue()


# Continue playing or quit function
def to_continue():
    cq = int(input("Press 1 to Continue OR any number to Quit: "))
    if cq == 1:
        default_data()
    else:
        global is_playing
        is_playing = False


# Main Game function
def tic_tac_toe():
    try:
        global player_letter, computer_letter, is_playing
        letter = int(input("Choose letter Press 1 for O OR 2 for X: "))
        if letter == 1:
            player_letter = "O"
            computer_letter = "X"
        elif letter == 2:
            player_letter = "X"
            computer_letter = "O"
        else:
            print("--Invalid Input! Run Again--")
            is_playing = False

        while is_playing:
            try:
                print(pattern)

                remaining_data = [i for i in data if 'O' != data[i] != 'X']
                if len(remaining_data) != 0:
                    player = int(input(f"You're player {player_letter} Enter the number you want to play 1-9: "))

                    if 0 < player < 10:
                        if 'O' != data[player] != 'X':
                            data[player] = player_letter
                            checking_win()
                            if not is_playing:
                                break
                        else:
                            print(f"--Can't play {player}, Choose another number!--")
                            continue
                    else:
                        print("--Invalid number!--")
                        continue
                else:
                    print("--Game Tie--")
                    to_continue()
                    if not is_playing:
                        break
            except ValueError:
                print("--Invalid Input!--")
                continue
            #   Computer Game
            remaining_data = [i for i in data if 'O' != data[i] != 'X']
            if len(remaining_data) != 0:
                computer = random.randint(0, len(remaining_data) - 1)
                computer = remaining_data[computer]
                data[computer] = computer_letter
                checking_win()
                if not is_playing:
                    break
            else:
                print("--Game Tie!--")
                to_continue()
                if not is_playing:
                    break

            game_broad()
    except ValueError:
        print("--Invalid Input!--")


# Starting the Game
tic_tac_toe()

print("---GAME OVER---")

if player_point > computer_point:
    print("---YOU WON---")
elif player_point == computer_point:
    print("---GAME TIE---")
else:
    print("---YOU LOSS---")

print(f"computer - {computer_point} : player - {player_point}")
