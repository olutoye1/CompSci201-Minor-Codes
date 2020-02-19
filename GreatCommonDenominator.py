# File: hw6_part2.py
# Author: olutoye sekiteri
# Date: 4/28/17
# Section: 23
# E-mail: olutoye1@umbc.edu
# Description:
# code determines the greatest common divisor of two integer of the the user's choices

#######################################
# checkInts()    check if integer can be used
# input:         none
# output         int1; first integer
#                int2; second integer
def checkInts():
    #checks if integer user inputted is viable
    int1=int(input("please enter the first integer: :"))
    while int1 < 1:
        print("Integer must be greater than or eqaul to 1")
        int1=int(input("please enter the first integer: :"))
    int2=int(input("please enter the second integer: "))
    while int2 < 1:
        print("Integer must be greater than or eqaul to 1")
        int2=int(input("please enter the second integer: :"))
    return int1, int2
##############################################3
# gcd()    solves for the gcd of both ints
# input    int1: first int
#           int2; second int
# output   int1; first int is updated and repurposed as gcd of starting integers
def gcd(int1,int2):
#dont understand the purpose of the third arugument in hw plan or how to impliment it


    # Base case
    if int2 == 0:
        return int1

    # Recursive case
    return gcd(int2, int1 % int2)


def main():

    int1,int2=checkInts()
    gcdd=gcd(int1,int2)

    print("The GCD for",int1,"and",int2,"is",gcdd)
main()
