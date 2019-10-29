"""
To create this program, write a Question class to hold the data for the trivia question.
The question class should have attributes for the following data:

A trivia question
Possible answer 1
Possible answer 2
Possible answer 3
Possible answer 4
The number of the correct answer (1, 2, 3, or 4)
The Question class should also have an appropriate __init__ method, accessors, and mutators.
"""


class Question:

    # __init__ initializes the attribute
    # we define each attribute with their specific functions, which will
    # then be used in quiz.py to display the questions and answers that correlate

    def __init__(self, question, answer_one, answer_two, answer_three, answer_four, correct_answer):
        self.question = question
        self.answer_one = answer_one
        self.answer_two = answer_two
        self.answer_three = answer_three
        self.answer_four = answer_four
        self.correct_answer = correct_answer

    def set_question(self, question):
        self.question = question

    def set_answer_one(self, answer_one):
        self.answer_one = answer_one

    def set_answer_two(self, answer_two):
        self.answer_two = answer_two

    def answer_three(self, answer_three):
        self.answer_three = answer_three

    def answer_four(self, answer_four):
        self.answer_four = answer_four

    def set_correct_answer(self, correct_answer):
        self.correct_answer = correct_answer

    def get_question(self):
        return self.question

    def get_answer_one(self):
        return self.answer_one

    def get_answer_two(self):
        return self.answer_two

    def get_answer_three(self):
        return self.answer_three

    def get_answer_four(self):
        return self.answer_four

    def get_correct_answer(self):
        return self.correct_answer
