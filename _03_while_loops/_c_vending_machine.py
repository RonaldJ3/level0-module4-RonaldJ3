"""
Calculate the value of the change (coins) the user has.
"""
from tkinter import messagebox, simpledialog, Tk


# Write you code under the if __name__ == '__main__': below
def vending_machine(money):
    items_for_sale = {"water" : 0.50, "soda" : 1.00, "pretzels" : 1.00, "candy bar" : 1.50, "exit" : 0.00}

    while True:
        intro_str = "Welcome to the vending machine! You have " +\
                    str("{:.2f}".format(money)) + " dollars left.\n"
        intro_str += "Enter the item you want to buy?\n"

        for item, cost in items_for_sale.items():
            intro_str += item + ' - $' + str("{:.2f}".format(cost)) + '\n'

        item_num = simpledialog.askstring(title='Vending Machine', prompt=intro_str)

        # Cancel button pressed
        if item_num is None:
            return 0.00
        elif item_num in items_for_sale:
            return items_for_sale[item_num]
        else:
            messagebox.showwarning('Invalid item',
                                   'Please enter one of the following ' + str([item for item in items_for_sale]))

# ======================= DO NOT EDIT THE CODE ABOVE =========================


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    money_in_dollars = 3.00

    # TODO) Write a while loop that ends when you have no money left
    while money_in_dollars =< 0:

        # TODO) Call the vending_machine() function and save the money spent
        #  in a variable, for example:
        #  money_spent = vending_machine(money_in_dollars)
