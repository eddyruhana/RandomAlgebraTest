# Project: Generate a Random Math Quiz for Students and Grade at the End

import random
from tkinter import *

class AlgebraTest(Frame):
    """The Test will be a GUI"""

    def __init__(self):
        """Create and grid several components (Text, RadioButton, Button, Label) into the Frame"""

        Frame.__init__(self)    # initializes Frame object
        self.master.title("Elementary Algebra Test")

        # Main frame fills entire container, expands if necessary
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = W+E+N+S)

        self.textQuestion = Text(self, width = 90, height = 30)  # Component of the questions of the Test

        # 8 questions test, span 8 rows and all available space
        self.textQuestion.grid(rowspan = 8, sticky = W+E+N+S)


        file = open("Question_Pool.txt", "r")       # Open the Questionnaire file, read the questions
        question_pool = {}       # This dictionary will house the Questions and Answers

        for line in file:
            q_and_a = line.split("#")
            q_and_a_numberID = int(q_and_a[0])
            q_and_a_content = q_and_a[1]
            cut_content = len(q_and_a_content) - 1   # This get the length of the question - the last character: '\n'
            q_and_a_content = q_and_a_content[0:cut_content]    # Cut the question's last character off (\n)
            question_pool[q_and_a_numberID] = q_and_a_content   # And here is my dictionary of Q & A

        # Generate the test by randomly selecting 8 questions out of The Pool of Questions file: Question_Pool.txt:
        self.selectedQuestion = []   # Watch that no question is repeated twice by storing the Question number
        self.correctAnswersIndices = []  # Stores the correct answer's index to each question of the Test
        self.correctMultipleChoice = []  # List of the correct multiple choice
        howManyQuestion = 0     # Count up to 8 questions selected for the test
        questionNumber = 1      # Each Question in the Test has a Question number

        while howManyQuestion < 8:
            x = random.randint(1, 15)
            y = x + 1000    # To each selected question, here's the correct index answer
            if x not in self.selectedQuestion:
                self.selectedQuestion.append(x)
                self.correctAnswersIndices.append(y)
                self.correctMultipleChoice.append(question_pool[self.correctAnswersIndices[howManyQuestion]])
                print("%2d. %2s \n" % (questionNumber, question_pool[x]))
                self.textQuestion.insert(INSERT, "%2d. %2s \n\n\n" % (questionNumber, question_pool[x]))    # GUI: The selected question of the Test
                questionNumber += 1
                howManyQuestion += 1

        # Create multiple Choice Answers Radio Buttons
        multipleChoice = ["a", "b", "c", "d"]
        self.yourAnswer1 = StringVar()
        self.yourAnswer2 = StringVar()
        self.yourAnswer3 = StringVar()
        self.yourAnswer4 = StringVar()
        self.yourAnswer5 = StringVar()
        self.yourAnswer6 = StringVar()
        self.yourAnswer7 = StringVar()
        self.yourAnswer8 = StringVar()

        self.yourAttempt1 = []
        self.yourFinalAnswer1 = []
        self.yourAttempt2 = []
        self.yourFinalAnswer2 = []
        self.yourAttempt3 = []
        self.yourFinalAnswer3 = []
        self.yourAttempt4 = []
        self.yourFinalAnswer4 = []
        self.yourAttempt5 = []
        self.yourFinalAnswer5 = []
        self.yourAttempt6 = []
        self.yourFinalAnswer6 = []
        self.yourAttempt7 = []
        self.yourFinalAnswer7 = []
        self.yourAttempt8 = []
        self.yourFinalAnswer8 = []

        self.correctAnswer1 = question_pool[self.correctAnswersIndices[0]]
        self.correctAnswer2 = question_pool[self.correctAnswersIndices[1]]
        self.correctAnswer3 = question_pool[self.correctAnswersIndices[2]]
        self.correctAnswer4 = question_pool[self.correctAnswersIndices[3]]
        self.correctAnswer5 = question_pool[self.correctAnswersIndices[4]]
        self.correctAnswer6 = question_pool[self.correctAnswersIndices[5]]
        self.correctAnswer7 = question_pool[self.correctAnswersIndices[6]]
        self.correctAnswer8 = question_pool[self.correctAnswersIndices[7]]


        # Question 1 - Multiple Choice - RadioButton in 1st row, 3rd column [row:0, Col:2]:
        col = 2
        for possibleAnswer in multipleChoice:
            self.answerButton1 = Radiobutton(self, text = possibleAnswer, variable = self.yourAnswer1, value = possibleAnswer, font = "Times 15", command = self.trackAnswer1)
            self.answerButton1.grid(row = 0, column = col, sticky = W+E+N+S)
            col += 1

        # Question 2 - Multiple Choice - RadioButton in 2nd row, 3rd column [row:1, Col:2]:
        col = 2
        for possibleAnswer in multipleChoice:
            answerButton2 = Radiobutton(self, text = possibleAnswer, variable = self.yourAnswer2, value = possibleAnswer, font = "Times 15", command = self.trackAnswer2)
            answerButton2.grid(row = 1, column = col, sticky = W+E+N+S)
            col += 1

        # Question 3 - Multiple Choice - RadioButton in 3rd row, 3rd column [row:2, Col:2]:
        col = 2
        for possibleAnswer in multipleChoice:
            answerButton3 = Radiobutton(self, text = possibleAnswer, variable = self.yourAnswer3, value = possibleAnswer, font = "Times 15", command = self.trackAnswer3)
            answerButton3.grid(row = 2, column = col, sticky = W+E+N+S)
            col += 1

        # Question 4 - Multiple Choice - RadioButton in 4th row, 3rd column [row:3, Col:2]:
        col = 2
        for possibleAnswer in multipleChoice:
            answerButton4 = Radiobutton(self, text = possibleAnswer, variable = self.yourAnswer4, value = possibleAnswer, font = "Times 15", command = self.trackAnswer4)
            answerButton4.grid(row = 3, column = col, sticky = W+E+N+S)
            col += 1

        # Question 5 - Multiple Choice - RadioButton in 5th row, 3rd column [row:4, Col:2]:
        col = 2
        for possibleAnswer in multipleChoice:
            answerButton5 = Radiobutton(self, text = possibleAnswer, variable = self.yourAnswer5, value = possibleAnswer, font = "Times 15", command = self.trackAnswer5)
            answerButton5.grid(row = 4, column = col, sticky = W+E+N+S)
            col += 1

        # Question 6 - Multiple Choice - RadioButton in 6th row, 3rd column [row:5, Col:2]:
        col = 2
        for possibleAnswer in multipleChoice:
            answerButton6 = Radiobutton(self, text = possibleAnswer, variable = self.yourAnswer6, value = possibleAnswer, font = "Times 15", command = self.trackAnswer6)
            answerButton6.grid(row = 5, column = col, sticky = W+E+N+S)
            col += 1

        # Question 7 - Multiple Choice - RadioButton in 7th row, 3rd column [row:6, Col:2]:
        col = 2
        for possibleAnswer in multipleChoice:
            answerButton7 = Radiobutton(self, text = possibleAnswer, variable = self.yourAnswer7, value = possibleAnswer, font = "Times 15", command = self.trackAnswer7)
            answerButton7.grid(row = 6, column = col, sticky = W+E+N+S)
            col += 1

        # Question 8 - Multiple Choice - RadioButton in 8th row, 3rd column [row:7, Col:2]:
        col = 2
        for possibleAnswer in multipleChoice:
            answerButton8 = Radiobutton(self, text = possibleAnswer, variable = self.yourAnswer8, value = possibleAnswer, font = "Times 15", command = self.trackAnswer8)
            answerButton8.grid(row = 7, column = col, sticky = W+E+N+S)
            col += 1

        # Grade the Test (Work-in-progress)
        self.buttonGrade = Button(self, text = "Submit to be Graded Over 100: ", command = self.gradeTest)
        self.buttonGrade.grid(row = 8, column = 0, sticky = W+E+N+S)


        yourScore = "Not Graded Yet"
        self.LabelScore = Label(self, text = yourScore, font = "Times 15")
        self.LabelScore.grid(row = 8, column = 2, columnspan = 5, sticky = W+E+N+S)


        print("The Questions-Index of the Test: %s " % self.selectedQuestion)     # List of the selected questions of the Test
        print("The Correct Answers-Index: %s" % self.correctAnswersIndices)    # List of the correct answers of the Test
        print("The correct multiple choice: %s \n" % self.correctMultipleChoice)   # Correct multiple choice


    def gradeTest(self):
        grade = 0.00
        if self.yourFinalAnswer1 == self.correctAnswer1:
            grade += 12.5
        if self.yourFinalAnswer2 == self.correctAnswer2:
            grade += 12.5
        if self.yourFinalAnswer3 == self.correctAnswer3:
            grade += 12.5
        if self.yourFinalAnswer4 == self.correctAnswer4:
            grade += 12.5
        if self.yourFinalAnswer5 == self.correctAnswer5:
            grade += 12.5
        if self.yourFinalAnswer6 == self.correctAnswer6:
            grade += 12.5
        if self.yourFinalAnswer7 == self.correctAnswer7:
            grade += 12.5
        if self.yourFinalAnswer8 == self.correctAnswer8:
            grade += 12.5
        print("Your Grade: ", grade)

        # Display your grade:
        self.LabelGrade = Label(self, text = grade, font="Times 15")
        self.LabelGrade.grid(row = 8, column = 2, columnspan = 5, sticky = W+E+N+S)


    def trackAnswer1(self):
        self.yourAttempt1.append(self.yourAnswer1.get())
        self.yourFinalAnswer1 = self.yourAttempt1[-1]
        print("Attempts to Question 1: ", self.yourAttempt1)
        print("Final answer to Question 1: %s\n" % self.yourFinalAnswer1)

    def trackAnswer2(self):
        self.yourAttempt2.append(self.yourAnswer2.get())
        self.yourFinalAnswer2 = self.yourAttempt2[-1]
        print("Attempts to Question 2: ",self.yourAttempt2)
        print("Final answer to Question 2: %s\n" % self.yourFinalAnswer2)

    def trackAnswer3(self):
        self.yourAttempt3.append(self.yourAnswer3.get())
        self.yourFinalAnswer3 = self.yourAttempt3[-1]
        print("Attempts to Question 3: ",self.yourAttempt3)
        print("Final answer to Question 3: %s\n" % self.yourFinalAnswer3)

    def trackAnswer4(self):
        self.yourAttempt4.append(self.yourAnswer4.get())
        self.yourFinalAnswer4 = self.yourAttempt4[-1]
        print("Attempts to Question 4: ",self.yourAttempt4)
        print("Final answer to Question 4: %s\n" % self.yourFinalAnswer4)

    def trackAnswer5(self):
        self.yourAttempt5.append(self.yourAnswer5.get())
        self.yourFinalAnswer5 = self.yourAttempt5[-1]
        print("Attempts to Question 5: ",self.yourAttempt5)
        print("Final answer to Question 5: %s\n" % self.yourFinalAnswer5)

    def trackAnswer6(self):
        self.yourAttempt6.append(self.yourAnswer6.get())
        self.yourFinalAnswer6 = self.yourAttempt6[-1]
        print("Attempts to Question 6: ",self.yourAttempt6)
        print("Final answer to Question 6: %s\n" % self.yourFinalAnswer6)

    def trackAnswer7(self):
        self.yourAttempt7.append(self.yourAnswer7.get())
        self.yourFinalAnswer7 = self.yourAttempt7[-1]
        print("Attempts to Question 7: ",self.yourAttempt7)
        print("Final answer to Question 7: %s\n" % self.yourFinalAnswer7)

    def trackAnswer8(self):
        self.yourAttempt8.append(self.yourAnswer8.get())
        self.yourFinalAnswer8 = self.yourAttempt8[-1]
        print("Attempts to Question 8: ",self.yourAttempt8)
        print("Final answer to Question 8: %s\n" % self.yourFinalAnswer8)


# THE DRIVER:
def main():
    AlgebraTest().mainloop()        # starts event loop

if __name__ == "__main__":
    main()
