import random


print("Welcome the guessing game")
print("""

  _______  __    __   _______      _______.     _______. __  .__   __.   _______      _______      ___      .___  ___.  _______ 
 /  _____||  |  |  | |   ____|    /       |    /       ||  | |  \ |  |  /  _____|    /  _____|    /   \     |   \/   | |   ____|
|  |  __  |  |  |  | |  |__      |   (----`   |   (----`|  | |   \|  | |  |  __     |  |  __     /  ^  \    |  \  /  | |  |__   
|  | |_ | |  |  |  | |   __|      \   \        \   \    |  | |  . `  | |  | |_ |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
|  |__| | |  `--'  | |  |____ .----)   |   .----)   |   |  | |  |\   | |  |__| |    |  |__| |  /  _____  \  |  |  |  | |  |____ 
 \______|  \______/  |_______||_______/    |_______/    |__| |__| \__|  \______|     \______| /__/     \__\ |__|  |__| |_______|
                                                                                                                                

""")
def seed():
    seed = random.randint(0, 101)
    return seed

def user_input(user_answer):
    if user_answer == 'easy':
        turn = 5
    else:
        turn = 10

    return turn


def game(turn):
    secret_value = seed()
    # print(secret_value)
    while turn>0:
        guess = int(input("guess your number:").lower())
        if guess == secret_value:
            print(f"you got it, the answer is {guess}\n")
            break
        elif guess > secret_value:
            print("your guess is too high\nGuess again")
            turn -=1
            print(f"you have {turn} attempt\n")
        else:
            print("your guess is too low\nGuess again")
            turn -=1
            print(f"you have {turn} attempt\n")
    if turn == 0:
        print("you loose!")


def main():
    user_answer = input("you want easy or difficult? answer 'easy' or 'difficult\n")
    turn = user_input(user_answer)
    print(f"turn {turn}")
    game(turn)



if __name__ == '__main__': main()