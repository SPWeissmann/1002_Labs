'''main function for code, from which all my other functions will be called'''
import hamming as h
import palindromes as p


def main():

    strA = input("please enter the first string")
    strB = input("please enter the second string")
    dist = hammingDistance(strA, strB)

    #discussioning main method for vietnam
    # talk about how variable names don't need to match
    # Discuss scope with students
    # Discuss functions and functions usage within codes.