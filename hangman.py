import random

def main():
    # create the art for hangman
    hangman = {1: """
        _____
        |    |
        |    O
        |
        |
        |
    
    """,

    2: """
        _____
        |    |
        |    O
        |   /
        |
        |
    
    """,
    3: """
        _____
        |    |
        |    O
        |   / \\
        |
        |
    """,
    4: """
        _____
        |    |
        |    O
        |   /|\\
        |
        |
    
    """,
    5: """
        _____
        |    |
        |    O
        |   /|\\
        |   /
        |
    
    """,

    6: """
        _____
        |    |
        |    O
        |   /|\\
        |   / \\
        |
    
    """
    }

    #print the welcome message
    print("""
        Welcome to hangman game!
        ,--.  ,--.  ,---.  ,--.  ,--. ,----.   ,--.   ,--.  ,---.  ,--.  ,--. 
        |  '--'  | /  O  \ |  ,'.|  |'  .-./   |   `.'   | /  O  \ |  ,'.|  | 
        |  .--.  ||  .-.  ||  |' '  ||  | .---.|  |'.'|  ||  .-.  ||  |' '  | 
        |  |  |  ||  | |  ||  | `   |'  '--'  ||  |   |  ||  | |  ||  | `   | 
        `--'  `--'`--' `--'`--'  `--' `------' `--'   `--'`--' `--'`--'  `--'                                                                            
    
    """)
    # create the list of word for game
    #use random to get the random word
    list = ["chicken", "pork", "kimchi", "rice", "sauce",
            "Christmas", "glass", "soup", "water", "juice"]
    word = random.choice(list)

    # create word_list to contain the character of the random word
    word_list = []
    for i in range(len(word)):
        word_list.append(word[i])

    # print(word_list)

    # create the list with empty character underline
    letter_list = ["_"] * len(word)
    print(letter_list)

    # create the variable for wrong guess to keep track
    wrong_count = 0

    # create the while loop < 6 (hangman art) and if still have empty space
    # we must ask the user enter new letter
    #if the word_list[] = user input letter in variable guess, the letter will add to letter list
    #index which have same index with word list
    while wrong_count < 6 and "_" in letter_list:
            guess = input("please enter one letter: \n").lower()
            for i in range(len(word_list)):
                if word_list[i] == guess:
                    letter_list[i] = guess
                    # print("your guess is right")

            user_input_repeat_list = []
            if guess in word_list:
                user_input_repeat_list.append(guess)
                print("you chose this letter. Please choose another one")


            # keep track guess wrong with word_list, the wrong count will increase one until 6
            if guess not in word_list:
                wrong_count +=1
                print("you guess wrong")
                print(hangman[wrong_count])

                if wrong_count == 6:
                    break

            print(letter_list)

    # maximum guess is 6, after 6 time wrong, if the letter list = word_list, the user win
    #if not the user wrong
    if letter_list == word_list:
        print("you won")
    else:
        print("you lose")

if __name__ == '__main__': main()