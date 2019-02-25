import string
import collections
import random

# Dictionary filter
def find_key(words_character_counter, values_list):
    keys = list()
    words_list = words_character_counter.items()
    for item in words_list:
        if item[1] in values_list:
            keys.append(item[0])
    return keys


'''Read in filename and place words into a dictionary.'''
with open('words.txt') as file:
    text = file.read().casefold()

# Put words from text into a list
words = []
for word in text.split():
    if word in word:
        words.append(word)

# Create dictionary
words_character_counter = {words: len(words) for words, words in enumerate(words)}

# Prepare characters for guessing.
def selected_word_characters(selected_word, guessed):
    '''Put randomized word's characters into a list'''
    # characters = string.ascii_letters
    selected_characters = []
    for character in selected_word:
        if character in guessed:
            selected_characters.append(character) 
        else:
            selected_characters.append('_')
    selected_characters = ' '.join(selected_characters)
    selected_characters = selected_characters.upper()
    return selected_characters

# Monitors the progress of the game.
def word_check(selected_word, guessed):
    """Checks to determine whether or not the word has been guessed. It is called in the game_loop while loop."""
    progress = selected_word_characters(selected_word, guessed)
    if '_' in progress:
        return False
    else:
        return True

# Difficulty selection     
def easy_mode():
    '''Generate a word for easy mode.'''
    easy = find_key(words_character_counter, [4, 5, 6])
    selected_word = random.choice(easy) 
    return selected_word

def normal_mode():
    '''Generate a word for normal mode.'''
    normal = find_key(words_character_counter, [6, 7, 8])
    selected_word = random.choice(normal)
    return selected_word

def hard_mode():
    '''Generate a word for hard mode.'''
    hard = find_key(words_character_counter, [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
    selected_word = random.choice(hard)
    return selected_word

def run_game():
    '''Run the main game loop.'''
    print('''Welcome to the mystery word game! 
    
    The object of the game is to guess the mystery word. In order to play, you must enter a letter that you suspect is in the word. Incorrect answers will count as an 
    attempt. You have 8 attempts to guess the mystery word. I will let you know if your have previously guessed a letter and how many guesses you've used.
    
    ''')

    while True:
        user_input = input('To begin, please select the level of difficulty by enter E for easy, N for normal, and H for hard: ')
        difficulty = ['E','N','H']
        if user_input == difficulty[0]:
            selected_word = easy_mode()
            return gameplay_loop(selected_word)
        elif user_input == difficulty[1]:
            selected_word = normal_mode()
            return gameplay_loop(selected_word)   
        elif user_input == difficulty[2]:
            selected_word = hard_mode()
            return gameplay_loop(selected_word)   
        else:
            print('Something is amiss... Select the difficulty by entering the first capitalized character of the mode you wish to select.\n')
            
def gameplay_loop(selected_word):
    '''Allows user to input their guess, filters guesses, and monitors remaining attempts.'''
    guessed = []
    attempts = 0
    print('The word you\'re looking for has {} letters.\n'.format(len(selected_word)))
    while word_check(selected_word, guessed) == False:
        guess = (input('Enter your the letter you would like to guess: \n'))
        if guess not in string.ascii_letters:
            print('Please enter a letter!')
        elif len(guess) > 1:
            print('You can only guess one character per turn.')
        elif guess not in guessed:
            if guess not in selected_word:
                attempts += 1
                print('That letter isn\'t in your word.')
            else:
                print('Nice! That letter is in your word!')
        else:
            print('You already guessed that!')
        guessed.append(guess)
        print(selected_word_characters(selected_word, guessed))
        print('These are your guesses so far: {}'.format(guessed))
        print('You have {} guesses left.\n'.format(8 - attempts))
        if attempts >= 8:
            break
    if attempts >= 8:
        play_again_lose = input(('You were bested! The word was {}.\n'.format(selected_word)))
        replay()
    else:
        play_again_win = input(('Congratulations, you win!\n'))
        replay()

def replay():
    """Prompt user to replay game"""
    response = input('Would you like to play again? (Y/N): ')
    if response == 'Y' or response == 'y':
        run_game()
    else:
        print('Thanks for playing!')
        return

if __name__ == '__main__':
    run_game()
