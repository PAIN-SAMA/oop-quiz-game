from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random
# print(question_data[0]["text"])
ran_num = random.randint(1,10)
right_answer = 0
q_number = 0
question_bank = []
trys = 0
for question in question_data:
    q_number += 1
    question_text = question["text"]; question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question) # we are adding an object to a list

# print("Done ")
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# class User:
#     def __init__(self, name, id):
#         self.id = id
#         self.username = name
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#       user.followers += 1
#       self.following += 1

# bander = User("banderkj", "911");
# adel = User("adelkj", "102");

# bander.follow(adel);

# print(f"bander follower {bander.followers} following {bander.following}\n\n")
# print(f"adel follower {adel.followers} following {adel.following}")