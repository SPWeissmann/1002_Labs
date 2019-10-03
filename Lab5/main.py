'''
Samuel Weissmann
spw2136
2019-10-02

Main function for code, from which all other functions will be called
'''
import hamming as h
import palindrome as p


def main():
    choice = ""
    while choice != "q":
        print("Please select what you would like to computer:")
        print("h) Hamming distance between two strings of equal length.")
        # print("h2) Hamming distance between two strings of any length")
        print("p) If a string is a palindrome.")
        print("q) to quit.")
        choice = input("")

        if choice == "p":
            input_str = input("Please type the string that you would like to check: ")

            if p.isPalindrome(input_str):
                print(input_str," is a palindrome")
            else:
                print(input_str, "is not a palindrome")

        if choice == "h":

            input_str1 = input("Please enter the first string: ")
            input_str2 = input("Please enter the second string: ")
            hamming_dist = h.hammingDistance(input_str1, input_str2)
            print("The hamming distance between",input_str1," and ",\
                  input_str2," is ",hamming_dist)

        # if choice == "h2":
        #     input_str1 = input("Please enter the first string: ")
        #     input_str2 = input("Please enter the second string: ")
        #     hamming_dist = h.hammingDistance2(input_str1, input_str2)
        #     print("The hamming distance between",input_str1," and ",\
        #           input_str2," is ",hamming_dist)

        if choice == "q":
            print("Goodbye!")


    #discussioning main method for vietnam
    # talk about how variable names don't need to match
    # Discuss scope with students
    # Discuss functions and functions usage within codes.