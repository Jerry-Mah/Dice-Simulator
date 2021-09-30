# All the imports
from tkinter import *
from PIL import ImageTk, Image
import random 

# This is basic tkinter code
root = Tk()
root.title("Practice")  
root.geometry("600x600")
root.configure(bg = "#44AF3E")


# This function does the rolling part
def dice():
    show()
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'] 
    dice_1.config(text = f"{random.choice(dice)}")
    dice_2.config(text = f"{random.choice(dice)}")
    dice_3.config(text = f"{random.choice(dice)}")
    dice_4.config(text = f"{random.choice(dice)}")
    dice_5.config(text = f"{random.choice(dice)}")
    dice_6.config(text = f"{random.choice(dice)}")
    
#This function clears all the dice
def clearAll():
    dice_1.grid_forget()
    dice_2.grid_forget()
    dice_3.grid_forget()
    dice_4.grid_forget()
    dice_5.grid_forget()
    dice_6.grid_forget()


# This function takes the clicked variable and display the equal amount of dice
def show():
    clearAll()
    num = clicked.get()
    if num == "2":
        dice_2.grid(row = 0, column=1)
        dice_1.grid(row = 0, column=0)
    if num == "6":
        dice_2.grid(row = 0, column=1)
        dice_1.grid(row = 0, column=0)
        dice_3.grid(row = 0, column=2)
        dice_4.grid(row = 1, column=0)
        dice_5.grid(row = 1, column=1)
        dice_6.grid(row = 1, column=2)
    if num == "5":
        dice_2.grid(row = 0, column=1)
        dice_1.grid(row = 0, column=0)
        dice_3.grid(row = 0, column=2)
        dice_4.grid(row = 1, column=0)
        dice_5.grid(row = 1, column=1)
    if num == "4":
        dice_2.grid(row = 0, column=1)
        dice_1.grid(row = 0, column=0)
        dice_3.grid(row = 0, column=2)
        dice_4.grid(row = 1, column=0)
    if num == "3":
        dice_2.grid(row = 0, column=1)
        dice_1.grid(row = 0, column=0)
        dice_3.grid(row = 0, column=2)
    if num =="1":
        dice_1.grid(row=0,column=0)



#frames
heading_frame = Frame(root, bg = "#44AF3E")
heading_frame.pack(pady=10, padx=80)

frame_below_heading_frame = Frame(root, bg="#44AF3E")
frame_below_heading_frame.pack()

frame1 = Frame(root, bg="#44AF3E" , borderwidth=3, relief=RAISED, padx = 80)
frame1.pack()

button_frame = Frame(root, bg = "#44AF3E", pady= 20, padx=90)
button_frame.pack()


# This is the clicked variable
clicked = StringVar()
# initial menu text
clicked.set( "1")
# Dropdown menu options
options = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    ]
# Code to display the dropdown menu  
drop = OptionMenu( frame_below_heading_frame ,clicked, *options)
drop.grid(row = 1, column=0, padx=10,pady=20)


#the title label
heading = Label(heading_frame, text = "Dice Simulator", font = "Helvetica 30 bold" , bg="#44AF3E", fg="black")
heading.grid(row = 0, column=0)
    

# defining all the dice
dice_1 = Label(frame1, text ="\u2681", bg = "#44AF3E", fg="white", font = "Courier 100")
dice_2 = Label(frame1, text ="\u2685", bg = "#44AF3E", fg="white", font = "Courier 100")
dice_3 = Label(frame1, text ="\u2681", bg = "#44AF3E", fg="white", font = "Courier 100")
dice_4 = Label(frame1, text ="\u2685", bg = "#44AF3E", fg="white", font = "Courier 100")
dice_5 = Label(frame1, text ="\u2681", bg = "#44AF3E", fg="white", font = "Courier 100")
dice_6 = Label(frame1, text ="\u2685", bg = "#44AF3E", fg="white", font = "Courier 100")

# This is the initial dice that will be displayed on the screen
dice_1.grid(row = 0, column=0)



#the buttons
button = Button(button_frame, text="Roll", command=dice, bg="black", fg="white", font = "Courier 14 bold", padx=26, pady= 7)
button.pack()
ok = Button(frame_below_heading_frame, text = "ok" , command = show, bg="black", fg="white", font = "Courier 14 bold" )
ok.grid(row = 1, column=1)



root.mainloop()