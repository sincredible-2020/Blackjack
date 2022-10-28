import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


score = {"A": [1, 11], "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, '8': 8, "9": 9, "10": 10, "J": 10, "Q": 10,
         "K": 10}


def total(alist):
    global summation
    summation = 0
    for a_card in alist:
        if a_card == "A":
            if 21 - summation < 11:
                summation = summation + score[a_card][0]
            elif 21 - summation > 11:
                summation = summation + score[a_card][1]
        else:
            summation = summation + score[a_card]
    return summation


def final_comparison(user_sum, computer_sum):
    if computer_sum > 21:
        return "You Win!"
    elif computer_sum == 21:
        return "Blackjack for the computer!\nYou Lose."
    elif computer_sum > user_sum:
        return "You Lose."
    elif computer_sum < user_sum:
        return "You Win!"
    elif computer_sum == user_sum:
        return "Draw"


def game(player_cards, computer_cards, user_sum, computer_sum):
    global result
    if user_sum == 21:
        return f"Your cards: {player_cards}, current score: {user_sum}\nComputer's cards: {computer_cards}\nBlackjack for you!\nYou Win!"
    elif computer_sum == 21:
        return f"Your cards: {player_cards}, current score: {user_sum}\nComputer's cards: {computer_cards}\nBlackjack for the computer!\nYou Lose."
    elif user_sum > 21:
        return f"Your cards: {player_cards}, current score: {user_sum}\nComputer's cards: {computer_cards}\nYou Lose."
    elif computer_sum > 21:
        return f"Your cards: {player_cards}, current score: {user_sum}\nComputer's cards: {computer_cards}\nYou Win!"
    else:
        print(f"Your cards: {player_cards}, current score: {user_sum}\nComputer's first card: {computer_cards[0]}")
        answer = input("Type 'y' to get another card, type 'n' to pass: ")
        if answer == "y":
            player_cards.append(random.choice((list(score.keys()))))
            user_sum = user_sum + score[player_cards[-1]]
            print(game(player_cards, computer_cards, user_sum, computer_sum))
        elif answer == 'n':
            print(f"Your final hand: {player_cards}, final score: {user_sum}")
            while computer_sum < 17:
                computer_cards.append(random.choice(list(score.keys())))
                computer_sum = computer_sum + score[computer_cards[-1]]
            print(f"Computer's final cards: {computer_cards}, final score: {computer_sum}")
            result = final_comparison(user_sum, computer_sum)
            return result


def main():
    global sum_u
    global sum_c
    if input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
        print(logo, "\nWelcome to Blackjack Game!")
        player_cards = random.choices(list(score.keys()), k=2)
        computer_cards = random.choices(list(score.keys()), k=2)
        sum_u = total(player_cards)
        sum_c = total(computer_cards)
        print(game(player_cards, computer_cards, sum_u, sum_c))
        main()
    else:
        print("You chose not to play the game.")


main()
