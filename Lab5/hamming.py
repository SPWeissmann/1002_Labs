'''
Samuel Weissmann
spw2136
2019-10-02

Hamming: Find the Hamming distance between two strings, which is defined as
the nunmber of character substitutions required to make the two strings equal.
'''

def hammingDistance(str1, str2):
    if len(str1) < len(str2):
        short_str, long_str = str1, str2
    else:
        short_str, long_str = str2, str1

    difference = 0
    for i in range(len(short_str)):
        if short_str[i] != long_str[i]:
            difference += 1

    difference += len(long_str) - len(short_str)


    #Steps for project:

    # 1. For whichever string is shorter, look at each element.
    # 2. If the element being inspected does not match the element at the
    #    same index in the other string, change it so that it does
    # 3. When finished changing elements, add the remainder of the longer string
    #    onto the shorter string.
    # 4. Print to user what happens





