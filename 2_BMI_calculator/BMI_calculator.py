"""
Second day learning Python
This program will calculate your BMI calculator
"""
import time

print("Input your height and weight to achieve BMI\n")

height = float(input("Input your height (m): "))
weight = float(input("Input your weight (kg): "))

bmi = weight/(height*height)

# Not create a new line at the end
print("\nCalculating", end="")
for i in range(3):
    time.sleep(0.75)
    print(".", end="", flush=True)

time.sleep(0.75)
print("\n")
print(f"Your BMI is: {round(bmi, 1)}")

# Get the intepretation of the BMI
if (bmi < 18.5):
    print("You are underweight")
elif (bmi < 25):
    print("You have a normal weight")
elif (bmi < 30):
    print("You are over weight")
elif (bmi < 35):
    print("You are obese")
else:
    print("You are clinically obese")

input()
