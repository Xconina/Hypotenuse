#hypotenuse.py
#This program computes the hypotenuse for 3 different sized right triangles
#By Ashley Cook

import math

def main():
    print ("This program computes the hypotenuse for 3 different sized right triangles.")
    for i in range(3):
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = math.sqrt(a**2 + b**2)
        print ("The hypotenuse is", "{:.2f}".format(c))

main()

