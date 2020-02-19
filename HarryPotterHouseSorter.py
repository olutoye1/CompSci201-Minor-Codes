# File:    hw8.py
# Author:  Olutoye Sekiteri
# Date:    11/23/2016
# Section: 29
# E-mail:  olutoye1@umbc.edu
# Description:
# The great house sorter code
# Collaboration:
# I did not collaborate with anyone on this assignment


import random


#This function sort the dictonary for all the houses
def fileSort():
    input_file = open(input('Please enter filename to load from:'), 'r')
    house= []
    member = []
    memberList = dict()
    for line in input_file:
        houseHold, nameHold = line.split(",")
        houseHold = houseHold.strip()
        nameHold = nameHold.strip()
        memberList.setdefault(houseHold,[])
        memberList[houseHold].append(nameHold)

    input_file.close()
    return memberList, house
#This function takes the users input for the house and checks if valid then prints list
def printOneHouse(memberList):
    choice=input("What house's members would you like to print? ")

    if choice in memberList:
        print("The members of the house of",choice,"are")
        print(memberList[choice])
    else:
        print("There is no house by the name", choice)
#This function prints out all the houses and their members
def printAllHouse(memberList):
    for x in memberList:
        print ("The members of the house of",x,"are")
        for y in memberList[x]:
            print (y)
#This function prints the menu and gets the users selection
def printMenu():
    print("Please make a choice from the menu:")
    print("1 - Print a single house")
    print("2 - Print all the houses")
    print("3 - Sort a new person into a house")
    print("4 - Exit the program")

    userChoice=int(input("Please enter a number between 1 and 4 (inclusive): "))
    return userChoice
#Randomly selects the house a new member will be placed into
def houseSort(house, memberList):
    name=input("What is the person's name? ")
    selection=input("What house do they prefer? ")
    keyList = list()
    for i in memberList.keys():
        keyList.append(i)
    n = len(keyList)
    for i in range(len(keyList)):
        if selection == keyList[i]:
            keyList.append((keyList[i])*n)
    selection=random.choice(keyList)
    memberList[name] = selection
    print(name,"was sorted into house",selection)
    return memberList

def main():
    memberList,house=fileSort()
    print("")
    userChoice=printMenu()

    while userChoice!=4:
        if userChoice==1:
            printOneHouse(memberList)
            print("||||||||||||||||||||||||||||||||||")
            userChoice=printMenu()
        if userChoice==2:
            printAllHouse(memberList)
            print("||||||||||||||||||||||||||||||||||")
            userChoice=printMenu()
        if userChoice==3:
            memberList=houseSort(house,memberList)
            print("||||||||||||||||||||||||||||||||||")
            userChoice=printMenu()
    print("Thank you for using the Great Houses Program")

main()


