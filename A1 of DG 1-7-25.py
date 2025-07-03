# ---------------------------------------------------------
# Python Program Collection
# Author: Dr Samit Kumar Singh
# AICTE ID : 1-1127758109
# Description: This script contains the following 4 programs:
# 1. Find the greatest of three numbers and check even/odd.
# 2. Check if a given year is a leap year.
# 3. Simulate traffic light behavior based on input.
# 4. Grade classification based on marks.
# ---------------------------------------------------------

# -------------------------------
# Program 1: Greatest of Three Numbers & Even/Odd Check
# -------------------------------

print("Program 1: Find Greatest of Three Numbers & Check Even/Odd")
print("-----------------------------------------------------------")

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Finding the greatest number
if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

print("Greatest number is:", greatest)

# Check whether the greatest number is even or odd
if greatest % 2 == 0:
    print("The greatest number is Even.")
else:
    print("The greatest number is Odd.")

print("\n")  # Line break between programs

# -------------------------------
# Program 2: Leap Year Checker
# -------------------------------

print("Program 2: Check if Year is Leap Year")
print("--------------------------------------")

# Taking year as input from user
year = int(input("Enter a year: "))

# Checking conditions for leap year
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")

print("\n")  # Line break between programs

# -------------------------------
# Program 3: Traffic Light Simulation
# -------------------------------

print("Program 3: Traffic Light Simulation")
print("-----------------------------------")

# Asking user to enter traffic light color
light = input("Enter traffic light color (Red/Yellow/Green): ").lower()

# Simulating traffic behavior based on color
if light == "red":
    print("Signal: RED - Stop! 🚦")
elif light == "yellow":
    print("Signal: YELLOW - Wait! ⚠️")
elif light == "green":
    print("Signal: GREEN - Go! ✅")
else:
    print("Invalid input! Please enter Red, Yellow, or Green.")

print("\n")  # Line break between programs

# -------------------------------
# Program 4: Grade Classification Based on Marks
# -------------------------------

print("Program 4: Grade Classification Based on Marks")
print("----------------------------------------------")

# Taking marks as input
marks = int(input("Enter marks (out of 100): "))

# Grading logic
if marks > 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 50:
    print("Grade: E")
else:
    print("Result: Fail")

# -------------------------------
# End of Program Collection
# -------------------------------