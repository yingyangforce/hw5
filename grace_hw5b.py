# File: grace_hw5b.py
# Author: Isaiah Grace
# Date: 2022/3/11
# Lab Section: Tuesday
# Email: isaiah.grace@maine.edu
# Description: fall distance simulator
# Collabs: N/a

# Task B ---

def distanceFallen(float g, int sec) -> float:
    # distance fallen = 0.5 * g * sec**2
    return 0.5 * g * sec**2

def inputValidate():
    usr_input = input("Enter the acceleration due to gravity: ")
    while usr_input <= 0:
        print("ValError: Please input a positive number")
    return usr_input

usr_g = inputValidate()

sec = 0

fall_dist = distanceFallen(usr_g, sec)

while fall_dist < 100:
    print(f"After {sec} seconds, the object fell {sec} meters.")
    sec += 1
    fall_dist = distanceFallen(usr_g, sec)
    print(f"After {sec} seconds, the object fell {sec} meters.")

