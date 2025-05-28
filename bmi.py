def calculate_bmi(height, weight):  # Define a function that calculates BMI using height and weight
    bmi = weight / (height ** 2)  # BMI formula: weight divided by height squared
    print("Height = " + str(height) + "m")  # Display the height in meters
    print("Weight = " + str(weight) + "kg")  # Display the weight in kilograms
    print("BMI = " + str(round(bmi, 2)))  # Display the BMI rounded to 2 decimal places
    return bmi  # Return the calculated BMI value to the caller

height = float(input("Enter your height in meters: "))  # Ask user for height, convert input to float
weight = float(input("Enter your weight in kg: "))  # Ask user for weight, convert input to float

bmi = calculate_bmi(height, weight)  # Call the function with user's height and weight and store result in bmi

if bmi < 18.5:  # Check if BMI is less than 18.5
    print("Underweight")  # If true, print that the user is underweight
elif bmi > 25.0:  # Check if BMI is greater than 25.0
    print("Overweight")  # If true, print that the user is overweight
else:  # If BMI is between 18.5 and 25.0
    print("Normal weight")  # Print that the user has a normal weight