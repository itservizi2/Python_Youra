from typing_extensions import Annotated


def get_positive_number(prompt: str) -> float:
    while True:
        try:
            num = float(input(prompt))
            if num <= 0:
                print("Please enter a positive number.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a number.")


def is_valid_triangle(a: Annotated[float, "side length"],
                      b: Annotated[float, "side length"],
                      c: Annotated[float, "side length"]) -> bool:
    return a + b > c and a + c > b and b + c > a


def calculate_area(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def calculate_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c


# Prompt user for side lengths
a = get_positive_number("Enter the length of side A: ")
b = get_positive_number("Enter the length of side B: ")
c = get_positive_number("Enter the length of side C: ")

# Check if the input values form a valid triangle
while not is_valid_triangle(a, b, c):
    print("The entered side lengths do not form a valid triangle.")
    a = get_positive_number("Please enter the length of side A again: ")
    b = get_positive_number("Please enter the length of side B again: ")
    c = get_positive_number("Please enter the length of side C again: ")

# Calculate and print area and perimeter
area = calculate_area(a, b, c)
perimeter = calculate_perimeter(a, b, c)

print(f"The area of the triangle is {area:.2f}.")
print(f"The perimeter of the triangle is {perimeter:.2f}.")
