# File: hw6_part1.py
# Author: olutoye sekiteri
# Date: 4/28/17
# Section: 23
# E-mail: olutoye1@umbc.edu
# Description:
# checks if the users input is a palindrome if not it puts word in reverse
##############################################
# reverse()    reverse the user's word
# input()      word; word user selects
# output()     rev; reversed word
def reverse(word):

    if word == "":
        return word
    else:
        return word[-1] + reverse(word[:-1])
###############################################
# palindrome1()    checks if word has a space
# input:           word; user's word
# output:          bool; returns false if word has a space

def palindrome1(word):
    for i in range(len(word)-1):
        if word[i]==" ":
            return False
###############################################
# palindrome2()    checks if word is a palindrome
# input:           word; user's word
# output:          bool; returns true if palindrome

def palindrome2(word):
    #for index in word if the string index count forward doesnr equal one
    #counting backward then is false
    for i in range(len(word)-1):
        if word[i].upper() !=word[(len(word)-1)-i].upper():
            return False
        else:
            return True


def main():
    word=input("Please enter a word to check for palindrome-ness: ")
    boole1=palindrome2(word)
    boole2=palindrome1(word)

    rev=reverse(word)
    #if either is false then is not palindrome
    if boole2==False or boole1==False:
        print("Sorry, the word",word,"is not a palindrome")
        print("Backwards, it becomes",rev)
    else:
    	print("The word",word,"IS a palindrome")
main()

