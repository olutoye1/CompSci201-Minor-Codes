# File:    scramble.py
# Started: by Dr. Gibson (updated by Kristin McLaughlin)
# Author:  olutoye sekiteri
# Date:    5/3/17
# Section: 23
# E-mail:  olutoye1@umbc.edu
# Description:
#   This file contains python code that computes all of
#   the possible combinations of a string's characters.


# permute() is a recursive function that scrambles a string
# Input:    currentScramble; the scrambled word so far
#           lettersLeft;     the letters left to scramble
# Output:   none;            prints out each scramble as it's completed
def permute(currentScramble, lettersLeft):

    # BASE CASE: __________
    if len(lettersLeft)== 0:
        # print out the ______ variable to see the result
        print(currentScramble)

    # RECURSIVE CASE:
    else:
        # for each letter still available for scrambling
        for letter in lettersLeft:

            # create a copy of the string without that letter
            # (this code removes the FIRST instance of the letter)
            # (for example: if string was "2010", now it's "210")
            newLettersLeft = lettersLeft.replace(letter, "", 1)

            # add the letter we removed from lettersLeft
            # to the current scrambled word, call it newScramble
            newScramble = currentScramble+letter
            # RECURSIVE CALL: use the new variables for this call
            permute(newScramble, newLettersLeft)


def main():

    print("Welcome to the Scrambler!")
    word = input("Please enter a string to scramble: ")
    currentScramble=""
    # call the recursive function here
    permute(currentScramble, word)

    print("Thank you for using the Scrambler!\n")

main()
