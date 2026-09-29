
# `statement.md`

```markdown
# Project Statement

## Project Title

Hangman Game

## 1. Problem Statement

Word guessing games require players to identify a hidden word using a limited number of attempts.

The objective of this project is to develop a simple command-line based Hangman Game using Python. The system selects a random programming or technology-related word and allows the player to guess the word one letter at a time.

The game provides feedback for correct and incorrect guesses, displays the Hangman stages, maintains the number of remaining lives, and determines whether the player wins or loses.

## 2. Proposed Solution

The proposed solution is a Python-based command-line Hangman Game.

The program contains a predefined collection of programming and technology-related words. At the beginning of every round, the computer randomly selects one word.

The selected word is displayed using underscores. The player enters one letter at a time.

Correct guesses reveal the corresponding letters. Incorrect guesses reduce the player's remaining lives and update the Hangman drawing.

The game continues until the player guesses the complete word or loses all lives.

The program also calculates scores and maintains game statistics during the current session.

## 3. Project Objectives

- To create an interactive command-line game using Python.
- To apply basic Python programming concepts.
- To implement random word selection.
- To implement input validation.
- To detect repeated guesses.
- To implement win and lose conditions.
- To create a scoring system.
- To maintain winning streaks and game statistics.
- To provide simple terminal-based interaction.

## 4. Scope of the Project

The project includes:

- Main menu
- Predefined word list
- Random word selection
- Hidden word display
- Letter-by-letter guessing
- Input validation
- Repeated letter detection
- Eight lives
- Hangman stage display
- Correct and incorrect guess handling
- Win detection
- Lose detection
- Round score calculation
- Total score calculation
- Winning streak tracking
- Best winning streak tracking
- Games played tracking
- Games won tracking
- Games lost tracking
- Win percentage calculation
- Instructions
- Final score display

The current version is designed for command-line execution and does not use a graphical interface or database.

## 5. Target Users

- Students learning Python
- Beginners learning programming
- Students interested in command-line applications
- Users who enjoy word guessing games
- Users interested in programming and technology-related vocabulary

## 6. High-Level Features

### 6.1 Main Menu

The main menu allows the player to:

1. Start Game
2. View Instructions
3. View Score
4. Exit

### 6.2 Random Word Selection

The program randomly selects a word from the predefined word list using Python's `random` module.

### 6.3 Hidden Word Display

The selected word is initially displayed using underscores.

### 6.4 Letter Guessing

The player enters one letter at a time to identify the hidden word.

### 6.5 Input Validation

The program checks whether the player has entered a valid single alphabetic character.

### 6.6 Repeated Letter Detection

The program detects letters that have already been guessed.

### 6.7 Lives System

The player starts each round with 8 lives. Each incorrect guess reduces the number of remaining lives.

### 6.8 Hangman Display

The Hangman drawing changes according to the number of remaining lives.

### 6.9 Win Detection

The player wins when all letters in the selected word have been revealed.

### 6.10 Lose Detection

The player loses when all available lives are used before the word is completely revealed.

### 6.11 Score System

The winning score is calculated using:

```text
Round Score = 100 + (Remaining Lives × 10)