'''
Samuel Weissmann
spw2136
2019-10-02

Skeleton code for the lab 5 file, to fill in during the lab.
'''

def isPalindrome():
    '''Takes in a string, tests if it is a palindrome, and returns
    True or False'''
    #code goes here
    pass


def hamming_distance(s1,s2):
    '''Takes in two strings of equal length, and returns the hamming
    distance between them'''
    count = 0
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count = count + 1
            
    return count

def do_stuff(str1, int1):
    '''Example of a function where the order of the arguments matter when 
    calling it.
    
    Takes an integer and a string, and prints the string to 
    the user and prints the value of the integer + 1 to the user'''
    
    print(str1)
    print(int1 + 1)
    
    return True
        
    
def main():
    '''Prompts the user to choose whether to check a palindrome
    or the hamming distance, and then computes tha answer using
    the functions defined above'''
    
    
    input1 = input("please type something")
    input2 = input("please type something")
    
    hamming_distance(input1, input2)
    
    #end of main function

#What do we need to add here in order to make file run when executed?


#end of file


