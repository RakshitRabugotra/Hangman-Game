# Hangman game

import random
import string

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
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord:str, lettersGuessed:list):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if lettersGuessed is None: return False
    else: return all(map(lambda x: x in lettersGuessed, secretWord))


def getGuessedWord(secretWord:str, lettersGuessed:list):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = "_ "*len(secretWord)
    word.strip()
    word = word.split(" ")
    word.pop()

    if_guess_in_word = set((secretWord[i], (secretWord[i] in lettersGuessed, i)) for i in range(len(secretWord)))

    for k, v in if_guess_in_word:
      if v[0]: word[v[1]] = k
      else: pass

    return " ".join(word).strip()


def getAvailableLetters(lettersGuessed:list):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    parent = string.ascii_lowercase
    available_words = []

    for letter in parent:
      if letter in lettersGuessed: continue
      else: available_words.append(letter)

    return "".join(available_words)

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
    lettersGuessed = [] # The letters that have been guessed so far.
    mistakesMade = -8 # The number of incorrect guesses made so far.
    availableLetters = getAvailableLetters(lettersGuessed) # The letters that may still be guessed

    # Setting up the premise
    print("Welcome to the game Hangman! \nI am thinking of a word that is {} letters long.".format(len(secretWord)))
    # Guessing word
    word = "_"

    while mistakesMade != 0:
        print("\n------------- \nYou have {} guesses left. \nAvailable letters: {}".format(mistakesMade*(-1), availableLetters))
        # Taking a guess from user
        guess = input("Please guess a letter: ").lower()

        if len(guess) > 1 or guess == "":
            print("Invalid Guess... Guess a letter only")
            continue
        else:
            # Conditional Logic
            if guess in secretWord:
                if guess in lettersGuessed:
                  print("Oops! You've already guessed that letter: "+word)
                  continue
                else:
                    # Generating available letters
                    lettersGuessed.append(guess)
                    availableLetters = getAvailableLetters(lettersGuessed)
                    # Fetching the incomplete word
                    word = getGuessedWord(secretWord, lettersGuessed)
                    print("Good guess: "+word)
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter: "+word)
                continue
            else:
                print("Oops! That letter is not in my word: "+word)
                # Generating available letters
                lettersGuessed.append(guess)
                availableLetters = getAvailableLetters(lettersGuessed)
                # Mistake is made
                mistakesMade += 1
                continue

        if isWordGuessed(secretWord, lettersGuessed):
            print("-----------")
            print("Congratulations, you won!")
            break

    if mistakesMade == 0:
        print("-----------")
        print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
