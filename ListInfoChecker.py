# File: hw7.py
# Author: Olutoye Sekiteri
# Date: 11/2/16
# Section: 29
# E-mail: olutoye1@umbc.edu
# Description:
# The code provide the user with a menu of choice in which the user can create a list and check if list's content are the same, different, or in alphabetical order
# Collaboration:
# I did not collaborate with anyone on the assignment



#Takes in users input for numbers for list and sentinel and returns a list
def createIntList():
    listOfNum=[]
    sentinel=int(input("What would you like to be your sentinel "))
    numForList=int(input("Please enter a number,"+str(sentinel)+"to stop"))
    while numForList != sentinel:
        listOfNum.append(numForList)
        numForList=int(input("Please enter a number,"+str(sentinel)+"to stop"))
    return listOfNum
#Takes in user's input and check if it meets parameters
def getValidInt(number):
    number = int(input("Enter an integer between 1 and 5 (inclusive): "))
    while number < 1 or  number > 5:
        print("")
        number = int(input("Enter an integer between 1 and 5 (inclusive): "))

    return number
#Print out menu of choices
def printMenu():
    print("Welcome to the List Info Checker")
    print("")
    print("Please make a choice from the menu: ")
    print("1 - Create a list")
    print("2 - Check if  list is all same")
    print("3 - Check if list is all different")
    print("4 - Check if list is sorted")
    print("5 - Exit the program")

# This function takes a boolean and list and checks if the values of the list are diffrent
def allTheSame(listNum):
    same= True
    for i in range(len(listNum)):
        if listNum[0] == listNum[i]:
            same= True
        else:
            same= False
    return same
# This function takes a boolean and list and checks if the values of the list are diffrent
def allDifferent(listNum):
    diff=True
    for i in range(len(listNum)):
        if listNum[0] != listNum[i]:
            diff= True
        else:
            diff= False

    return diff
#This function takes the list list and checks if the values of the list are in order from least to greatest
def sortede(listNum):
    sort=True
    for i in range(len(listNum)-1):

        if listNum[i]< listNum[i+1]:
            sort= True
        else:
            sort= False
    return sort

def main():
    menuSelectNum=0
    printMenu()
    menuSelectNum= getValidInt(menuSelectNum)

    while menuSelectNum != 5:
        if menuSelectNum==1:
            listOfNum=createIntList()
            menuSelectNum= getValidInt(menuSelectNum)
        elif menuSelectNum==2:
            same= allTheSame(listOfNum)
            if same==True:
                print("The list" + str(listOfNum)+ "is all the same element")
            else:
                print("The list" + str(listOfNum)+ "is not all the same element")
            menuSelectNum= getValidInt(menuSelectNum)
        elif menuSelectNum==3:
            diff= allDifferent(listOfNum)
            if diff==True:
                print("The list" + str(listOfNum)+ "is all the unique elements")
            else:
                print("The list" + str(listOfNum)+ "is not  all unique elements")
            menuSelectNum= getValidInt(menuSelectNum)
        elif menuSelectNum==4:
            sort= sortede(listOfNum)
            if sort==True:
                print("The list" + str(listOfNum)+ "is sorted")
            else:
                print("The list" + str(listOfNum)+ "is not sorted")
            menuSelectNum= getValidInt(menuSelectNum)
        printMenu()
    print("Thank you for using the List Info Checker")
main()