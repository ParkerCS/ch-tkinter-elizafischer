# MAGIC 8-BALL (25pts)
# Create a tkinter app which acts as a "Magic 8-ball" fortune teller
# The user asks a yes/no question that they want an answer to.
# Then the user clicks a button, and your program displays
# the "magic" random answer to their question.
# Your program will have the following properties:
# - Use an App class to create the tkinter app √
# - Add a proper title (appears in the window tab) √
# - Add a Label widget at the top to give the user instructions/intro. √
# - Add an Entry widget so the user can enter their question. √
# - Add a Button widget which will trigger the answer.
# - Add a Label widget to display the answer (set to a initial value of "Your Fortune Here" or "--" or similar)
# - Get your random answer message from a list of at least 10 possible strings. (e.g. ["Yes", "No", "Most Likely", "Definitely", etc...])
# - Add THREE or more other style modifications to make your app unique (font family, font size, color, padding, image, borders, justification,
# whatever you can find in tkinter library etc.)  Make a comment at the top or bottom of your code to tell me your 3 things you did. (Just to help me
# out in checking your assignment)


'''
Making a magic 8-ball app
'''


from tkinter import *
from tkinter import font
import random

class App():
    def __init__(self, master):
        # Storing the question entered
        self.entery = DoubleVar()
        self.entery.set("")

        self.answer = DoubleVar()
        self.answer.set("8ball's Answer Here!")

        # Creating the instruction text box
        self.instructions = Label(master, text="Ask any yes/no question:")
        self.instructions.grid(column=2, row=4, columnspan=4, sticky="e" + "w")

        # Creating the entry widget
        self.entry = Entry(master, textvariable=self.entery)
        self.entry.grid(column=2, row=5, columnspan=4, sticky= "e" + "w")

        # Creating the "Submit" button
        self.results = Button(master, text="Submit!", command=lambda: self.get_answer())
        self.results.grid(column=3, row=6, columnspan=2, sticky="e" + "w")

        # self.but_submit = Button(master, text = "Submit!")
        # self.but_submit.grid(column=3, row=6, columnspan= 2, sticky = "e" + "w")

        # Creating the fortune/answer area
        self.answer_label = Label(master, textvariable=self.answer)
        self.answer_label.grid(column=2, row=7, columnspan=4, sticky= "e" + "w")


        # Creating the image widget
        #self.image = Image.open(file = "8ball.gif")
        #self.image.grid(column=3, row=2, columnspan=2, rowspan= 2, sticky= "n" + "s" + "e" + "w")


        self.answer_opts = ["Yes!", "Not a change", "No way!", "Most likely", "Probably?", "I wouldn't be surprised...","Maybe", 'Without a doubt', 'I wouldn\'t count on it','Ask again later']

    def get_answer(self):
        self.entery.set("")
        random_answer = self.answer_opts[random.randrange(len(self.answer_opts))]
        self.answer.set(random_answer)

if __name__ == "__main__":
    root = Tk()
    root.title("Magic8Ball")
    app = App(root)
    root.mainloop()