from question_model import Question
from data import question_data

question_bank = []

for index in question_data:
    new_q = Question(index["text"], index["answer"])
    question_bank.append(new_q)