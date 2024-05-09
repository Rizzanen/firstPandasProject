


# If you specifically need to import functions:
from calculations import getAverage, getAverageOfYears, getAverageOfMonth, getMax, getMin 



def welcome():
    print("Welcome to my project! ")
    print("Here you can analyze data of finnish exchange electricity prices between 2021-2024.")
    options()

def options():    
    print("For average price type 1")
    print("For average price of each year type 2")
    print("For averages of years months type 3")
    print("For max value type 4")
    print("For min value type 5")
    print("To quit type x")
    userInput = input("Type a number and press enter \n")

    if userInput == "1":
        print("\n")
        getAverage()
        print("\n")
        options()
    elif userInput == "2":
        print("\n")
        getAverageOfYears()
        print("\n")
        options()
    elif userInput == "3":
        print("\n")
        getAverageOfMonth()
        print("\n")
        options()
    elif userInput == "4":
        print("\n")
        getMax()
        print("\n")
        options()
    elif userInput == "5":
        print("\n")
        getMin()
        print("\n")
        options()
    elif userInput == "x":
        return
    else:
        print("\n")
        print("Please type 1, 2, 3, 4, 5 or x")
        print("\n")
        options()



welcome()



