import tkinter
from tkinter import messagebox
from random import randint

window = tkinter.Tk()

def lottery_number_generator():
    loto_list = []
    while True:
        loto_number = randint(1, 50)
        if loto_number not in loto_list:
            loto_list.append(loto_number)

        if len(loto_list) == int(input.get()):
            break
    messagebox.showinfo("Loto numbers: ", loto_list)


welcome = tkinter.Label(window,  text ="Welcome to the Lottery numbers generator.\n" +
"Please enter how many random numbers would you like to have: ")
welcome.pack()

input = tkinter.Entry(window)
input.pack()

submit = tkinter.Button(window, text = "Submit", command = lottery_number_generator)
submit.pack()



window.mainloop()
