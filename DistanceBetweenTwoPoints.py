# File:  hw5_part1.py
# Author: olutoye sekiteri
# Date: 4/7/17
# Section: 23
# E-mail: olutoye1@umbc.edu
# Description:
# this code solves for the distance of two points


###################################################
# getTupl()   get all point values from user
# Input:      none
# Output:     tupl1; the first point user entered
#             tupl2; the second point user entered
def getTupl():

    x1=int(input("Please enter a value for x1: "))
    y1=int(input("Please enter a value for y1: "))
    x2=int(input("Please enter a value for x2: "))
    y2=int(input("Please enter a value for y2: "))

    tupl1=(x1,y1)
    tupl2=(x2,y2)

    return tupl1, tupl2
####################################################
# distance()   calculate the distance between points
# Input:       tupl1; the first point user entered
#              tupl2; the second point user entered
# Output:      total; the total distance
def distance(tupl1,tupl2):
    total=(((tupl2[0]-tupl1[0])**2+(tupl2[1]-tupl1[1])**2))**.5

    return total

def main():

    print("This program will ask for two points, and")
    print("will compute the distance between the two.")

    tupl1,tupl2=getTupl()
    total=distance(tupl1,tupl2)

    print("the distance between",tupl1,"and",tupl2,"is",total)
main()
