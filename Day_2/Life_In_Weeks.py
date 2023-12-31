"""
Instructions
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
"""
age = input("What is your current age? ")
remaining_years = 90 - int(age)
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365
print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")


