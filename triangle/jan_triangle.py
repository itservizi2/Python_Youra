from typing_extensions import Annotated
from math import sqrt


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


def is_valid_triangle(a: Annotated[float, "side length"], b: Annotated[float, "side length"],
                      c: Annotated[float, "side length"]) -> bool:
    return a + b > c and a + c > b and b + c > a


def calculate_area(a: Annotated[float, "side length"], b: Annotated[float, "side length"],
                   c: Annotated[float, "side length"]) -> float:
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))


def calculate_perimeter(a: Annotated[float, "side length"], b: Annotated[float, "side length"],
                        c: Annotated[float, "side length"]) -> float:
    return a + b + c


# Prompt user for side lengths
side1 = get_positive_number("Enter the first side length: ")
side2 = get_positive_number("Enter the second side length: ")
side3 = get_positive_number("Enter the third side length: ")

# Validate triangle sides
while not is_valid_triangle(side1, side2, side3):
    print("The given sides do not form a valid triangle. Please enter new side lengths.")
    side1 = get_positive_number("Enter the first side length: ")
    side2 = get_positive_number("Enter the second side length: ")
    side3 = get_positive_number("Enter the third side length: ")

# Calculate and print area and perimeter
area = calculate_area(side1, side2, side3)
perimeter = calculate_perimeter(side1, side2, side3)

print(f"The area of the triangle is {area:.2f}")
print(f"The perimeter of the triangle is {perimeter:.2f}")
