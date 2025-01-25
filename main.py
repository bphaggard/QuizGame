from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for index in question_data:
    new_q = Question(index["text"], index["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz.next_question()