# dndrandomizer

Randomizes the stat rolls for a D&D character without needing dice!

monday feb 17, 2020//
I don't know what I'm supposed to put in a README yet since I'm still new to coding, so I guess I'll put some of my thoughts about the project now that I'm done with it (for the moment).

I wanted to create something that I thought would be fairly simple to make as a beginner and might be useful to me in some way. I needed for there to be a GUI since I'm in love with the idea of making an application that I could give to someone else and allow them to easily use.

Tkinter was my only option, as I didn't want to venture off too far away from the bare essentials. Through developing this, I was able to familiarize myself with the scope of what one function could pack into a program, and just how long they could be.

The randomize() function inside of the "Roll" button first fixes the state of each Entry widget to "normal." Next, it goes through "if" statements assigned to each widget - if the Entry is not empty, then it will delete the contents. This check is in place because otherwise, the function will concatenate the number on each roll, making the result grow.
    Example:
        Strength first roll (14) - 14
        Strength second roll (10) - 1014
        Strength third roll (4) - 41014

After that, each category has a variable that is assigned the result of random.randint(1, 20). The range of 1-20 was chosen because the die used in Dungeons and Dragons to roll stats is the d20. Those variables are then inserted into each Entry widget and the numbers are displayed.

Finally, the Entry widgets' states are changed to "readonly," which prevents the randomized values in the boxes from being changed by the user. Pressing the "Roll" button again restarts the function, which changes the widgets back to the "normal" state. The widgets have to be changed from "normal" to "readonly" and back because Entry widgets in a "readonly" state do not update, but the changes are reflected if the state is "normal." Unfortunately, "normal" allows the user to type in the Entry widgets and change the results, which is undesireable behavior, so the widgets have to go back into the "readonly" state after the numbers are generated and displayed.


Looking at the code now that it's done, I feel like I could have used lists and loops to add methods and change states of widgets somehow, but I'm still not comfortable or confident when it comes to using loops. Having every single thing typed out line-for-line without a loop does provide me some clarity.
