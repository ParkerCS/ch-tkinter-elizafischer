# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a tkinter app with the following attributes:
# - use an App class √
# - Add a title. √
# - Make a label and entry widget for m1, m2, and r √
# - Make a "Calculate" button widget to trigger a lambda function √
# - Add a calculate label widget to display the answer √
# - Make exceptions for division by zero and type conversion errors. √
# - When "Calculate" is pushed, the result is displayed.  Yay! √
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception) √
# - Make your app unique by changing 3 or more DIFFERENT style attributes or kwargs for your app.
#   Perhaps consider: fonts, color, padding, widths, etc).
# Put a comment in your code to tell me what you changed.
# If you change the font for all the widgets, that is ONE thing.
# If you add padx to all your app widgets, that is ONE thing.
# If you change the color of all your blocks, that is ONE thing.

'''
- Changed all label fonts to Times
- Raised all label widget borders
- Added instructions labels
'''

from tkinter import *
from tkinter import font

class App():
    def __init__(self, master):
        # set title
        self.title_font = font.Font(family="Times bold", size=25, underline=2)
        self.title = Label(master, text="Universal Force of Gravity Calculator", font=self.title_font)
        self.title.grid(column=1, row=1, columnspan=4)

        self.label_font = font.Font(family="Times", size=15)


        # set variables
        self.m1 = DoubleVar()
        self.m2 = DoubleVar()
        self.r = DoubleVar()

        self.results = DoubleVar()
        self.results.set(0)


        # Instructions
        self.instructions1 = Label(master, text = "Universal Gravity Calculator:", font = self.label_font, relief = RAISED)
        self.instructions1.grid(column=1, row=3, sticky = "e")

        self.instructions2 = Label(master, text = "Force of Gravity between two objects: F = G * (m1 * m2) / r**2", font = self.label_font, relief = RAISED)
        self.instructions2.grid(column=1, row=4, columnspan=6, sticky="w")


        # m1, m2 and r label and entry widgets
        self.mass1_label = Label(master, text="Mass #1 (kg):", font = self.label_font, relief = RAISED)
        self.mass1_label.grid(column=1, row=6, sticky = "w")
        self.mass1 = Entry(master,textvariable = self.m1)
        self.mass1.grid(column = 2, row = 6, columnspan = 2)

        self.mass2_label = Label(master, text="Mass #2 (kg):", font = self.label_font, relief = RAISED)
        self.mass2_label.grid(column=1, row=7, sticky = "w")
        self.mass2 = Entry(master, textvariable=self.m2)
        self.mass2.grid(column=2, row=7, columnspan=2)

        self.radus_label = Label(master, text="Distance between M1 & M2 (m):", font = self.label_font, relief = RAISED)
        self.radus_label.grid(column=1, row=9)
        self.radius = Entry(master, textvariable=self.r)
        self.radius.grid(column=2, row=9, columnspan=2)


        # Solve button
        self.solve_button = Button(master, text="Calculate Force (N)", command=lambda: self.solve())
        self.solve_button.grid(column=2, row=10)
        self.solve_label = Label(master, textvariable=self.results, bg = "grey", fg = "white", font = self.label_font, relief = RAISED)
        self.solve_label.grid(column=2,row=11)


    def solve(self):
        try:
            self.results.set((6.67 * (10 ** -11)) * (self.m1.get() * self.m2.get()) / (self.r.get() ** 2))
        except:
            self.results.set("Error!")

if __name__ == "__main__":
    root = Tk()
    root.title("GravityCalc")
    app = App(root)
    root.mainloop()