import sys
import math

# (1) What this program does:
# It solves a quadratic equation: a*x^2 + b*x + c = 0
# It expects you to provide a, b, c as command-line inputs when starting the program.

def do_stuff():
    # (2) What the error is
    # When code is run in IDE, python only gives 1 arguments however
    # the code we made needs 3 arguements which dont exist so python gives index error
    # Also quotations in print f statemnts were incorrect syntax and were corrected

    # Fix: check if the user actually provided 3 arguments (a, b, c).
    if len(sys.argv) != 4:
        print("ERROR: Missing inputs.")
        print("This program needs 3 numbers: a b c")
        return

    # Read inputs from the command line
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    
    if a == 0:
        print("ERROR: a cannot be 0 for a quadratic equation.")
        return

   
    d = b**2 - 4*a*c

    if d > 0:
        
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        print(f"The solutions are: {r1}, {r2}")
    elif d == 0:
       
        r = -b / (2*a)
        print(f"The solution is: {r}")
    else:
       
        print("There are no real solutions.")

do_stuff()
