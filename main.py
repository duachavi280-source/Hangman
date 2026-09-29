import random


stages = [

'''
 +-------+
    |    |
    O    |
   /|\\   |
    |    |
   / \\   |
=============
''',

'''
 +-------+
    |    |
    O    |
   /|\\   |
    |    |
   /     |
=============
''',

'''
 +-------+
    |    |
    O    |
   /|\\   |
    |    |
         |
=============
''',

'''
 +-------+
    |    |
    O    |
   /|\\   |
         |
=============
''',

'''
 +-------+
    |    |
    O    |
   /|    |
         |
=============
''',

'''
 +-------+
    |    |
    O    |
    |    |
         |
=============
''',

'''
 +-------+
    |    |
    O    |
         |
         |
=============
''',

'''
 +-------+
    |    |
         |
         |
         |
=============
''',

'''
 +-------+
         |
         |
         |
         |
=============
'''
]



word_list = [

    "PYTHON",
    "CODING",
    "PROGRAM",
    "ARRAYS",
    "FUNCTIONS",
    "COMMANDS",
    "DATABASE",
    "RECURSION",
    "SYNTAX",
    "DEVELOPMENT",
    "BOOLEAN",
    "COMPILER",
    "PARAMETER",
    "ENCRYPTION",
    "ITERATION",
    "DEBUGGING",
    "INTERPRETER",
    "INSTALLATION",
    "SPECIALIZATION",
    "PSEUDOCODE",
    "ALGORITHM",
    "VARIABLE",
    "OPERATOR",
    "SOFTWARE",
    "HARDWARE",
    "COMPUTER",
    "NETWORK",
    "INTERNET",
    "SERVER",
    "BROWSER",
    "WEBSITE",
    "APPLICATION",
    "SECURITY",
    "FIREWALL",
    "PASSWORD",
    "PROCESSOR",
    "MEMORY",
    "KEYBOARD",
    "MONITOR",
    "WIRELESS",
    "BLUETOOTH",
    "STORAGE",
    "DIGITAL",
    "TECHNOLOGY",
    "ARTIFICIAL",
    "INTELLIGENCE",
    "MACHINE",
    "LEARNING",
    "DATASET",
    "NEURAL",
    "NETWORKING",
    "PREDICTION",
    "CLASSIFICATION",
    "REGRESSION",
    "TRAINING",
    "FEATURE",
    "MODEL",
    "SUPERVISED",
    "UNSUPERVISED",
    "CLUSTERING",
    "ACCURACY",
    "DETECTION",
    "AUTOMATION",
    "ROBOTICS",
    "COMPUTATION",
    "INFORMATION",
    "TECHNICAL",
    "SOFTWARE",
    "PROGRAMMING",
    "VARIABLES",
    "ALGORITHM",
    "FLOWCHART",
    "PSEUDOCODE",
    "FUNCTION",
    "ARGUMENT",
    "GITHUB",
    "TERMINAL",
    "APPLICATION",
    "DEVELOPER",
]

total_score = 0

round_score = 0

winning_streak = 0

best_streak = 0

games_played = 0

games_won = 0

games_lost = 0



def show_title():
    print("==========================================")
    print("              HANGMAN GAME")
    print("==========================================")



def show_main_menu():
    print("==========================================")
    print("              MAIN MENU")
    print("==========================================")
    print("1. Start Game")
    print("2. Instructions")
    print("3. View Score")
    print("4. Exit")



def show_instructions():
    print("==========================================")
    print("             INSTRUCTIONS")
    print("==========================================")
    print("1. The computer selects a random word.")
    print("2. The selected word is related to programming or technology.")
    print("3. The word is displayed using underscores.")
    print("4. Guess one letter at a time.")
    print("5. If your guessed letter is correct,it will appear in the word.")
    print("6. If your guessed letter is wrong,you will lose one life.")
    print("7. You have 8 lives at the beginning.")
    print("8. The Hangman drawing changes after wrong guesses.")
    print("9. Guess the complete word before losing all your lives.")
    print("10. Winning gives you a round score.")
    print("11. Your round score is added to your total score.")
    print("12. Consecutive wins increase your winning streak.")
    print("13. Losing a game resets the current winning streak.")
    print("14. Your best winning streak is saved during the current program session.")
    print("15. Choose option 4 from the main menu whenever you want to exit.")

def view_score():

    global total_score
    global winning_streak
    global best_streak
    global games_played
    global games_won
    global games_lost

    print("==========================================")
    print("                SCORE")
    print("==========================================")
  
    print("Total Score       :", total_score)
    print("Current Streak    :", winning_streak)
    print("Best Streak       :", best_streak)
    print("Games Played      :", games_played)
    print("Games Won         :", games_won)
    print("Games Lost        :", games_lost)
    if games_played > 0:

        win_percentage = (games_won / games_played) * 100

        print("Win Percentage    :",round(win_percentage, 2),"%")

    else:
        print("Win Percentage    : 0%")



def display_word(display):
    print("Word:", end=" ")

    for letter in display:

        print(letter, end=" ")


def display_lives(lives):
    print("Lives Left:", lives)



def display_guessed_letters(guessed_letters):
    if len(guessed_letters) == 0:
        print("Guessed Letters: None")

    else:
        print("Guessed Letters:",", ".join(sorted(guessed_letters)))



def get_valid_letter():

    while True:

        guessed_letter = input(
            "Guess a Letter: "
        ).upper().strip()

        if len(guessed_letter) == 0:

            print()
            print("You did not enter anything.")
            print("Please enter one letter.")

        elif len(guessed_letter) > 1:
            print("Please enter only ONE letter.")

        elif not guessed_letter.isalpha():
            print("Please enter an alphabetic letter.")

        else:
            return guessed_letter


def check_repeated_letter(
    guessed_letter,
    guessed_letters
):

    if guessed_letter in guessed_letters:

        print("You already guessed this letter.")

        return True

    return False




def create_display(chosen_word):

    display = []

    for i in range(len(chosen_word)):

        display.append("_")

    return display


def check_letter(chosen_word,display,guessed_letter):

    correct_guess = False

    for position in range(len(chosen_word)):

        letter = chosen_word[position]

        if letter == guessed_letter:

            display[position] = guessed_letter

            correct_guess = True

    return correct_guess



def check_win(display):

    if "_" not in display:

        return True

    return False


def calculate_score(lives):

    score = 100 + (lives * 10)

    return score

def show_round_result(score,won,chosen_word):

    if won:

        print("YOU WIN!")
        print("The word was:", chosen_word)
        print("Round Score:", score)

    else:

        print("  GAME OVER!")

        print("The word was:", chosen_word)

        print("Round Score:", score)



def start_game():

    global total_score
    global round_score
    global winning_streak
    global best_streak
    global games_played
    global games_won
    global games_lost

    print("==========================================")
    print("              STARTING GAME")
    print("==========================================")

    chosen_word = random.choice(word_list)

    lives = 8


    display = create_display(chosen_word)

    guessed_letters = []


    game_over = False

    won = False


    round_score = 0

    display_word(display)


    print(stages[lives])

    while not game_over:

        display_lives(lives)

        display_guessed_letters(guessed_letters)

        guessed_letter = get_valid_letter()

        if check_repeated_letter(guessed_letter,guessed_letters):

            continue

        guessed_letters.append(guessed_letter)

        correct_guess = check_letter(
            chosen_word,
            display,
            guessed_letter)


        if correct_guess:
            print("Correct Guess!")

            display_word(display)

        else:
            print("Wrong Guess!")
            lives -= 1
            print("You lost one life.")
            print("Lives Left:",lives)

        print(stages[lives])

        if check_win(display):

            game_over = True

            won = True

            print("The complete word is:")

            display_word(display)

            print("Congratulations!")

        elif lives == 0:

            game_over = True

            won = False

            print("You have lost all your lives.")

            print("The correct word was:",chosen_word)

        else:
            print("Keep Guessing!")


    games_played += 1

    if won:

        games_won += 1

        round_score = calculate_score(lives)

        total_score += round_score

        winning_streak += 1

        if winning_streak > best_streak:

            best_streak = winning_streak

        print("==========================================")
        print("              ROUND RESULT")
        print("==========================================")

        print("Round Score:",round_score)

        print("Total Score:",total_score)
        print("Winning Streak:",winning_streak)

        print("Best Winning Streak:",best_streak)

    else:

        games_lost += 1

        round_score = 0

        winning_streak = 0

        print("==========================================")
        print("              ROUND RESULT")
        print("==========================================")

        print("Round Score:", round_score)
        print("Total Score:",total_score)

        print("Winning Streak:",winning_streak)

        print("Best Winning Streak:",best_streak)
    print("Returning to Main Menu...")

    return round_score



def main_menu():

    while True:
        show_main_menu()
        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            start_game()

        elif choice == "2":
            show_instructions()

        elif choice == "3":
            view_score()

        elif choice == "4":
            print("==========================================")
            print("              FINAL SCORE")
            print("==========================================")

            print("Total Score:",total_score)
            print("Best Winning Streak:",best_streak)
            print("Games Played:",games_played)
            print("Games Won:",games_won )
            print("Games Lost:",games_lost)
            print("Thank You For Playing Hangman!")
            break

        else:
            print("Invalid Choice!")
            print("Please enter 1, 2, 3 or 4." )

show_title()
print("Welcome to the Programming Hangman Game!")
main_menu()