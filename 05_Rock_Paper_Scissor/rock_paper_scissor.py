import random

print('''Game Rule:
1 - "Rock"
2 - "Paper"
3 - "Scissor"
''')
try:
    game_words = ["Rock", "Paper", "Scissor"]
    computer_choose = game_words[random.randint(0, 2)]
    user_input = int(input("Enter Game Number 1-3: ")) - 1
    user_choose = game_words[user_input]
    print("Computer =", computer_choose, "-- User =", user_choose)

    if user_choose == "Rock":
        if computer_choose == "Paper":
            print("You Lose")
        elif computer_choose == "Scissor":
            print("You Win")
        else:
            print("Tie")

    elif user_choose == "Paper":
        if computer_choose == "Scissor":
            print("You Lose")
        elif computer_choose == "Rock":
            print("You Win")
        else:
            print("Tie")

    elif user_choose == "Scissor":
        if computer_choose == "Rock":
            print("You Lose")
        elif computer_choose == "Paper":
            print("You Win")
        else:
            print("Tie")
except ValueError:
    print("Invalid input 1-3")
except IndexError:
    print("Invalid input 1-3")
