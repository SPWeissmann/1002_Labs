'''
Samuel Weissmann
spw2136
2019-10-02

Main function, just used for testing whatever we come up with for palindromes
and hamming functions
'''
import lab5 as l

def main():
    while True:
        print("\nPlease type an option from the menu, or press anything else to quit:")
        print("\t h: Hamming distance between two strings of equal length.")
        # print("h2: Hamming distance between two strings of any length")
        print("\t p: If a string is a palindrome.")
        choice = input("\t: ")

        if choice == "p":
            input_str = input("Please type the string that you would like to check: ")
            if l.isPalindrome(input_str):
                print(input_str," is a palindrome")
            else:
                print(input_str,"is not a palindrome")

        elif choice == "h":
            input_str1 = input("Please enter the first string: ")
            input_str2 = input("Please enter the second string: ")
            #check inputs
            if len(input_str1) == len(input_str2):
                hamming_dist = l.hammingDistance(input_str1, input_str2)
                print("The hamming distance between",input_str1,"and",\
                      input_str2,"is",hamming_dist)
            else:
                print("Please enter two strings of same length.")

        # if choice == "h2":
        #     input_str1 = input("Please enter the first string: ")
        #     input_str2 = input("Please enter the second string: ")
        #     hamming_dist = l.hammingDistance2(input_str1, input_str2)
        #     print("The hamming distance between",input_str1," and ",\
        #           input_str2," is ",hamming_dist)

        else:
            print("Goodbye!")
            break
main()

    #discussioning main method for vietnam
    # talk about how variable names don't need to match
    # Discuss scope with students
    # Discuss functions and functions usage within codes.