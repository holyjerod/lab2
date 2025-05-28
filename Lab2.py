def display_main_menu():  # Define a function called display_main_menu
    print("main_menu")  # Print the function name (for debugging or clarity)
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")  # Show user instructions

def get_user_input():  # Define a function to get user input and convert it to a list of numbers
    print("user_input")  # Print the function name

    inputstr = input()  # Read the number sequence entered by the user as a string
    
    strlist = inputstr.split(",")  # Split the string into a list using comma as the separator
    print("After split:", strlist)  # Print the list of strings (for debugging)

    floatlist = []  # Create an empty list to store the numbers as floats
    for eachstr in strlist:  # Loop through each string in the list
        floatlist.append(float(eachstr))  # Convert each string to float and add to floatlist
    print("Data List:", floatlist)  # Print the final list of float numbers
    return floatlist  # Return the list of float numbers to the caller

def calc_average(datalist):  # Define a function to calculate average from a list of numbers
    print("calc_average")  # Print the function name

    total = 0.0  # Start with a total of 0.0 (float value)
    for eachData in datalist:  # Loop through each number in the list
        total = total + eachData  # Add the number to the total

    # Alternatively, we could write: total = sum(datalist)
    average = total / len(datalist)  # Calculate average by dividing total by number of items
    print("Average = ", average)  # Print the calculated average
    return average  # Return the average to the caller

def find_min_max(datalist):  # Define a function to find the minimum and maximum values
    print("find_min_max")  # Print the function name

    floatlist = datalist.copy()  # Make a copy of the list to avoid changing the original
    floatlist.sort()  # Sort the copied list from smallest to largest
    print("MIN = ", floatlist[0])  # Print the first item (minimum)
    print("MAX = ", floatlist[-1])  # Print the last item (maximum)
    return (floatlist[0], floatlist[-1])  # Return both min and max as a tuple

def sort_temperature():  # Define a placeholder function (not implemented yet)
    print("sort_temperature")  # Print the function name

def calc_median_temperature():  # Define another placeholder function (not implemented yet)
    print("calc_median_temperature")  # Print the function name

def main():  # Define the main function where the program starts running
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python") # Print the title of the lab
    print("*ET0735 Lab 2 Ex3")  # Print a label to show this is Exercise 3
    display_main_menu()  # Call the function to display the menu and instructions
    resultlist = get_user_input()  # Call the function to get and process user input

    avg = calc_average(resultlist)  # Call the average function and store the result
    print("* Average is ", avg)  # Print the average value

    minimum, maximum = find_min_max(resultlist)  # Call the min/max function and get both values
    print("* Minimum is ", minimum)  # Print the minimum value
    print("* Maximum is ", maximum)  # Print the maximum value

    print("* End of program")  # Indicate that the program has ended

if __name__ == "__main__":  # Correct way to check if script is being run directly
    main()
