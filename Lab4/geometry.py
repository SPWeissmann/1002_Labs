# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.

import circle
import rectangle
import triangle
import sphere
import cylinder

# The main function.

def main():
    
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0

    while not(choice == 5):
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == 1:
            r = float(input("Enter the circle's radius: "))
            print('The area is {:.3f}.'.format(circle.area(r)))          
        elif choice == 2:
            radius = float(input("Enter the circle's radius: "))
            print('The circumference is {:.3f}'.\
                    format(circle.circumference(radius)))
        elif choice == 3:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print("The area is {:.3f}".format(rectangle.area(width, length)))
        elif choice == 4:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The perimeter is {:.3f}'.\
                    format(rectangle.perimeter(width, length)))
        elif choice == 5:
            base = float(input("Enter triangle's base length: "))
            height = float(input("Enter the triangle's height: "))
            print("The area is: {:.3f}".format(triangle.area(height,base)))
            
        elif choice == 6:
            side_a = float(input("Enter the length of the side a: "))
            side_b = float(input("Enter the length of the side b: "))
            side_c = float(input("Enter the length of the side c: "))
            print("The perimeter of the triangle is: {:.3f}".\
                  format(triangle.perimeter(side_a, side_b, side_c)))
        
        elif choice == 7: 
            radius = float(input("Enter the sphere's radius: "))
            print("The surface area of the sphere is: {:.3f}".\
                  format(sphere.surface(radius)))
        
        elif choice == 8:
            height = float(input("Enter the sphere's height: "))
            radius = float(input("Enter the sphere's radius: "))
            print("The volume of the sphere is: {:.3f}".\
                  format(sphere.volume(height,radius)))
        
        elif choice == 9:
            height = float(input("Enter the cylinder's height: "))
            radius = float(input("Enter the cylinder's radius: "))
            print("The surface area of the cylinder is: {:.f}".\t
                  format(cylinder.surface(height, radius)))
        
        elif choice == 10:
            height = float(input("Enter the cylinder's height: "))
            radius = float(input("Enter the cylinder's radius: "))
            print("The volume of the cylinder is: {:.f}".\
                  format(cylinder.volume(height, radius)))
            
        elif choice == 0:
            print("Exiting the program...")
        else:
            print("Error: invalid selection.")
    
# The display_menu function displays a menu.
def display_menu():
    print("        MENU for ")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Area of a triangle")
    print("6) Perimeter of a triangle")
    print("7) Surface area of a sphere")
    print("8) Volume of a sphere")
    print("9) Surface area of a cylinder")
    print("10) Volume of a cylinder")
    print("0) Quit")

# Call the main function.
main()

