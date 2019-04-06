"""
Project Name: Resistance Calculator
Purpose: To calculate the combined resistance of 2 resistors
Developer Name: Folu Obidare
Email: obidarefolu@gmail.com
"""
# Set up run_again variable
run_again = ""

# Commence while loop
while(run_again.lower() != "e"):

    # Welcome user
    print("Welcome to the resistance calculator")

    # Prompt user to enter values for resistor 1 and resistor 2
    r1 = int(input("Enter the value of Resistor 1: "))
    r2 = int(input("Enter the value of Resistor 2: "))

    # Ask user to select the type of connection the resistors are in
    connection_type = input("Are the resistors connected in...\nA) Parallel\nOR\nB) Series\n")

    # Calculation of total resistance in parallel connection
    if(connection_type.lower() == "a"):
        total_resistance = (r1 * r2) / (r1 +r2)
        total_resistance = round(total_resistance, 1)

        # Display result
        print("The total resistance is", total_resistance)

        # Ask user if it wants to do another calculation
        run_again = input("Do you want to perform another calculation? ENTER = RUN AGAIN. E = EXIT: ")
       
    else:
       # Calculate total resistance in series connection
       total_resistance = r1 + r2

       # Display result
       print("The total resistance is", total_resistance)

       # Ask user if it wants to do another calculation
       run_again = input("Do you want to perform another operation: ENTER = RUN AGAIN. E = EXIT: ") 
 
