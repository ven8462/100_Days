#!/usr/bin/python3

# Write a program that interprets the Body Mass Index (BMI) based on the user's weight and height


height = float(input("Enter your height in m: "))
weight = float(input("Enter your age in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are Underweight")
elif bmi > 18.5 and  bmi > 25:
    print(f"Your BMI is {bmi},you are normal weight")
elif bmi > 25 and bmi < 35:
    print(f"Your BMI is {bmi},you are overweigt")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {bmi},you are obese")
else:
    print(f"Your BMI is {bmi},you are clinically obese")
     


