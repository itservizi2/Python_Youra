'''
Task 1
Create variables that describe the car - model, color, year, number of doors. Place values in them.
Then change the color of the car by assigning a new value to the corresponding variable in the code below.
Display all values. When creating variable names, use appropriate words.

Create variables that will contain people's ages. Also create a variable that will store the number of people.
Calculate and display the average age of a person based on the ages of these five people. If you don’t know
the formula for calculating the arithmetic average, use the Internet to search for information.
When creating variable names, use appropriate words.
'''
# Initial variables
car_model = "Toyota Camry"
car_color = "Red"
car_year = 2020
car_number_of_doors = 4

# Display initial values
print("Initial Car Details:")
print("Model:", car_model)
print("Color:", car_color)
print("Year:", car_year)
print("Number of doors:", car_number_of_doors)

# Change the color of the car
car_color = "Blue"

# Display updated values
print("\nUpdated Car Details:")
print("Model:", car_model)
print("Color:", car_color)
print("Year:", car_year)
print("Number of doors:", car_number_of_doors)

'''
Task 2
Create variables that will contain people's ages. Also create a variable that will store the number of people. 
Calculate and display the average age of a person based on the ages of these five people. 
When creating variable names, use appropriate words.
'''
# Variables containing people's ages
age_person_1 = 25
age_person_2 = 30
age_person_3 = 22
age_person_4 = 28
age_person_5 = 35

# Variable storing the number of people
number_of_people = 5

# Calculate the average age
total_age = age_person_1 + age_person_2 + age_person_3 + age_person_4 + age_person_5
average_age = total_age / number_of_people

# Display the average age
print("\nThe average age of the people is:", average_age)
