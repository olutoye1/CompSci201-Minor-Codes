# File: hw6.py
# Author: Olutoye Sekiteri
# Date: 10/26/16
# Section: 29
# E-mail: olutoye1@umbc.edu
# Description:
# The code takes the user input for number of lists, sentinel value, and content of the lists and gives the summation and product of the list
# Collaboration:
# I did not collaborate with anyone on the assignment


def createIntList(listNum,num,cent):
    cent=int(input("What would you like to be your sentinel  "))
    while num != cent:
        num=int(input("Please enter a number,"+str(cent)+"to st\
op: "))
        if num!=cent:
            listNum.append(num)


    return listNum

def summation(val,listNum):
    listOfN=[]
    for f in listNum:
        val=val + int(f)

    return val

def multiply(aNum,listNum):
    listOfN=[]
    for i in listNum:
        aNum=aNum * int(i)

    return aNum
def main():
    listOfN=[]
    addVal=0
    multiplyVal=1
    userNum=int(82837382829837382738182829228738)
    sentinel=0

    print("Welcome to the Simple Math Helper")
    numOfL=int(input("How many lists would you like to create?  "))
    if numOfL<=0:
        print("Thank you for using the Simple Math Helper")
    for n in range(numOfL):
        print("you are creating list # ", n+1)
        finalList=createIntList(listOfN,userNum,sentinel)
        addition=summation(addVal,listOfN)
        product=multiply(multiplyVal,listOfN)
        print(finalList)
		print("The summation of your list is",addition)
        print("The product of your list is",product)

main()

# File: hw6.py
# Author: Olutoye Sekiteri
# Date: 10/26/16
# Section: 29
# E-mail: olutoye1@umbc.edu
# Description:
# The code takes the user input for number of lists, sentinel value, and content of the lists and gives the summation and product of the list
# Collaboration:
# I did not collaborate with anyone on the assignment


def createIntList(listNum,num,cent):
    cent=int(input("What would you like to be your sentinel  "))
    while num != cent:
        num=int(input("Please enter a number,"+str(cent)+"to st\
op: "))
        if num!=cent:
            listNum.append(num)


    return listNum

def summation(val,listNum):
    listOfN=[]
    for f in listNum:
        val=val + int(f)

    return val

def multiply(aNum,listNum):
    listOfN=[]
    for i in listNum:
        aNum=aNum * int(i)

    return aNum
def main():
    listOfN=[]
    addVal=0
    multiplyVal=1
    userNum=int(82837382829837382738182829228738)
    sentinel=0

    print("Welcome to the Simple Math Helper")
    numOfL=int(input("How many lists would you like to create?  "))
    if numOfL<=0:
        print("Thank you for using the Simple Math Helper")
    for n in range(numOfL):
        print("you are creating list # ", n+1)
        finalList=createIntList(listOfN,userNum,sentinel)
        addition=summation(addVal,listOfN)
        product=multiply(multiplyVal,listOfN)
        print(finalList)
print("The summation of your list is",addition)
        print("The product of your list is",product)

main()
