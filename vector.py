#Vector Addition Calculator

import math

# Input Magnitude

magnitudeA = float(input("What is the magnitude of the first vector? "))
magnitudeB = float(input("What is the magnitude of the second vector? "))
units = str(input("What are the units of magnitude? "))

# Input Angle

angleA = float(input("What is the angle of the first vector in degrees? "))
dirA1 = str(input("What direction? "))
dirA2 = str(input("of? "))

# Convert Angle to a value between 0 and 360

if dirA1 == "N":
    print("north")
elif dirA1 == "S":
    print("south")
elif dirA1 == "E":
    print("east")
elif dirA1 == "W":
    print("west")

print("of")

if dirA2 == "N":
    print("north")
elif dirA2 == "S":
    print("south")
elif dirA2 == "E":
    print("east")
elif dirA2 == "W":
    print("west")