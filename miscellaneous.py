import tkinter as tk
import random


YELLOW = '#F2EA87'
PINK = '#fe86a4'
LIGHT_BLUE = '#a2cffe'
BROWN = '#C18E60'
size = "600x500"

def Spacer():
    '''
    Creates space (for aesthetics) between widgets.
    '''
    spacer = tk.Label(text ='', bg = LIGHT_BLUE)
    spacer.pack()

def quit(story):
    '''
    Exits out of the window.
    :param story: window being destroyed
    '''
    story.destroy()

def ComputerRate(window, color):
    '''
    Creates random grade for each story and presents it as packed.
    :param window: window that this grade will be presented on/ the master for the label
    :param color: master window's background color, so that the label can match exactly
    '''
    grade = random.randint(0,101)

    Grade_label = tk.Label(window, 
                           text = f"The Computer graded your story {grade}/ 100 !!",
                           pady = 20, 
                           bg = color)
    Grade_label.pack()


