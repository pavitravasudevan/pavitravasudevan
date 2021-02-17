#!usr/bin/env python3

print("Hello guys")

def chocolate_lovers(choice):
    if choice.lower() == "dark":
        print("You have an amazing choice!!")
    else:
        print("Well not a bad choice!!")
choice = ("Enter the type of chocolate you want to buy(dark/milk/white/ruby): ")
chocolate_lovers(choice)
    
