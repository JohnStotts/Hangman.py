import random
import os

# ANSI escape codes ~ colors
class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

# words/categories
def choose_word():
    words = {
        "Fruits": ["apple", "banana", "orange", "grape", "pear", "kiwi", "nectarine", "blueberry", "dragonfruit", "cherry"],
        "Colors": ["red", "blue", "green", "yellow", "orange", "purple", "black", "white", "pink", "brown"],
        "Countries": ["china", "usa", "canada", "india", "russia", "brazil", "australia", "france", "japan"],
        "Animals": ["dog", "cat", "elephant", "tiger", "lion", "giraffe", "monkey", "panda", "bear", "kangaroo"],
        "Vegetables": ["carrot", "potato", "broccoli", "cucumber", "spinach", "lettuce", "tomato", "onion", "garlic", "celery"],
        "Sports": ["soccer", "basketball", "tennis", "baseball", "football", "volleyball", "golf", "swimming", "cricket", "hockey"]
    }
    category = random.choice(list(words.keys()))
    return category, random.choice(words[category])

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def get_guess(guessed_letters):
    while True:
        guess = input("Guess a letter or the whole word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        elif len(guess) > 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a letter or the whole word.")

def reset_game():
    return 6, []

def provide_hint(word, guessed_letters):
    hint = random.choice([letter for letter in word if letter not in guessed_letters])
    print(f"Hint: The word contains the letter '{hint}'.")

def play_hangman():
    attempts_limit = 6
    word_count = 5

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen
    
    print(colors.GREEN + "Welcome to Hangman!" + colors.RESET)
    print(colors.YELLOW + "Let's play a game!" + colors.RESET)

    for _ in range(word_count):
        category, word = choose_word()
        attempts, guessed_letters = reset_game()
        
        print(f"\nCategory: {category}")
        print(colors.YELLOW + "New word! Start guessing...\n" + colors.RESET)
        print(display_word(word, guessed_letters))
        
        while True:
            guess = get_guess(guessed_letters)
            if len(guess) == 1:
                guessed_letters.append(guess)
                if guess not in word:
                    attempts -= 1
                    print(colors.RED + f"\nWrong guess! You have {attempts} attempts left." + colors.RESET)
                    draw_hangman(attempts)
                    if attempts == 0:
                        print(colors.RED + "\nGame over! The word was:", word + colors.RESET)
                        break
                    elif attempts < 3:
                        provide_hint(word, guessed_letters)
                displayed = display_word(word, guessed_letters)
                print(displayed)
                if "_" not in displayed:
                    print(colors.GREEN + "\nCongratulations! You guessed the word:", word + colors.RESET)
                    break
            else:
                if guess == word:
                    print(colors.GREEN + "\nCongratulations! You guessed the word:", word + colors.RESET)
                    break
                else:
                    attempts -= 1
                    print(colors.RED + f"\nWrong guess! You have {attempts} attempts left." + colors.RESET)
                    draw_hangman(attempts)
                    if attempts == 0:
                        print(colors.RED + "\nGame over! The word was:", word + colors.RESET)
                        break
            
        play_again = input(colors.YELLOW + "\nDo you want to play again? (yes/no): " + colors.RESET).lower()
        if play_again != "yes":
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
            break

    exit()  # Exit the program after the loop ends

#fun doodles to represent vitality
def draw_hangman(attempts):
    stages = [
        """
           ------
           |    |
           |    O
           |   \|/
           |    |
           |   / \\
           -
        """,
        """
           ------
           |    |
           |    O
           |   \|/
           |    |
           |   / 
           -
        """,
        """
           ------
           |    |
           |    O
           |   \|/
           |    |
           |    
           -
        """,
        """
           ------
           |    |
           |    O
           |   \|
           |    |
           |    
           -
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    |
           |    
           -
        """,
        """
           ------
           |    |
           |    O
           |   
           |    
           |    
           -
        """,
        """
           ------
           |    |
           |    
           |   
           |    
           |    
           -
        """
    ]
    print(stages[attempts])

play_hangman()