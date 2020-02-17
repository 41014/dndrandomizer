from tkinter import *
import random


def randomize():
    if resultStrength.index("end") != 0:
        resultStrength.delete(0, END)
    if resultDexterity.index("end") !=0:
        resultDexterity.delete(0, END)
    if resultIntelligence.index("end") !=0:
        resultIntelligence.delete(0, END)
    if resultWisdom.index("end") !=0:
        resultWisdom.delete(0, END)
    if resultCharisma.index("end") !=0:
        resultCharisma.delete(0, END)

    statStr = random.randint(1, 20)
    statDex = random.randint(1, 20)
    statInt = random.randint(1, 20)
    statWis = random.randint(1, 20)
    statChar = random.randint(1, 20)
    resultStrength.insert(0, statStr)
    resultDexterity.insert(0, statDex)
    resultIntelligence.insert(0, statInt)
    resultWisdom.insert(0, statWis)
    resultCharisma.insert(0, statChar)

root = Tk()
root.title("D&D Rndmzr")


#frame stuff
frame = LabelFrame(root, text="Randomize Your Character", padx = 50, pady = 40)
frame.grid(padx=10, pady=10)


#Random All
buttonRandomize = Button(frame, text="Randomize Stats", command=lambda: randomize())
buttonRandomize.grid(row=0, column=0)


#Strength
labelStrength = Label(frame, text="Strength")
labelStrength.grid(row=1, column=0)
resultStrength = Entry(frame)
resultStrength.grid(row=2, column=0)

#Dexterity
labelDexterity = Label(frame, text="Dexterity")
labelDexterity.grid(row=3, column=0)
resultDexterity = Entry(frame)
resultDexterity.grid(row=4, column=0)

#Intelligence
labelIntelligence = Label(frame, text="Intelligence")
labelIntelligence.grid(row=5, column=0)
resultIntelligence = Entry(frame)
resultIntelligence.grid(row=6, column=0)

#Wisdom
labelWisdom = Label(frame, text="Wisdom")
labelWisdom.grid(row=7, column=0)
resultWisdom = Entry(frame)
resultWisdom.grid(row=8, column=0)

#Charisma
labelCharisma = Label(frame, text="Charisma")
labelCharisma.grid(row=9, column=0)
resultCharisma = Entry(frame)
resultCharisma.grid(row=10, column=0)


root.resizable(width=False, height=False)
root.mainloop()