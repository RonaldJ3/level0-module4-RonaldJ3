"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
pistring = "3.1415926535897932384"

    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384
print(pistring[0])
print(pistring[1])
print(pistring[2])
print(pistring[3])
piindex = 3
while True:
    anwser = simpledialog.askstring(None,"what is the digit at" + str(piindex))
    if anwser == pistring[piindex]:
        piindex += 1
        messagebox.showinfo(None, 'Correct!')
    else:
        messagebox.showinfo(None, "incorrect")
        break
messagebox.showinfo(None, "you got" + str(piindex - 4))
    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit

    # TODO) Use a while loop to keep asking for the next digit of pi


        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
