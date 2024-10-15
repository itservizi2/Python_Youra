from typing import Annotated


def get_positive_input(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a


def calculate_area_and_perimeter(a: float, b: float, c: float) -> Annotated[float, "Area of the triangle"]:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def calculate_perimeter(a: float, b: float, c: float) -> Annotated[float, "Perimeter of the triangle"]:
    return a + b + c


if __name__ == "__main__":
    while True:
        try:
            side1 = get_positive_input("Enter the length of side 1: ")
            side2 = get_positive_input("Enter the length of side 2: ")
            side3 = get_positive_input("Enter the length of side 3: ")

            if is_valid_triangle(side1, side2, side3):
                area = calculate_area_and_perimeter(side1, side2, side3)
                perimeter = calculate_perimeter(side1, side2, side3)
                print(f"Area: {area:.2f}")
                print(f"Perimeter: {perimeter:.2f}")
                break
            else:
                print("The sides do not form a valid triangle. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")
