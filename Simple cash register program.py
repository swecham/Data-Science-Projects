# File: Chamala_week11.py
# Author: Swetha Chamala
# Date: 11/10/19
# Course: DSC510 - Introduction to programming
# Description: Sample cash register program using Python object oriented programming
import locale

locale.setlocale(locale.LC_ALL, 'en_US')


class CashRegister:

    def __init__(self):
        print("Welcome to Grocery Store Cash register")
        self.itemCount = 0
        self.totalPrice = 0.0

    def add_item(self, price):  # adds item to register
        self.itemCount = self.itemCount + 1
        self.totalPrice += price
        print("The item is added to Cash Register\n")

    def get_total(self):  # return total price
        return self.totalPrice

    def get_count(self):  # return count of items
        return self.itemCount

    def clear(self):  # reset register to zero
        self.itemCount = 0
        self.totalPrice = 0


s = CashRegister()
more_items = input("Would you like to enter items?: Y/N\n").lower()
item_price = None
while True:
    if more_items == 'y':
        item_price = float(input("please enter price of item:\n"))
        s.add_item(item_price)
        more_items = input("Would you like to enter more items?: Y/N\n").lower()
    elif more_items == 'n':
        totalCount = s.get_count()
        print('Total number of items in your cart:', totalCount)
        s.get_total()
        print("Total price of items in your cart =", locale.currency(s.get_total()))
        break
    else:
        print("Please enter valid input")
        more_items = input("Would you like to enter more items?: Y/N\n").lower()
