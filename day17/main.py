from question_model import Question
from data import question_data 
from quiz_brain import Quizbrain
question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=Quizbrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

print("you've complete the quiz")
print(f"your final score was:{quiz.score}/{len(question_bank)}")