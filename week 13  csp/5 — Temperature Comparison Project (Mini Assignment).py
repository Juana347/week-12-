# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temperature = int(input("What is the temperature today?:"))

if temperature > 45 and temperature < 70:
    print("It's warm")
elif temperature > 70 and temperature < 110:
    print("It's hot")
else:
    print("Extreme temperature warning!")

 

