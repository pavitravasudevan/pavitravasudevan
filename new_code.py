#!usr/bin/env python3

print("Hello guys")

def chocolate_lovers(choice):
    if choice.lower() == "dark":
        print("You have an amazing choice!!")
    elif choice.lower() == "ruby":
        print("The naturally pink tasty chocolate, really expensive though!!")
    elif choice.lower() == "milk":
        print("Tasty buttery milky!!")
    elif choice.lower() == "white":
        print("Too much sweet!!")
    else:
        print("Please enter any four of the valid choice next time(dark/milk/white/ruby)")

choice = ("Enter the type of chocolate you want to buy(dark/milk/white/ruby): ")
chocolate_lovers(choice)
