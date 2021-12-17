import random

def computer_pick():
    random.seed(random.randint(0,30000))
    return random.randint(0,2)

def main():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    key = {0:rock , 1:paper, 2:scissors}

    player_point = 0
    computer_point = 0
    while True:
        choice = int(input("please enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
        print(f"Player choice: {key.get(choice)}")
        computer = computer_pick()
        print(f"Computer choice: {key.get(computer)}")

        if choice == computer:
            print("you pick the same - Try again")
            continue
        if choice == 0 and computer == 2 or choice == 2 and computer == 1 or choice == 1 and computer == 0:
            print("you win")
            player_point +=1
        else:
            print("you loose")
            computer_point +=1
            if computer_point == 3:
                break

main()


