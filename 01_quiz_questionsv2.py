# Trial 2 of 03_quiz_questionsv2
# test to see if using a class system is better than importing questions from Csv
# proper questions and formatting added

class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        question_list.append(self)

    def display_info(self):
        print("Question: ", self.question)
        print("Answer: ", self.answer)


def print_question():
    for question in question_list:
        question.display_info()


question_list = []

question1 = Questions("What is Monday in Māori", "Rāhina")
question2 = Questions("What is Tuesday in Māori","Rātū")
question3 = Questions("What is Wednesday in Māori", "Rāapa")
question4 = Questions("What is Thursday in Māori", "Rāpare")
question5 = Questions("What is Friday in Māori", "Rāmere")
question6 = Questions("What is Saturday in Māori", "Rāhoroi")
question7 = Questions("What is Sunday in Māori", "Rātapu")

print_question()
