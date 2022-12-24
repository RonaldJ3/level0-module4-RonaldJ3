"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    pi0 = 3
    pi1 = 1
    pi2 = 4
    pi3 = 1
    pi4 = 5
    pi5 = 9
    pi6 = 2
    pi7 = 6
    pi8 = 5
    pi9 = 3
    pi10 = 5
    pi11 = 8
    pi12 = 9
    pi13 = 7
    pi14 = 9
    pi15 = 3
    pi16 = 2
    pi17 = 3
    pi18 = 8
    pi19 = 4


    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384

    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit
    print(pi0,pi1,pi2)

    pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")

    # TODO) Use a while loop to keep asking for the next digit of pi
    while pi == "1":
        print(pi3)
        print("correct")
        pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
        while pi == "5":
            print(pi4)
            print("correct")
            pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
            while pi == "9":
                print(pi5)
                print("correct")
                pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
                while pi == "2":
                    print(pi6)
                    print("correct")
                    pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
                    while pi == "6":
                        print(pi7)
                        print("correct")
                        pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
                        while pi == "5":
                            print(pi8)
                            print("correct")
                            pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
                            while pi == "3":
                                print(pi9)
                                print("correct")
                                pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
                                while pi == "5":
                                    print(pi10)
                                    print("correct")
                                    pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
                                    while pi == "8":
                                        print(pi11)
                                        print("correct")
                                        pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
                                        while pi == "9":
                                            print(pi12)
                                            print("correct")
                                            pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
                                            while pi == "7":
                                                print(pi13)
                                                print("correct")
                                                pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
                                                while pi == "9":
                                                    print(pi14)
                                                    print("correct")
                                                    pi = simpledialog.askstring(title="Num",prompt="Type the next digit of pi ")
                                                    while pi == "3":
                                                        print(pi15)
                                                        print("correct")
                                                        pi = simpledialog.askstring(title="Num", prompt="Type the next digit of pi ")
                                                        while pi == "2":
                                                            print(pi16)
                                                            print("correct")
                                                            pi = simpledialog.askstring(title="Num",prompt="Type the next digit of pi ")
                                                            while pi == "3":
                                                                print(pi17)
                                                                print("correct")
                                                                pi = simpledialog.askstring(title="Num",prompt="Type the next digit of pi ")
                                                                while pi == "8":
                                                                    print(pi18)
                                                                    print("correct")
                                                                    pi = simpledialog.askstring(title="Num",prompt="Type the next digit of pi ")
                                                                    while pi == "4":
                                                                    print(pi19)
                                                                    print("correct")
                                                                    simpledialog(title="Done", prompt="Your done")

        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
