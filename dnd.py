
from tkinter import *
import random

stats = {'Strength':0, 'Dexterity':0, 'Constitution':0, 'Intelligence':0, 'Wisdom':0, 'Charisma':0} #Dict with the stats and their names
indexstats = list(stats) #Creates a stats list, used for .index() function

def randomize():

    for key, value in stats.items():
        stats[key] = random.randint(1, 20) #Sets each value in the stats dict to a random value

    for statName, statValue in stats.items():
        currentwidget = root.nametowidget(".mainframe." + statName.lower()) #Gets the entry by searching for it's id, then sets it to a variable
        currentwidget.configure(state='normal') #Sets the widget state to normal

        if currentwidget.index('end') != 0: #Checks if any entry is not empty and resets them accordingly
            currentwidget.delete(0, END)
        
        currentwidget.insert(0, stats[statName]) #Inserts the stat value into the entry
        currentwidget.configure(state="readonly", readonlybackground="white") #Sets entry state to readonly

root = Tk()
root.title("DnD Rndmzr")

#Frame Stuff
frame = LabelFrame(root, text="Roll Your Character", padx = 50, pady = 40, name='mainframe')
frame.grid(padx=10, pady=10)

#Random All
buttonRandomize = Button(frame, text="Roll", command=lambda: randomize())
buttonRandomize.grid(row=0, column=0)

for statName in stats.keys():
    label = Label(frame, text=statName)
    labelrow = indexstats.index(statName)*2+1 #Setting the row proportional to the position of the stat name in the list
    label.grid(row=labelrow, column=0)
    result = Entry(frame, justify = "center", name=statName.lower()) #Giving each entry field their own id, lowercase required hence .lower() is used
    result.grid(row=labelrow+1, column=0)
    
root.resizable(width=False, height=False)
root.mainloop()
