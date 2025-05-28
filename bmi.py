def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    print("Height = " + str(height) + "m")
    print("Weight = " + str(weight) + "kg")
    print("BMI = " + str(bmi))
    return bmi

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))


bmi = calculate_bmi(height, weight)

if bmi < 18.5:
    print("Underweight")
elif bmi > 25.0:
    print("Overweight")
else:
    print("Normal weight")