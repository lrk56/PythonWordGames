'''
Title: Mini-Game Collection: Hangman, WordMax, and Unscramble

Author: Lillian Kager

Class: CSCI 203 With Professor Havill

Description: This script contains a collection of mini-games implemented using
the Turtle graphics module. It includes games such as Hangman,
WordMax, and Unscramble where players can guess letters and words.

Date: November 2024
'''
import string
import turtle
import random
def removePunctuation(text):
    """Remove punctuation from a text.
    Parameter:

    text: a string object

    Return value: a copy of text with punctuation removed
    """
    newText = ''
    for character in text:
        if character not in string.punctuation:
            newText = newText + character
    return newText
def normalize(text):
    """Normalize a text by making it lowercase and removing punctuation.
    Parameter:

    text: a string object

    Return value: a normalized copy of text

    """
    newText = text.lower()
    newText = removePunctuation(newText)
    return newText
def splitIntoWords(text):
    """Split a text into words.
    Parameter:

    text: a string object

    Return value: the list of words in the text
    """
    wordList = []
    prevCharacter = ' '
    word = ''
    for character in text:
        if character not in string.whitespace:
            word = word + character
        elif prevCharacter not in string.whitespace:
            wordList.append(word)
            word = ''
        prevCharacter = character
    if word != '':
        wordList.append(word)
    return wordList
def wordTokens(text):
    """Break a text into words with punctuation removed.
    Parameter:

    text: a string object

    Return value: a list of word tokens

    """
    newText = normalize(text)
    tokens = splitIntoWords(newText)
    return tokens
def mainMenu():
    """
    Display a main menu for a collection of mini-games and handle user input for selecting a game or exiting.

    Parameters:
    None

    Return value:
    A string: the name of the game chosen by the user.

    The function loops until the user makes a choice. Valid choices include:
    - 'wordmax': Wordmax.
    - 'hangman': Hangman.
    - 'unscramble': Unscramble.
    - 'info': Displays information about the games.
    - 'done': Exits the program.

    """
    while True:
        gamechosen = input('Hello! Welcome to the mini-game collection.\n'
                           'Would you like to play WordMax ("wordmax"), Hangman ("hangman"), or Unscramble ("unscramble")?\n'
                           'If you need more information about each game, enter "info".\n'
                           'To exit the program, enter "done": ').lower().strip()
        if gamechosen == 'wordmax' or gamechosen == 'hangman' or gamechosen == 'unscramble':
            return gamechosen
        elif gamechosen == 'info':
            print('Hangman: Guess the hidden word by suggesting letters before you run out of chances.\n'
                  'WordMax: Choose how many random letters you want to work with, then make the highest-scoring words possible within five guesses.\n'
                  'Unscramble Word: Rearrange the mixed-up letters to form a valid word.\n')
        elif gamechosen == 'done':
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print('Uh oh! That is not a valid option. Please enter "wordmax", "hangman", "unscramble", "info", or "done".')
def gameTextFile():
    """
    Prompt the user for a txt file and make sure that it contains at least 100 words.

    Parameters:
    None

    Return value:
    list: A list of words extracted from the txt file.

    The function asks the user to input a file name until a file is provided
    that contains at least 100 words. It reads the file, turns the text into
    words, and returns the list of words.

    If the provided file is 100 or more words long, the function will print the number of words in the file.
    """
    text=''
    while len(text)<100:
        fileName = input('These games require a txt file with at least 1000 words in it.\nWe recommend that you choose the provided "words.txt" dictionary file.\nPlease enter the file name here:')
        textFile = open(fileName, 'r', encoding = ' utf-8')
        text=wordTokens(textFile.read())
        if len(text)>=1000:
            print('Perfect! Your text file is',len(text),'words long.')
            return text   
    textFile.close()
def prepGameScreen(word_length):
    screen = turtle.Screen()
    screen.bgcolor("LightSkyBlue")
    turtle.speed(5)     
    turtle.pensize(5)  
    if word_length==3:
        startingposition=-90
    elif word_length==4:
        startingposition=-120
    elif word_length==5:
        startingposition=-150
    elif word_length==6:
        startingposition=-180
    elif word_length==7:
        startingposition=-210
    elif word_length==8:
        startingposition=-240
    elif word_length==9:
        startingposition=-270
    else:
        startingposition=-300
    turtle.penup()
    turtle.goto(startingposition, 250)
    turtle.pendown()
    for dash in range(word_length):
        turtle.forward(40)  
        turtle.penup()
        turtle.forward(20)  
        turtle.pendown()
    return startingposition
def guess1():
    """
    Draws the base of the hangman setup.

    Parameters:
    None
    """
    turtle.speed(5)     
    turtle.pensize(30) 
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(-80,-300)
    turtle.pendown()
    turtle.forward(150)
def guess2():
    """
    Draws the pole of the hangman setup.

    Parameters:
    None
    """
    turtle.speed(5)     
    turtle.pensize(20) 
    turtle.penup()
    turtle.setheading(90)
    turtle.goto(-5,-300)
    turtle.pendown()
    turtle.forward(415)
def guess3():
    """
    Draws the first part of the hook of the hangman setup.

    Parameters:
    None
    """
    turtle.speed(5)     
    turtle.pensize(20) 
    turtle.penup()
    turtle.setheading(180)
    turtle.goto(-5,120)
    turtle.pendown()
    turtle.forward(110)
def guess4():
    """
    Draws the second part of the hook of the hangman setup.

    Parameters:
    None
    """
    turtle.speed(5)     
    turtle.pensize(20) 
    turtle.penup()
    turtle.setheading(270)
    turtle.goto(-120,120)
    turtle.pendown()
    turtle.forward(30)
def guess5():
    """
    Draws the hangman head.

    Parameters:
    None
    """
    turtle.speed(5)     
    turtle.pensize(8) 
    turtle.penup()
    turtle.goto(-133,5)
    turtle.pendown()
    turtle.setheading(340)
    turtle.circle(40)
def guess6():
    """
    Draws the hangman body.

    Parameters:
    None
    """
    turtle.speed(5)     
    turtle.pensize(8) 
    turtle.penup()
    turtle.goto(-117.9,3)
    turtle.pendown()
    turtle.setheading(270)
    turtle.forward(85)
def guess7():
    """
    Draws the hangman first arm.

    Parameters:
    None
    """
    turtle.speed(5)     
    turtle.pensize(8) 
    turtle.penup()
    turtle.goto(-117.9,-10)
    turtle.pendown()
    turtle.setheading(230)
    turtle.forward(55)
def guess8():
    """
    Draws the hangman second arm.

    Parameters:
    None
    """
    turtle.speed(5)     
    turtle.pensize(8) 
    turtle.penup()
    turtle.goto(-117.9,-10)
    turtle.pendown()
    turtle.setheading(310)
    turtle.forward(55)
def guess9():
    """
    Draws the hangman first leg.

    Parameters:
    None
    """
    turtle.speed(5)     
    turtle.pensize(8) 
    turtle.penup()
    turtle.goto(-117.9,-85)
    turtle.pendown()
    turtle.setheading(310)
    turtle.forward(55)
def guess10():
    """
    Draws the hangman second leg.

    Parameters:
    None
    """
    turtle.speed(5)     
    turtle.pensize(8) 
    turtle.penup()
    turtle.goto(-117.9,-85)
    turtle.pendown()
    turtle.setheading(230)
    turtle.forward(55)
def gameover():
    global game_over
    game_over=True
    """
    Display a game over screen when the player runs out of guesses using the turtle library.

    Parameters:
    None

    Return value:
    None

    """
    turtle.hideturtle()
    sizecount=15
    turtle.speed(3)      
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    for i in range(20):
        sizecount+=5
        turtle.color('red')
        style = ('Courier', sizecount, 'bold')
        turtle.write('GAME OVER', font=style, align='center')
        turtle.color('DarkRed')
        style = ('Courier', sizecount, 'bold')
        turtle.write('GAME OVER', font=style, align='center')
    turtle.color('red')
    turtle.write('GAME OVER', font=style, align='center')
    turtle.speed(5)
    turtle.penup()
    turtle.pensize(8)
    turtle.goto(-300,-10)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()
    turtle.goto(-300,125)
    turtle.pendown()
    turtle.forward(600)
def winningScreen():
    """
    Display a winning screen when the player wins the game using the turtle library.

    Parameters:
    None

    Return value:
    None

    """
    turtle.hideturtle()
    sizecount=15
    turtle.speed(3)      
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    for i in range(20):
        sizecount+=5
        turtle.color('green')
        style = ('Courier', sizecount, 'bold')
        turtle.write('YOU WIN!', font=style, align='center')
        turtle.color('DarkGreen')
        style = ('Courier', sizecount, 'bold')
        turtle.write('YOU WIN!', font=style, align='center')
    turtle.color('green')
    turtle.write('YOU WIN!', font=style, align='center')
    turtle.speed(5)
    turtle.penup()
    turtle.pensize(8)
    turtle.goto(-300,-10)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()
    turtle.goto(-300,125)
    turtle.pendown()
    turtle.forward(600)
def letterspot(startingposition):
    """
    Returns 10 x-positions for drawing letters, spaced 60 units apart.

    Args:
        startingposition (int): The x-coordinate of the first letter's position.

    Returns:
        tuple: 10 x-positions for the letters.
    """
    spot1=startingposition+20
    spot2=spot1+60
    spot3=spot2+60
    spot4=spot3+60
    spot5=spot4+60
    spot6=spot5+60
    spot7=spot6+60
    spot8=spot7+60
    spot9=spot8+60
    spot10=spot9+60
    return spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,spot10
def drawLetter(letter,letterspot):
    """
    Draws the correctly guessed letter at a specified position on the screen.

    This function is used to display the letter the player guessed correctly at
    a given location on the Turtle graphics screen.

    Parameters:
        letter (str): The letter to be drawn on the screen.
        letterspot (int): The x-coordinate of the position where the letter will be drawn.

    """
    turtle.penup()
    turtle.goto(letterspot,245)
    turtle.pendown()
    style = ('Courier', 45, 'bold')
    turtle.write(letter, font=style, align='center')
def revealword(word):
    """
    Displays the given word on the screen using the Turtle graphics module.

    The function draws a blue line at the top of the screen and then displays
    a message ("The word was:") followed by the provided word in black text.

    Parameters:
        word (str): The word to display.
    """
    turtle.penup()
    turtle.goto(-300,200)
    turtle.setheading(0)
    turtle.pendown()
    turtle.pensize(1100)
    turtle.color('LightSkyBlue')
    turtle.forward(800)
    turtle.penup()
    turtle.goto(-5,200)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color('black')
    style = ('Courier', 30)
    turtle.write('The word was:', font=style, align='center')
    turtle.penup()
    turtle.goto(0-len(word),170)
    turtle.pendown()
    turtle.color('black')
    style = ('Courier', 35,'bold')
    turtle.write(word,font=style, align='center')
startingloc=-100
game_over=False
def addToLetterList(letter):
    """
    Adds a guessed letter to the list of letters displayed on the screen.

    The function checks if the game is over. If not, it updates the screen by
    displaying the text "Letters Guessed:" and then adds the new letter to the
    list of previously guessed letters, updating its position on the screen.

    Parameters:
        letter (str): The letter to be added to the list of guessed letters.
    """
    global startingloc, game_over
    if game_over==True:
        return
    turtle.penup()
    turtle.goto(-5,200)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color('black')
    style = ('Courier', 30)
    turtle.write('Letters Guessed:', font=style, align='center')
    turtle.penup()
    turtle.goto(startingloc,170)
    turtle.pendown()
    turtle.color('black')
    style = ('Courier', 20,'bold')
    turtle.write(letter,font=style, align='center')
    startingloc+=10
def pickDifficulty():
    difficulty = '  '
    while difficulty not in ['m', 'e', 'h','H','E','M']:
        difficulty = input("What difficulty would you like the game to be?\nEasy='e'\nMedium='m'\nHard='h'\n")
    return difficulty
def randWordPick(difficulty):
    """
    Selects a random word from a predefined list based on the chosen difficulty level.

    Picks a random word from a list of words that match the selected difficulty. The
    difficulty affects the length of the word to be selected.

    Returns:
        str: A randomly chosen word from the list of words that match the selected difficulty.
    """
    text = gameTextFile()
    if difficulty == 'e' or difficulty == 'E':
        wordLength = random.randint(3, 4)
    elif difficulty == 'm' or difficulty == 'M':
        wordLength = random.randint(5, 6)
    else:
        wordLength = random.randint(7, 10)
    possibleWords = [word.lower() for word in text if len(word) == wordLength]
    randWord = random.choice(possibleWords)
    return randWord
def hangMan():
    turtle.reset()
    difficulty=pickDifficulty()
    randWord=randWordPick(difficulty)
    wordGuess = ['_'] * len(randWord)
    wordDict = []
    guesscounter = 0
    letterGuess = ''
    startingPosition = prepGameScreen(len(randWord)) 
    spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9, spot10 = letterspot(startingPosition)  
    while ''.join(wordGuess) != randWord and guesscounter < 10:
        letterGuess = ''
        while not letterGuess.isalpha() or len(letterGuess) != 1:
            letterGuess = input("What letter would you like to guess? It must be a single letter: ").lower()
            if not letterGuess.isalpha() or len(letterGuess) != 1:
                print("Invalid input. Please enter a single letter.")
        if letterGuess not in randWord:
            guesscounter += 1
            if guesscounter == 1:
                guess1()
            elif guesscounter == 2:
                guess2()
            elif guesscounter == 3:
                guess3()
            elif guesscounter == 4:
                guess4()
            elif guesscounter == 5:
                guess5()
            elif guesscounter == 6:
                guess6()
            elif guesscounter == 7:
                guess7()
            elif guesscounter == 8:
                guess8()
            elif guesscounter == 9:
                guess9()
            elif guesscounter == 10:
                guess10()
                gameover()
                revealword(randWord)
        letterlist=[]
        if letterGuess not in letterlist:
            letterlist.append(letterGuess)
            addToLetterList(letterGuess)
        if letterGuess not in wordDict:
            wordDict.append(letterGuess)
            print('These are the guesses you have entered:', wordDict)
            for index in range(len(randWord)):
                if randWord[index] == letterGuess:
                    wordGuess[index] = letterGuess
                    if index == 0:
                        drawLetter(letterGuess, spot1)
                    elif index == 1:
                        drawLetter(letterGuess, spot2)
                    elif index == 2:
                        drawLetter(letterGuess, spot3)
                    elif index == 3:
                        drawLetter(letterGuess, spot4)
                    elif index == 4:
                        drawLetter(letterGuess, spot5)
                    elif index == 5:
                        drawLetter(letterGuess, spot6)
                    elif index == 6:
                        drawLetter(letterGuess, spot7)
                    elif index == 7:
                        drawLetter(letterGuess, spot8)
                    elif index == 8:
                        drawLetter(letterGuess, spot9)
                    elif index == 9:
                        drawLetter(letterGuess, spot10)
        print("Current word: ", ''.join(wordGuess))
    if ''.join(wordGuess) == randWord:
        print(f'Congratulations! You guessed the word in {guesscounter} tries!')
        winningScreen()
def canMakeWord(letters,text):
    """
    Checks if there are at least 50 words in the text that can be made using only the given letters.

    Args:
        letters (list): List of allowed letters.
        text (list): List of words to check.

    Returns:
        boolean: True if 50 or more valid words are found, otherwise False.
    """
    validwordcount = 0
    for word in text:
        word = word.strip().lower()
        valid = True
        for char in word:
            if char not in letters:
                valid = False
                break
        if valid:
            validwordcount += 1
    if validwordcount >= 50:
        return True
    else:
        return False
def pickLetters():
    """
    Selects a random set of letters based on difficulty and ensures:
    - At least one vowel is included.
    - The letters can form valid words.

    Difficulty levels:
    - 'e' or 'E': 10 letters
    - 'm' or 'M': 8 letters
    - Any other input: 6 letters

    Returns:
        tuple: (chosenLetters, letters)
            chosenLetters: list of selected letters
            letters: number of letters selected
    """
    text = gameTextFile()
    difficulty=pickDifficulty()
    vowels=['a','e','i','o','u']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if difficulty == 'e' or difficulty == 'E':
        letters = 10
  
    elif difficulty == 'm' or difficulty == 'M':
        letters = 8
    
    else:
        letters = 6
    vowelPresent = False
    validWordsFound=False
    while vowelPresent == False or validWordsFound == False:
        chosenLetters = random.sample(alphabet, letters)
        for letter in chosenLetters:
            if letter in vowels:
                vowelPresent = True
        if canMakeWord(chosenLetters,text)==True:
            validWordsFound=True
    return chosenLetters,letters,text
def drawWord(word,guessnum):
    """
    Draws the word, guess number, and points on the screen using Turtle graphics.

    This function displays the word, its corresponding guess number, and the points
    in a specified position on the screen for each guess.

    Parameters:
        word (str): The word to be displayed.
        guessnum (int): The current guess number (1 through 5).
        points (int): The points for the word (not used in this function, but part of the parameters).
    """
    if guessnum==1:
        startingpos=200
    elif guessnum==2:
        startingpos=160
    elif guessnum==3:
        startingpos=120
    elif guessnum==4:
        startingpos=80
    elif guessnum==5:
        startingpos=40
    guessnum=str(guessnum)
    turtle.penup()
    turtle.goto(-90,startingpos)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color('black')
    style = ('Courier', 30)
    turtle.write('Word Number',font=style, align='center')
    turtle.penup()
    turtle.forward(120)
    turtle.pendown()
    turtle.write(guessnum,font=style, align='center')
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    turtle.write(':',font=style, align='center')
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    turtle.write(word,font=style, align='left')
def drawUnscrambleLetters(word, guessnum, correct):
    """
    Draws the word with colored letters based on whether they are correct or incorrect.

    Parameters:
        word (str): The word being guessed.
        guessnum (int): The current guess number (1 through 5).
        correct (list): A list of booleans where True indicates a correct letter, False indicates an incorrect letter.

    Returns:
        None
    """
    if guessnum == 1:
        startingpos = 200
    elif guessnum == 2:
        startingpos = 160
    elif guessnum == 3:
        startingpos = 120
    elif guessnum == 4:
        startingpos = 80
    elif guessnum == 5:
        startingpos = 40
    guessnum = str(guessnum)
    turtle.penup()
    turtle.goto(-90, startingpos)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color('black')
    style = ('Courier', 30)
    turtle.write('Word Number', font=style, align='center')
    turtle.penup()
    turtle.forward(120)
    turtle.pendown()
    turtle.write(guessnum, font=style, align='center')
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    turtle.write(':', font=style, align='center')
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    for index, letter in enumerate(word):
        if correct[index]:
            turtle.color('green')
        else:
            turtle.color('red')
        turtle.write(letter, font=style, align='left')
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
def pointcount(guesses):
    """
    Calculates the total  score for a list of guesses using Scrabble score rules.

    Each letter's score is based on Scrabble letter values. The function sums
    the points for all letters in the given words.

    Parameters:
        guesses (list of str): A list of words to calculate the total score for.

    Returns:
        int: The total Scrabble score for the input words.
    """
    pointdict = {}
    for letter in 'aeioulnstr':
        pointdict[letter] = 1
    for letter in 'dg':
        pointdict[letter] = 2
    for letter in 'bcmp':
        pointdict[letter] = 3
    for letter in 'fhvwy':
        pointdict[letter] = 4
    pointdict['k'] = 5
    for letter in 'jx':
        pointdict[letter] = 8
    for letter in 'qz':
        pointdict[letter] = 10
    points=0
    for word in guesses:
        for char in word:
            points+=pointdict.get(char,0)
    return points
def getWord(letterlist,text,guesses):
    '''
    Prompts the user to input a valid word based on the following criteria:
    - The word must be composed of letters from the provided letter list.
    - The word must exist in the given text (dictionary or word list).
    - The word must not have been guessed before.

    The function keeps prompting the user until a valid word is entered.

    Parameters:
        letterlist (list of str): A list of allowed letters for the word.
        text (str or list): A text or word list containing valid words.
        guesses (list of str): A list of previously guessed words.

    Returns:
        string: The valid word entered by the user.
    '''
    wordguess = ''
    inletterlist = False
    indictfile = False
    inpreviousguesses = False
    while not inletterlist or not indictfile or inpreviousguesses:
        wordguess = input('What word do you want to enter? ').strip().lower()
        inletterlist = True
        for char in wordguess:
            if char not in letterlist:
                inletterlist = False
        indictfile = wordguess in text
        inpreviousguesses = wordguess in guesses
        if not inletterlist:
            print("Oops! Looks like you entered a letter that isn't in your letter list.\nTry again.")
        if not indictfile:
            print("This is not a valid word! Try again.")
        if inpreviousguesses:
            print("You've already guessed that word! Try a different one.") 
    return wordguess
def drawPoints(points):
    '''
    Draws the points on the screen with an increasing font size.

    The function displays the word "POINTS:" and the value of the points,
    gradually increasing the font size for visual effect. It also draws
    two horizontal lines at the bottom and top of the screen.

    Parameters:
        points (int): The points value to be displayed on the screen.
    '''
    turtle.speed(500)
    turtle.hideturtle()
    sizecount=70
    turtle.penup()
    turtle.setposition(-50,-200)
    turtle.pendown()
    for i in range(10):
        sizecount+=5
        turtle.color('LimeGreen')
        style = ('Courier', sizecount, 'bold')
        turtle.write('POINTS:', font=style, align='center')
        turtle.penup()
        turtle.setposition(250, -200)
        turtle.pendown()
        turtle.write(str(points), font=style, align='center')
        turtle.penup()
        turtle.setposition(-50,-200)
        turtle.pendown()
        turtle.color('Darkgreen')
        style = ('Courier', sizecount, 'bold')
        turtle.write('POINTS:', font=style, align='center')
        turtle.penup()
        turtle.setposition(250, -200)
        turtle.pendown()
        turtle.write(str(points), font=style, align='center')
        turtle.penup()
        turtle.setposition(-50,-200)
        turtle.pendown()  
    turtle.color('LimeGreen')
    turtle.write('POINTS:', font=style, align='center')
    turtle.penup()
    turtle.setposition(250, -200)
    turtle.pendown()
    turtle.write(str(points), font=style, align='center')
    turtle.speed(5)
    turtle.penup()
    turtle.pensize(8)
    turtle.goto(-300,-210)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()
    turtle.goto(-300,-75)
    turtle.pendown()
    turtle.forward(600)
def wordMax():
    turtle.reset()
    '''
    Manages the word max game:
    - Picks letters for the game.
    - Prepares the game screen.
    - Allows the user to guess words and draws them on the screen.
    - Calculates and displays the total score based on guesses.
    '''
    guesses=[]
    letterlist,lettercount,text=pickLetters()
    startingPosition = prepGameScreen(lettercount) 
    spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9, spot10 = letterspot(startingPosition)
    for index in range(lettercount):
        letter=letterlist[index]
        drawLetter(letter,letterspot(startingPosition)[index])
    for count in range(1,6):
        wordguess=getWord(letterlist,text,guesses)
        guesses.append(wordguess)
        drawWord(wordguess,count)
    points=pointcount(guesses)
    drawPoints(points)
def wordShuffler(word):
    """
    Shuffles the letters in a word and returns a new word that is different from the original.

    Parameters:
        word (str): The word to shuffle.

    Returns:
        str: A new word with shuffled letters.
    """
    shuffledWord=word
    while shuffledWord == word:
        wordList=list(word)
        random.shuffle(wordList)
        shuffledWord=''.join(wordList)
    return shuffledWord
def checkandGetGuess(randWord):
    """
    Prompts the user to guess a word until they either guess correctly or exhaust their attempts.

    Parameters:
        randWord (str): The word the user needs to guess.

    Returns:
        None
    """
    guess = ''
    guessnum = 0
    word_length = len(randWord)
    while guessnum < 5:
        guessnum += 1
        guess = input(f"Guess {guessnum}/5: ").strip()
        if len(guess) != word_length:
            print(f"Try again! The word must be {word_length} letters long.")
            guessnum -=1
            continue
        correct = [False] * word_length
        for index in range(word_length):
            if guess[index].lower() == randWord[index].lower():
                correct[index] =True 
        for index in range(word_length):
            if not correct[index]:
                if guess[index].lower() in randWord.lower() and guess[index].lower() != randWord[index].lower():
                    correct[index]=False 
        drawUnscrambleLetters(guess, guessnum, correct)
        if guess.lower() == randWord.lower():
            winningScreen()
            return
        if guessnum == 5:
            revealword(randWord)
            gameover()
            return
def unScramble():
    """
    Starts and runs a word unscrambling game where the user has to guess the original word.

    The function:
    - Resets the turtle graphics screen.
    - Sets the difficulty level and picks a random word based on the difficulty.
    - Shuffles the letters of the word to create a scrambled version.
    - Displays the scrambled word on the screen and allows the user to make guesses.
    - Tracks the number of guesses and checks if the user has guessed the word correctly.

    Returns:
        None
    """
    turtle.reset()
    guesses=0
    difficulty=pickDifficulty()
    randWord=randWordPick(difficulty)
    print(randWord)
    shuffledWord=wordShuffler(randWord)
    wordGuess = ['_'] * len(randWord)
    wordDict = []
    guesscounter = 0
    wordGuess = ''
    startingPosition = prepGameScreen(len(shuffledWord)) 
    spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9, spot10 = letterspot(startingPosition)
    for index in range(len(shuffledWord)):
        letter=shuffledWord[index]
        drawLetter(letter,letterspot(startingPosition)[index])
    checkandGetGuess(randWord)
def main():
    while True:
        game_choice = mainMenu()
        if game_choice == 'hangman':
            hangMan()
        elif game_choice == 'unscramble':
            unScramble()
        elif game_choice == 'wordmax':
            wordMax()
        elif game_choice == 'exit':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice, please try again.")
            continue
main()
