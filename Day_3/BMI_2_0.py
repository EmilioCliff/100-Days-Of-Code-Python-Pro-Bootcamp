"""
Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.
"""
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi_no = round(weight / (height**2))
if bmi_no <= 18.5:
    print(f"Your BMI is {bmi_no}, you are underweight")
elif bmi_no > 18.5 and bmi_no <= 25:
    print(f"Your BMI is {bmi_no}, you have a normal weight")
elif bmi_no > 25 and bmi_no <= 30:
    print(f"Your BMI is {bmi_no}, you are slightly overweight")
elif bmi_no > 30 and bmi_no <= 35:
    print(f"Your BMI is {bmi_no}, you are obese")
else:
    print(f"Your BMI is {bmi_no}, you are clinically obese")
