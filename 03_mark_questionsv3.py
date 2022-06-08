
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
                print("CORRECT")
                print()
                global correct
                correct += 1
            else:
                print("INCORRECT")
                print()
                incorrect_list.append(self.question)


def display_stats():
    print()
    print("##### YOUR STATS #####")
    print("You got {} question correct".format(correct))
    print("You need to work on these questions:\n {}, \n ".format(incorrect_list))
    print("################################")


correct = 0
incorrect_list = []

question1 = Questions("What is 1 + 1", "2")
question1.ask_questions()
question2 = Questions("What is 2 + 2", "4")
question2.ask_questions()

# main routine

display_stats()
