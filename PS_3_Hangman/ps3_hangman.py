# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    print(random.choice(wordlist))
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

# Example Usage:
    
#secretWord = "apple"
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#lettersGuessed = ['e', 'i', 'l', 'p', 'a', 's']
#secretWord = "lettuce"
#lettersGuessed = ['z', 'x', 'q', 'l', 'e', 't', 't', 'u', 'c', 'e']
#secretWord = "durian"
#lettersGuessed = ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

#print("#secretWord:", secretWord)
#print("#lettersGuessed:", lettersGuessed)
#print(isWordGuessed(secretWord, lettersGuessed))

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ""
    for char in secretWord:
        if char not in lettersGuessed:
            word += "_ "
        else:
            word += char
    return word
    
#print(getGuessedWord(secretWord, lettersGuessed))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    word = ""
    all_chars = "abcdefghijklmnopqrstuvwxyz"
    for char in all_chars:
        if char not in lettersGuessed:
            word += char
    return word
    
#print(getAvailableLetters(lettersGuessed))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("")
    print("")
    print("")
    print("")
    print("")
    print("****Game starts here****")
    print("")
    wordLen = len(secretWord)
    guessLeft = 8
    lettersGuessed = []
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", wordLen, "letters long.")
    for g in range(guessLeft):
        guessedWord = getGuessedWord(secretWord, lettersGuessed)
        charsLeft = getAvailableLetters(lettersGuessed)
        print("-------------")
        print("You have", guessLeft, "guesses left.")
        print("Available letters:", charsLeft)
        char = input("Please guess a letter: ")[:1]
        lettersGuessed.append(char)
        if char not in charsLeft:
            print("Oops! You've already guessed that letter:", guessedWord)
        elif char not in secretWord:
            guessLeft -= 1
            print("Oops! That letter is not in my word:", guessedWord)
        elif char in charsLeft:
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            print("Good guess:", guessedWord)
        is_correct_guess = isWordGuessed(secretWord, lettersGuessed)
        if is_correct_guess:
            print("-------------")
            print("Congratulations, you won!")
            return
    print("-------------")
    print("Sorry, you ran out of guesses. The word was else.")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()

hangman(secretWord)
