import tkinter as tk
from miscellaneous import Spacer, quit, ComputerRate

YELLOW = '#F2EA87'
PINK = '#fe86a4'
LIGHT_BLUE = '#a2cffe'
BROWN = '#C18E60'
size = "600x500"

    
def MainPage(): 
    '''
    First Page, Asking Player which story they want to play
    '''
   
    root = tk.Tk()
    root.title("Anna's Project 7")
    root.geometry(size)
    root['bg'] = LIGHT_BLUE
    
    label = tk.Label(text="Mad Libs Game", bg=LIGHT_BLUE, font = 'bold')
    label.pack()
    
    Spacer()
    
    choose_story_label = tk.Label(text= 'Which story do you want?', bg = LIGHT_BLUE)
    choose_story_label.pack()
    
    Spacer()

    Story_1_button = tk.Button(text="Story 1",
                               padx=10, pady=5,
                               command=lambda: [Story1(), quit(root)])
    Story_1_button.pack()
    
    Spacer()
    
    Story_2_button = tk.Button(text="Story 2", 
                               padx=10, 
                               pady=5,
                               command=lambda: [Story2(), quit(root)])
    Story_2_button.pack()
    
    Spacer()
    
    Story_3_button = tk.Button(text="Story 3", 
                               padx=10, 
                               pady=5,
                               command=lambda: [Story3(), quit(root)])
    Story_3_button.pack()


def Story1():
    '''
    Creates new window and prompts input from user needed for Story 1.
    '''
    
    Input_Window = tk.Tk()
    Input_Window.geometry(size)
    Input_Window.title("Story 1")
    Input_Window.geometry(size)
    Input_Window['bg'] = LIGHT_BLUE
    Input_Window.grid_columnconfigure((0,1), weight=1)
    
    Label1 = tk.Label(Input_Window, text="Person Name", bg = LIGHT_BLUE)
    Label2 = tk.Label(Input_Window, text="Verb ending in 'ing'", bg = LIGHT_BLUE)
    Label3 = tk.Label(Input_Window, text="Verb", bg = LIGHT_BLUE)
    Label4 = tk.Label(Input_Window, text="Ajective", bg = LIGHT_BLUE)
    
    Entry1 = tk.Entry(Input_Window)
    Entry2 = tk.Entry(Input_Window)
    Entry3 = tk.Entry(Input_Window)
    Entry4 = tk.Entry(Input_Window)

    Label1.grid(row=3, column=0)
    Entry1.grid(row=3, column=1, sticky="ew")
    Label2.grid(row=4, column=0)
    Entry2.grid(row=4, column=1, sticky="ew")
    Label3.grid(row=5, column=0)
    Entry3.grid(row=5, column=1, sticky="ew")
    Label4.grid(row=6, column=0)
    Entry4.grid(row=6, column=1, sticky="ew")


    
    # Below function takes player to page that creates story, and quits current page
    button = tk.Button(master=Input_Window,
                       text="Create Story", 
                       padx=10, 
                       pady=5,
                       command=lambda: [CreateStory1(Entry1,
                                                     Entry2, 
                                                     Entry3, 
                                                     Entry4), 
                                         quit(Input_Window)]) 

    button.grid(row=7, column = 1)


def Story2():
    '''
    Creates new window and prompts input from user needed for Story 2.
    '''
    Input_Window = tk.Tk()
    Input_Window.geometry(size)
    Input_Window.title("Story 2")
    Input_Window.geometry(size)
    Input_Window['bg'] = LIGHT_BLUE
    Input_Window.grid_columnconfigure((0,1), weight=1)
    
    Label1 = tk.Label(Input_Window, text="Person Name", bg = LIGHT_BLUE)
    Label2 = tk.Label(Input_Window, text="Person Name", bg = LIGHT_BLUE)
    Label3 = tk.Label(Input_Window, text="Adjective", bg = LIGHT_BLUE)
    
    Entry1 = tk.Entry(Input_Window)
    Entry2 = tk.Entry(Input_Window)
    Entry3 = tk.Entry(Input_Window)
    
    Label1.grid(row=3, column=0)
    Entry1.grid(row=3, column=1, sticky="ew")
    Label2.grid(row=4, column=0)
    Entry2.grid(row=4, column=1, sticky="ew")
    Label3.grid(row=5, column=0)
    Entry3.grid(row=5, column=1, sticky="ew")
    
    button = tk.Button(master=Input_Window,
                       text="Create Story", 
                       padx=10, 
                       pady=5,
                       command=lambda: [CreateStory2(Entry1,
                                                     Entry2, 
                                                     Entry3),
                                        quit(Input_Window)])
    button.grid(row=6, column = 1)


def Story3():
    '''
    Creates new window and prompts input from user needed for Story 3.
    '''
    
    Input_Window = tk.Tk()
    Input_Window.geometry(size)
    Input_Window.title("Story 3")
    Input_Window.geometry(size)
    Input_Window['bg'] = LIGHT_BLUE
    Input_Window.grid_columnconfigure((0,1), weight=1)
    
    Label1 = tk.Label(Input_Window, text="Favorite Sport", bg = LIGHT_BLUE)
    Label2 = tk.Label(Input_Window, text="Household item", bg = LIGHT_BLUE)
    Label3 = tk.Label(Input_Window, text="Relative", bg = LIGHT_BLUE)
    Label4 = tk.Label(Input_Window, text="Your Name", bg = LIGHT_BLUE)
    
    Entry1 = tk.Entry(Input_Window)
    Entry2 = tk.Entry(Input_Window)
    Entry3 = tk.Entry(Input_Window)
    Entry4 = tk.Entry(Input_Window)
    
    Label1.grid(row=3, column=0)
    Entry1.grid(row=3, column=1, sticky="ew")
    Label2.grid(row=4, column=0)
    Entry2.grid(row=4, column=1, sticky="ew")
    Label3.grid(row=5, column=0)
    Entry3.grid(row=5, column=1, sticky="ew")
    Label4.grid(row=6, column=0)
    Entry4.grid(row=6, column=1, sticky="ew")
    
    button = tk.Button(master=Input_Window,
                       text="Create Story", 
                       padx=10, 
                       pady=5,
                       command=lambda: [CreateStory3(Entry1, 
                                                     Entry2,
                                                     Entry3,
                                                     Entry4), 
                                        quit(Input_Window)])
    button.grid(row=7, column = 1)


def CreateStory1(Entry1, Entry2, Entry3, Entry4):
    '''
    Writes the story 1 based on input from last window and makes player input Upper Case. Calls Play Again, and Computer Rating of Story functions from miscellaneous file.
    :param Entry1: Input 1 from user, coming from Story1() function
    :param Entry2: Input 2 from user, coming from Story1() function
    :param Entry3: Input 3 from user, coming from Story1() function
    :param Entry4: Input 4 from user, coming from Story1() function
    '''
    
    window = tk.Tk()
    window.title("Story 1")
    window.geometry(size)
    window['bg'] = BROWN
    
    Entry1 = Entry1.get().upper()
    Entry2 = Entry2.get().upper()
    Entry3 = Entry3.get().upper()
    Entry4 = Entry4.get().upper()

    label = tk.Label(window,
                     text=f'There once was a lady named {Entry1}. ', 
                     pady=20, 
                     bg=BROWN)
    label2 = tk.Label(window, 
                      text = f'She was the prettiest at the ball. ', 
                      pady=20,
                      bg=BROWN)
    label3 = tk.Label(window,
                      text = f'Unfortunately, she was really really bad at {Entry2}.',
                      pady=20, 
                      bg=BROWN)
    label4 = tk.Label(window,
                      text = f'This made all the potential suiters {Entry3} away!',
                      pady=20, 
                      bg=BROWN)
    label5 = tk.Label(window,
                      text = f'It is too bad they cannot see her true value. She always seemed {Entry4}!', 
                      pady=20,
                      bg=BROWN)
    
    label.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()

    ReturnButton = tk.Button(text="Play Again?",  command = lambda:[quit(window),MainPage()])
    ReturnButton.pack()
 
    ComputerRate(window, BROWN)
    

def CreateStory2(Entry1, Entry2, Entry3):
    '''
    Writes the story 2 based on input from last window and makes player input Upper Case. Has button to Play Again, and Computer Rating of Story.
    :param Entry1: Input 1 from user, coming from Story2() function
    :param Entry2: Input 2 from user, coming from Story2() function
    :param Entry3: Input 3 from user, coming from Story2() function
    '''
    window = tk.Tk()
    window.title("Story 2")
    window.geometry(size)
    window['bg'] = PINK
    Entry1 = Entry1.get().upper() 
    Entry2 = Entry2.get().upper()
    Entry3 = Entry3.get().upper()
    
    label = tk.Label(window, 
                     text=f'{Entry1} is the worst!',
                     pady=20,
                     bg=PINK)
    label2 = tk.Label(window,
                      text=f'{Entry2} is {Entry3}!', 
                      pady=20, 
                      bg=PINK)

    label.pack()
    label2.pack()
    
    ReturnButton = tk.Button(text="Play Again?", 
                             command = lambda:[quit(window),
                                               MainPage()])
    ReturnButton.pack()  
    
    ComputerRate(window, PINK)

    
def CreateStory3(Entry1, Entry2, Entry3, Entry4):
    '''
    Writes the story 3 based on input from last window and makes player input Upper Case. Has button to Play Again, and Computer Rating of Story.
    :param Entry1: Input 1 from user, coming from Story3() function
    :param Entry2: Input 2 from user, coming from Story3() function
    :param Entry3: Input 3 from user, coming from Story3() function
    :param Entry4: Input 4 from user, coming from Story3() function
    '''
    window = tk.Tk()
    window.title("Story 3")
    window.geometry(size)
    window['bg'] = YELLOW
    
    Entry1 = Entry1.get().upper()
    Entry2 = Entry2.get().upper()
    Entry3 = Entry3.get().upper()
    Entry4 = Entry4.get().upper()
    
    label = tk.Label(window,
                     text=f"'{Entry4} is so bad at {Entry1}!' said {Entry3}", 
                     pady=20, 
                     bg=YELLOW)
    label2 = tk.Label(window, 
                      text=f"But they dont know you eat {Entry2} before each game", 
                      pady=20,
                      bg=YELLOW)
    
    label.pack()
    label2.pack()
    
    ReturnButton = tk.Button(text="Play Again?",
                             command = lambda:[quit(window),
                                               MainPage()])
    ReturnButton.pack()
    
    ComputerRate(window, YELLOW)


if __name__ == "__main__":
    MainPage()
    tk.mainloop()