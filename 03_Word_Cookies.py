# Word Cookies
from random import shuffle

cookies_words = [
    {"ADOTY": {
        "answer": ["DOT", "DAY", "TODAY", "TOY", "TOAD", "OAT", "TAD"],
        "user_ans": [],
        "bonus": ["AYO", "ADO", "TAO", "DAT"]
    }},
    {"FHORT": {
        "answer": ["FOR", "FORT", "FORTH", "FROTH", "HOT", "ROT"],
        "user_ans": [],
        "bonus": ["THOR", "TOR", "RHO", "THO"]
    }},
    {"EIPTY": {
        "answer": ["PET", "PIE" , "PIT", "TIE", "TIP", "YET", "PITY", "TYPE", "PIETY"],
        "user_ans": [],
        "bonus": ["YETI", "YIP"]
    }},
]


def display_ans(word) -> None:
    k = 0
    for i in word:
        k += 1
        print(i, end="")
    print(end="\n")


def shuffle_word(word: list) -> list:
    """
    shuffle word
    :param word: list
    :return list: cast_to_list
    """
    cast_to_list = list(word)
    shuffle(cast_to_list)
    return cast_to_list


def layout(words: list) -> None:
    """
    game layout
    :param words: - dict
    :return None: None
    """
    game_level = 0
    game_stop = len(words) - 1
    user_points = 0
    while game_level <= game_stop:
        pick_one = words[game_level]
        cookies_word = list(pick_one.keys())[0]
        printed_word = shuffle_word(list(cookies_word))
        print(f"Level {game_level + 1} ->", printed_word)
        word = pick_one[cookies_word]
        word["answer"].sort()
        k = 0
        for i in word["answer"]:
            k += 1
            print(f"{k}.", end="")
            for j in range(len(i)):
                print("_", end=" ")
            #     setting user answer format
            word["user_ans"].append(f"{k}.{len(i) * '_ '}")
            print(" ", end="")
        print(end="\n")

        is_game = True
        while is_game:
            user_input = input(f"Generate word form Level {game_level + 1}: "
                               f"").upper().strip()
            if user_input == "S":
                printed_word = shuffle_word(list(cookies_word))
                print(f"Level {game_level + 1} ->", printed_word)
            elif user_input == "H":
                if user_points >= 0:
                    # user_points -= 3
                    for i in word["user_ans"]:
                        if '_' in i:
                            position:int = word["user_ans"].index(i)
                            print(position)
                            # get_hint:str = word["answer"][position][0]
                            # word["user_ans"][position] = i[:2] + get_hint + " " + i[2:-2]
                            # break
                else:
                    print(f"Don't have Enough point for hint! remaining point -\
 {user_points}")
            else:
                print(f"Level {game_level + 1} ->", printed_word)
                if user_input in word["answer"] or user_input in word["bonus"]:
                    if user_input in word["answer"]:
                        position = word["answer"].index(user_input)
                        word["user_ans"][position] = f"{position + 1}.{user_input} "
                        display_ans(word["user_ans"])
                        check_ans = [None] * len(word["user_ans"])
                        for i in range(len(word["user_ans"])):
                            if word["user_ans"][i][2:-1] == word["answer"][i]:
                                check_ans[i] = word["answer"][i]
                            if check_ans == word["answer"]:
                                if game_level < game_stop:
                                    user_points += 5
                                    print(f"Added 5 point. Total Point Earn = \
{user_points}\nNext Level ->")
                                game_level += 1
                                is_game = False
                    else:
                        user_points += 1
                        print(f"Bonus Word!!! Added 1 point. Total Point Earn \
 = {user_points}")
                else:
                    print("oops! Word Not Found! Try again\nS - Shuffle Word \
OR H - Hint for 3 point")
    else:
        print("You Win!\nCookies Word Game Completed!")


layout(cookies_words)

# not to show printed_word once the users ans is filled
