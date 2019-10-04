'''
Samuel Weissmann
spw2136
2019-10-02
Combines required functions into one file, instead of splitting them up

hammingDistance: Find the Hamming distance between two strings, which is defined as
the nunmber of character substitutions required to make the two strings equal.

isPalindrome: Tests if a string is a palindrome
'''


def isPalindrome(str1):
    return str1 == str1[::-1]


def hammingDistance(str1, str2):
    difference = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            difference += 1

    return difference

def hammingDistance2(str1, str2):
    '''Can define the hamming distance between two strings of unequal length'''

    #identify shorter string
    if len(str1) < len(str2):
        short_str, long_str = str1, str2
    else:
        short_str, long_str = str2, str1

    #counter difference between shorter and longer string
    difference = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            difference += 1

    #add on the difference that results from shorter string missing characters
    difference += len(long_str) - len(short_str)

    return difference