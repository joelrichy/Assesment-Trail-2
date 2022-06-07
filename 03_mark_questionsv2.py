
class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.question_list = []
        self.question_list.append(question)

    def ask_questions(self):
        for question in self.question_list:
            question = input("{}: ".format(self.question))
            if question == self.answer:
                print("Correct")
                print()
                global correct
                correct += 1
            else:
                print("INCORRECT")


def display_stats():
    print()
    print("##### YOUR STATS #####")
    print("You got {} question correct".format(correct))


correct = 0

question1 = Questions("What is 1 + 1", "2")
question1.ask_questions()
question2 = Questions("What is 2 + 2", "4")
question2.ask_questions()

# main routine

display_stats()
