def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("BMI = " + str(round(bmi, 2)))
    return bmi

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))


bmi = calculate_bmi(height, weight)

if bmi < 18.5:def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("BMI = " + str(round(bmi, 2)))
    return bmi
def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("BMI = " + str(round(bmi, 2)))
    return bmi


height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

if bmi < 18.5:
    print("under weight")
elif bmi > 25.0:
    print("over weight")
else:
   print("normal weight")

calculate_bmi(height, weight)

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

if bmi < 18.5:
    print("under weight")
elif bmi > 25.0:
    print("over weight")
else:
   print("normal weight")

calculate_bmi(height, weight)
    print("Underweight")
elif bmi > 25.0:
    print("Overweight")
else:
    print("Normal weight")

