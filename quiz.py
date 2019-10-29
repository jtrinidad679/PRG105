"""
Lesson:
In this programming exercise, you will create a simple trivia game for two players.
The program will work like this:

Starting with player 1, each player gets a turn at answering 5 trivia questions.
(There should be a total of 10 questions.) When a question is displayed, 4 possible
answers are also displayed. Only one of the answers is correct, and if the player
selects the correct answer, he or she earns a point. After answers have been selected
for all the questions, the program displays the number of points earned by each player
and declares the player with the highest number of points the winner.To create this
program, write a Question class to hold the data for the trivia question. The question
class should have attributes for the following data:

A trivia question
Possible answer 1
Possible answer 2
Possible answer 3
Possible answer 4
The number of the correct answer (1, 2, 3, or 4)
The Question class should also have an appropriate __init__ method, accessors, and mutators.

The program should have a list or a dictionary containing 10 Question Objects, one for
each trivia question. Make up your own trivia question on the subject or subjects of your choice for the objects.
"""
import questions
# I've created 4 functions to solve this program and make it look more presentable and less cluttered. The main function
# simply has our questions which are then put into separate lists for each players quiz. Both player quiz functions do the
# same thing; they take the data from questions.py and use that to pull questions from their lists and present their possible answers.
# I initialized player_one and player_two scores to 0 at first and then they are passed to their respective functions. Once they
# are returned, they will be passed again to the score_card function which will determine who won or if there was a tie.


def main():
    question_one = questions.Question("Which bird is a universal symbol of peace?", "A. Raven", "B. Eagle", "C. Cardinal", "D. Dove", "D")
    question_two = questions.Question("How many hours do cats sleep each day?", "A. 12-16", "B. 16-20", "C. 20-24", "D. 8-12", "B")
    question_three = questions.Question("A snail can sleep for how many years?", "A. 5", "B. 3", "C. 1", "D. 4", "B")
    question_four = questions.Question("Which U.S. city had a cat for a mayor for almost 20 years?", "A. Warm River, Idaho", "B. Jacksboro, Texas", "C. Talkeetna, Alaska", "D. Gardner, Kansas", "C")
    question_five = questions.Question("Which animal never sleeps?", "A. Hippopotamus", "B. Bullfrog", "C. Bat", "D. Hammerhead Shark", "B")
    question_six = questions.Question("A group of kittens is known as what?", "A. Kine", "B. Kindle", "C. Kaboodle", "D. Kettle", "B")
    question_seven = questions.Question("What is the gestation period of a blue whale?", "A. 16-18 Months", "B. 4-6 Months", "C. 10-12 Months", "D. 2 Years", "C")
    question_eight = questions.Question("A newborn kangaroo is about the size of a ...?", "A. Grapefruit", "B. Plum", "C. Watermelon", "D. Lima Bean", "D")
    question_nine = questions.Question("How many times can a hummingbird flap its wings per second?", "A. 160", "B. 40", "C. 20", "D. 80", "D")
    question_ten = questions.Question("What animal has the highest blood pressure?", "A. Flea", "B. Elephant", "C. Giraffe", "D. Blue Whale", "C")

    set_one = [question_ten, question_eight, question_four, question_seven, question_one]
    set_two = [question_two, question_five, question_nine, question_six, question_three]

    player_one = 0
    player_two = 0

    player_one_score = player_one_quiz(set_one, player_one)
    player_two_score = player_two_quiz(set_two, player_two)

    score_card(player_one_score, player_two_score)


def player_one_quiz(questions_one, score_one):
    print("Player 1: ")
    for query in questions_one:
        print("\n")
        print(query.get_question())
        print(query.get_answer_one())
        print(query.get_answer_two())
        print(query.get_answer_three())
        print(query.get_answer_four())
        guess = input("Please enter the correct answer: ")
        if guess.upper() == query.get_correct_answer():
            print("Good job!")
            score_one += 1
        elif guess.upper() != query.get_correct_answer():
            print("So close! Buuut.. try again.")
    print("\n")
    print("Player 1 earned: " + str(score_one) + " points")
    print("\n")
    return score_one


def player_two_quiz(questions_two, score_two):
    print("Player 2: ")
    for query in questions_two:
        print("\n")
        print(query.get_question())
        print(query.get_answer_one())
        print(query.get_answer_two())
        print(query.get_answer_three())
        print(query.get_answer_four())
        guess = input("Please enter the correct answer: ")
        if guess.upper() == query.get_correct_answer():
            print("Good job!")
            score_two += 1
        elif guess.upper() != query.get_correct_answer():
            print("So close! Buuut.. try again.")
    print("\n")
    print("Player 2 earned: " + str(score_two) + " points")
    return score_two

# The score_card function takes both variables (player_one_score and player_two_score) and determines whether
# or not the players have tied, or which player wins the game.


def score_card(score_one, score_two):
    if score_one == score_two:
        print("You tied!")
    elif score_one > score_two:
        print("Player 1 is the winner!")
    elif score_one < score_two:
        print("Player 2 is the winner!")


main()
