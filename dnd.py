from tkinter import *
import random

root = Tk()
root.title("DnD")


#defining functions

def randomize():
    return

def race():
    return

def strength():
    return

def dexterity():
    return

def intelligence():
    return

def wisdom():
    return

def charisma():
    return


#frame stuff
frame = LabelFrame(root, text="Create your character", padx = 50, pady = 40)
frame.grid(padx=10, pady=10)


#Random All
buttonRandomize = Button(frame, text="Randomize Stats", command= lambda: randomize())
buttonRandomize.grid(row=0, column=0)


#Name
labelName = Label(frame, text="Name")
labelName.grid(row=1, column=0)

#Strength
labelStrength = Label(frame, text="Strength")
labelStrength.grid(row=3, column=0)

#Dexterity
labelDexterity = Label(frame, text="Dexterity")
labelDexterity.grid(row=5, column=0)

#Intelligence
labelIntelligence = Label(frame, text="Intelligence")
labelIntelligence.grid(row=7, column=0)

#Wisdom
labelWisdom = Label(frame, text="Wisdom")
labelWisdom.grid(row=9, column=0)

#Charisma
labelCharisma = Label(frame, text="Charisma")
labelCharisma.grid(row=11, column=0)


root.resizable(width=False, height=False)
root.mainloop()