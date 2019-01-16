# introduction to quiz. Allows explains test and chances for answers.
print("Hello MFFL (Mavs Fan For Life), Welcome to do you know your Dallas "
      "Mavericks is is a short quiz on history and facts about the Dallas "
      "Mavericks. You will have 3 levels in this quiz and 4 "
      "fill-in-the-blank answers per levels. you will have 5 opportunities "
      "to fill in the answer. GOOD LUCK!")

blanks = ["___1___", "___2___", "___3___", "___4___"]

answer_easy = ["1980", "Mark Cuban", "41", "Reunion"]

question_easy = "\nEasy Question: The Dallas Mavericks was founded " \
                "in ___1___ (hint:year). The current owner of the team is " \
                "billionaire ___2___(hint:He is a shark). The most popular " \
                "player in Dallas Mavericks  history wears number  " \
                "___3___(hint: German). The team's first game was played " \
                "in ___4___ Arena."

answer_medium = ["Carter", "Maverick", "Garner", "Kiki"]

question_medium = "\nMedium Question: The original owner of the team was " \
                  "Don ___1___. Forming the team was a gift to his wife. " \
                  "The team nickname was chosen after the television show " \
                  "___2___ staring Jim ___3___. The first player drafted " \
                  "by the mavericks was ___4___ Vanderweigh."

answer_hard = ["2", "Dick", "3", "6"]
question_hard = "\nThe team has been to ___1___ NBA Finals. The first " \
                "coach in team history was ___2___ Motta. Dallas has " \
                "retired ___3___ players number in the rafters. The can " \
                "also boast putting ___4___ players in the NBA Hall of Fame."

levels = ["easy", "medium", "hard"]


def choose_level(user_level):
    """after user has chosen and keyed in easy medium or hard mode, this
    function returns two arguments. first argument is the question of that
    mode, second argument is the answer of that mode to be used for
    comparison in later stage"""
    if user_level == "easy":
        print("easy it is")
        return question_easy, answer_easy
    elif user_level == "medium":
        print("good choice taking it up a notch")
        return question_medium, answer_medium
    else:
        print("Let's see if you are a true MFFL")
    return question_hard, answer_hard


def check(response, answer, answer_index):
    """after user has entered his guess for the blank, this function
    will compare his input against the specified answer """
    # compare user input against quiz's answers
    if response.lower() == answer[answer_index].lower():
        print("\nDude you know your stuff!")
        print("I bet you cannot answer the next one.")
        return True  # return true if answer matches
    else:
        return False  # return false if answer dont match


def play_game():
    """this is the main game function. Initially number of tries for the
    whole quiz is 5. Next, user will be prompted to choose the game
    difficulty mode and the question will be displayed with blanks for
    the user to guess what the first blank is. If user enter correct, this
    first blank will be replaced and display the right answer. Remaining
    quiz with blanks will be displayed to let user continue to guess the
    next blank. This will continue until user get all 5 blanks answered
    correctly. However, if user's guess is wrong, the number of tries will
    decrement by 1 and left with 4 tries to get the whole quiz correct.
    User will be prompted with message to tell him how many number of tries
    left and asked to continue to guess what should be the answer.
    Prgram will end when the number of tries reaches 0 or when user get
    all blanks answered correctly. """
    count = 5
    level = raw_input("Select level {}:".format(' | '.join(levels))).lower()
    if level in levels:
        quiz, answers = choose_level(level)
        print(quiz)
        index = 0
        while index < len(answers) and count > 0:
            answer = raw_input("Can you guess what is" + blanks[index] + "?")
            if check(answer, answers, index):
                quiz = quiz.replace(blanks[index], answer)
                print(quiz)
                index += 1
            else:
                count = count - 1
                print("Wrong guess. Number of tries left: {}".format(count))
    else:
        print("Invalid input! Try again. {}".format('|'.join(levels)))


play_game()
