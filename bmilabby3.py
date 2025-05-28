def calculate_bmi(height, weight):          # Define function that takes height/weight as input
    bmi = weight / (height ** 2)           # Calculate BMI: weight ÷ (height squared)
    
    print("Height = " + str(height) + "m")  # Display height with 'm' unit
    print("Weight = " + str(weight) + "kg") # Display weight with 'kg' unit
    print("BMI = " + str(round(bmi, 2)))   # Show BMI rounded to 2 decimal places
    
    if bmi < 18.5:                         # If BMI is below 18.5...
        return -1                           # → Return code for Underweight
    elif 18.5 <= bmi <= 25.0:               # If BMI is between 18.5-25.0...
        return 0                            # → Return code for Normal weight
    else:                                   # If BMI is above 25.0...
        return 1                            # → Return code for Overweight
