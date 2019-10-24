'''
Samuel Weissmann
spw2136
2019-10-02

Skeleton code for the lab 5 file, to fill in during the lab.
'''

def is_palindrome(s1):
    '''Takes in a string, tests if it is a palindrome, and returns
    True or False'''
    return (s1 == s1[::-1])


def hamming_distance(s1,s2):
    '''Takes in two strings of equal length, and returns the hamming
    distance between them'''
    count = 0
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count = count + 1
            
    return count
        
    
def main():
    '''Prompts the user to choose whether to check a palindrome
    or the hamming distance, and then computes tha answer using
    the functions defined above'''
    
    
    input1 = input("please type something")
    input2 = input("please type something")
    
    hamming_distance(input1, input2)
    
    #end of main function



main()