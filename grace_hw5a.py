# File: grace_hw5a.py
# Author: Isaiah Grace
# Date: 2022/3/11
# Lab Section: Tuesday
# Email: isaiah.grace@maine.edu
# Description: checks if second char == second to last char
# Collabs: N/a

# Task A ---
def nameChecker(name) -> bool:
    if len(name) <= 1:
        return False
    return True if name[1] == name[-2] else False

usr_name = input("Enter a name: ")

while(nameChecker(usr_name)):
    print("The second and penultimate chars are the same!")
    usr_name = input("Enter another name? Else enter n: ")

print("Goodbye")

