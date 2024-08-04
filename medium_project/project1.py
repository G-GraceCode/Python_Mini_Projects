import random


def rolldice():
    max_num = 6
    min_num = 1
    roll = random.randint(min_num, max_num)
    return roll


while True:
    num_of_players = input("Enter the number of Player(2 - 4): ")
    if (num_of_players.isdigit()):
        num_of_players = int(num_of_players)
        if (2 <= num_of_players <= 4):
            break
        else:
            print('Must enter a number between 2 - 4')
    else:
        print("Invalide number")

max_score = 50
player_scores = [0 for _ in range(num_of_players)]

''' a List comprehension: which start everything in 0 base on the num of player e.g [0, 0], [0, 0, 0] and where _ means i does care the iteration'''


while max(player_scores) < max_score:
    for player_idx in range(num_of_players):
        print("\nPlay number ", player_idx + 1, "Turn has started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you play (y): ")
            if should_roll.lower() != "y":
                break

            value = rolldice()

            if value == 1:
                print("You rolled a 1!, Turn done")
                current_score = 0
                break
            else:
                current_score += value
                print("You roll a:", value)

            print("Your score is: ", current_score)
        player_scores[player_idx] += current_score
        print("Your total score is: ", player_scores[player_idx])


# displaying the winner

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)

print("Player number", winning_idx + 1,
      "is the winner with a scoe of", max_score)
