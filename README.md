# Mini-Game Collection: Hangman, WordMax, and Unscramble

**Author:** Lillian Kager  
**Course:** CSCI 203 — Professor Havill  
**Date:** November 2024

## Description

This project is a collection of three word-based mini-games implemented in Python using the Turtle graphics module. Players can choose between Hangman, WordMax, and Unscramble through an interactive main menu.

The games combine text processing, random word selection, user input validation, and graphical displays.

## Games

### Hangman
Guess a randomly selected word one letter at a time. Each incorrect guess draws another part of the hangman. Try to guess the entire word before all ten parts are drawn!

- Choose a difficulty level: Easy, Medium, or Hard.
- Correctly guessed letters appear in their positions in the word.
- Incorrect guesses are tracked and displayed.
- Win by guessing the word before running out of attempts.

### WordMax
Use a randomly selected set of letters to create valid words and earn points.

- Choose a difficulty level to determine the number of available letters.
- The game includes at least one vowel in the selected letters.
- Enter five unique words using only the available letters.
- Words must appear in the provided text file.
- Earn points based on Scrabble letter values.

### Unscramble
Guess the original word from a shuffled arrangement of its letters.

- Choose a difficulty level to determine the word length.
- A random word is selected and its letters are shuffled.
- Enter guesses of the correct length.
- You have up to five attempts to guess the word.
- The game displays whether you win or run out of attempts.

## Requirements

- Python 3
- Python Turtle graphics module
- A text file containing at least 1,000 words (the provided `words.txt` dictionary file is recommended)

The `turtle` module is included with most standard Python installations. It requires a graphical environment to display the game windows.

## How to Run

1. Download or clone the project files.
2. Make sure the required dictionary text file is available.
3. Open a terminal in the project directory.
4. Run the Python script:

   ```bash
   python3 filename.py
   ```

   Replace `filename.py` with the name of the Python script.

5. Follow the prompts in the terminal to select a game and difficulty.
6. Enter `done` in the main menu to exit the program.

## Difficulty Levels

| Difficulty | Hangman Word Length | WordMax Letters | Unscramble Word Length |
|---|---|---|---|
| Easy | 3–4 letters | 10 | 3–4 letters |
| Medium | 5–6 letters | 8 | 5–6 letters |
| Hard | 7–10 letters | 6 | 7–10 letters |

## Implementation Details

The project uses several helper functions to process text and manage gameplay:

- **Text processing:** Removes punctuation, normalizes text, and splits text into word tokens.
- **Random selection:** Chooses words and letters based on the selected difficulty.
- **Input validation:** Checks guesses against game rules and dictionary contents.
- **Scoring:** Calculates WordMax scores using Scrabble letter values.
- **Graphics:** Uses Turtle to draw game screens, letters, the hangman, and win/loss displays.

## Notes

- Enter valid game names and difficulty choices when prompted.
- The dictionary file must contain enough words to support random word selection and gameplay.
- Game progress and scores are not saved between sessions.

## Acknowledgments

Developed as a CSCI 203 project with Professor Havill.
