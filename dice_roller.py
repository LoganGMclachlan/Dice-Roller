from tkinter import END, Tk, Label, Button, Text, Entry
from random import randint

def randomize():

    sizes = []

    if entry1.get() != "":
        sizes.append(int(entry1.get()))
    if entry2.get() != "":
        sizes.append(int(entry2.get()))
    if entry3.get() != "":
        sizes.append(int(entry3.get()))
    if entry4.get() != "":
        sizes.append(int(entry4.get()))
    if entry5.get() != "":
        sizes.append(int(entry5.get()))
    if entry6.get() != "":
        sizes.append(int(entry6.get()))

    dice_nums = []
    ran_num = 0
    for size in sizes:
        ran_num = randint(1,size)
        dice_nums.append(ran_num)


        
    dice1 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
    dice1.grid(row=2,column=0)

    dice2 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
    dice2.grid(row=2,column=1)

    dice3 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
    dice3.grid(row=2,column=2)

    dice4 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
    dice4.grid(row=4,column=0)

    dice5 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
    dice5.grid(row=4,column=1)

    dice6 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
    dice6.grid(row=4,column=2)


    if len(dice_nums) >= 1:
        dice1.insert(END,dice_nums[0])
    if len(dice_nums) >= 2:
        dice2.insert(END,dice_nums[1])
    if len(dice_nums) >= 3:
        dice3.insert(END,dice_nums[2])
    if len(dice_nums) >= 4:
        dice4.insert(END,dice_nums[3])
    if len(dice_nums) >= 5:
        dice5.insert(END,dice_nums[4])
    if len(dice_nums) == 6:
        dice6.insert(END,dice_nums[5])




 # ---------------------------------------------------------------- #
window = Tk()
window.title("Dice Roller")
window.geometry("230x190")
window.configure(background="grey")

Label(window,text="Dice Roller",font="30",bg="grey").grid(row=0,column=1)
Label(window,text="enter the size of each dice",bg="grey").grid(row=1,column=1)

dice1 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
dice1.grid(row=2,column=0)

dice2 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
dice2.grid(row=2,column=1)

dice3 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
dice3.grid(row=2,column=2)

entry1 = Entry(window, width="4")
entry1.grid(row=3,column=0)
entry1.insert(0, "20")

entry2 = Entry(window, width="4")
entry2.grid(row=3,column=1)
entry2.insert(0, "12")

entry3 = Entry(window, width="4")
entry3.grid(row=3,column=2)
entry3.insert(0, "10")


dice4 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
dice4.grid(row=4,column=0)

dice5 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
dice5.grid(row=4,column=1)

dice6 = Text(master=window,width=2,height=1,bd=2,font=20,padx=10,pady=10)
dice6.grid(row=4,column=2)


entry4 = Entry(window, width="4")
entry4.grid(row=5,column=0)
entry4.insert(0, "8")

entry5 = Entry(window, width="4")
entry5.grid(row=5,column=1)
entry5.insert(0, "6")

entry6 = Entry(window, width="4")
entry6.grid(row=5,column=2)
entry6.insert(0, "4")

Button(window,text="roll dice",command=randomize,bg="black",fg="white").grid(row=6,column=1)


window.mainloop()