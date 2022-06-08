
class Questions:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.question_list = []
        self.question_list.append(question)
        global question_num
        question_num += 1

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
                print()
                incorrect_list.append(self.question)


def display_stats():
    print()
    print("########## YOUR STATS ##########")
    print("You got {} question correct".format(correct))
    print("################################")
    print("You need to work on these questions:\n {}, \n ".format(incorrect_list))
    print("################################")


question_num = 1
correct = 0
incorrect_list = []

# main routine

start = ''

while start != "q":
    print("Welcome to the Māori Days of the Week quiz.")
    print()
    print("When answering questions please make sure to start your answers with a Capital letter. \n"
          "Also please make sure to include any macrons (ā) in your answer. \n"
          "These macrons can be found by pressing and"
          "holding a the letter you would like to put the macron on.")
    print()
    start = input("Press 'q' to start quiz: ")
    print()

while question_num != 8:
    if question_num == 1:
        question1 = Questions("What is Monday in Maori", "Rāhina")
        question1.ask_questions()
    elif question_num == 2:
        question2 = Questions("What is Tuesday in Maori", "Rātū")
        question2.ask_questions()
    elif question_num == 3:
        question3 = Questions("What is Wednesday in Maori", "Rāapa")
        question3.ask_questions()
    elif question_num == 4:
        question4 = Questions("What is Thursday in Maori", "Rāpare")
        question4.ask_questions()
    elif question_num == 5:
        question5 = Questions("What is Friday in Maori", "Rāmere")
        question5.ask_questions()
    elif question_num == 6:
        question6 = Questions("What is Saturday in Maori", "Rāhoroi")
        question6.ask_questions()
    elif question_num == 7:
        question7 = Questions("What is Sunday in Maori", "Rātapu")
        question7.ask_questions()


display_stats()
