'''
Samuel Weissmann
spw2136
2019-10-02

Contains the code that was collaboratively written during lab 5. I also
added a hamming_distance2 function which will detect the hamming distance
for two strings of unequal length. The logic is fundamentally the same,
but it needs to take a few more factors into consideration.
'''

def is_palindrome(str1):
    '''Takes in a string, tests if it is a palindrome, and returns
    True or False'''
    return str1 == str1[::-1]


def hamming_distance(str1, str2):
    '''Find the Hamming distance between two strings of equal length, which is
    defined as the number of character substitutions required to make the
    two strings equal.'''
    difference = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            difference += 1

    return difference

def hamming_distance2(str1, str2):
    '''Can define the hamming distance between two strings of unequal length.'''

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