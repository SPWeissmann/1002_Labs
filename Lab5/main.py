'''
Samuel Weissmann
spw2136
2019-10-02

Adds some structure for testing and playing with the functions we wrote during
lab 5. I also added an additional hamming distance function to handle strings
of different lengths. See lab5.py for implementation details.
'''
import lab5 as l

def main():

    while True:
        print("\nPlease type an option from the menu, or press anything "
              "else to quit:")
        print("\t h: Calculate the Hamming distance between two strings "
              "of equal length.")
        print("\t h2: Hamming distance between two strings of any length")
        print("\t p: Check if a string is a palindrome.")
        choice = input("\t ")

        if choice == "p":
            input_str = input("Please type the string that you would "
                              "like to check: ")
            if l.is_palindrome(input_str):
                print(input_str," is a palindrome")
            else:
                print(input_str,"is not a palindrome")

        elif choice == "h":
            input_str1 = input("Please enter the first string: ")
            input_str2 = input("Please enter the second git sstring: ")
            #check inputs
            if len(input_str1) == len(input_str2):
                hamming_dist = l.hamming_distance(input_str1, input_str2)
                print("The hamming distance between '{}' and '{}' is {}."\
                    .format(input_str1, input_str2, hamming_dist))
            else:
                print("Please enter two strings of same length.")

        if choice == "h2":
            input_str1 = input("Please enter the first string: ")
            input_str2 = input("Please enter the second string: ")
            hamming_dist = l.hamming_distance2(input_str1, input_str2)
            print("The hamming distance between",input_str1," and ",\
                  input_str2," is ",hamming_dist)

        else:
            print("Goodbye!")
            break
        
#ensures that code will only run if this is the "main" file being executed
if __name__== "__main__":
    main()