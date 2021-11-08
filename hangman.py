# ----------------------------------------------------------
# --------          HW 7: wheel of fortune         ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Macdonald Chirara
# Time spent on this problem: 3
#
# Collaborators and sources:
#   (List any collaborators or sources here.)
#Python hangman Youtube video https://www.youtube.com/watch?v=5x6iAKdJB6U
# ----------------------------------------------------------

# Complete the code below for wheel of fortune

import doctest
import random


def randomword():
    """
    This function is where the random words are generated.
    >>> get random word
    spring
    >>> get random word
    leaves
    >>> get random word
     mud
    >>> get random word
      windy
    >>> get random word
    rainy
    """
    words = ['spring', 'leaves', 'warm', 'mud', 'sunny', 'windy', 'rainy']
    secret = random.choice(words)
    print("For testing, the secret word is", secret)
    return secret


hang = ["_______", "_______", "_______", "_______", "_______"]


def gameplay(hang, missedLetters, correctLetters, secretWord):
    """"
    This function allows the keeping in track of the missed letters and also the corect
    letters.It also allows the blanks to be replaced with the correct letters.
    >>> ["_______", "_______", "_______", "_______", "_______"], edfr, w,windy
    _______
    Missed Letters: edfr
    >>> ["_______", "_______", "_______", "_______", "_______"], qzx, s,sunny
    _______
    Missed Letters: qzx
    """

    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")


def getGuess(alreadyGuessed):
    """
    This function takes the user input guessed letter.
    param: string
    return: string
    >>>Guess a letter: a
    a
    >>>Guess a letter: 3
    Please enter a LETTER
    >>>Guess a letter: boy
    Please enter a single letter
    >>>Guess a letter: a
    You have already guessed that letter. Choose again.
    """
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def onegame():
    """"
    This is a  function to tie together the other functions
    and coordinate playing one game of wheel of fortune
    """
    return ("\nThe game is over, thank you for playing. ")


missedLetters = ''
correctLetters = ''
secretWord = randomword()
gameIsDone = False

while True:
    gameplay(hang, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The secret word is "' +
                  secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hang) - 1:
            gameplay(hang, missedLetters,
                     correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                  str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if onegame():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = randomword()
        else:
            break

doctest.testmod()