import math


def get_valid_input(prompt):
    """
    Gets valid float input from user.

    Args:
        prompt (str): Input prompt message

    Returns:
        float: Valid float input
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_perimeter(a, b, c):
    """
    Calculates the perimeter of a triangle.

    Args:
        a (float): Length of side A
        b (float): Length of side B
        c (float): Length of side C

    Returns:
        float: Perimeter of the triangle
    """
    return a + b + c


def calculate_area(a, b, c):
    """
    Calculates the area of a triangle using Heron's formula.

    Args:
        a (float): Length of side A
        b (float): Length of side B
        c (float): Length of side C

    Returns:
        float: Area of the triangle
    """
    s = calculate_perimeter(a, b, c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def main():
    # Get user input for triangle side lengths
    a = get_valid_input("Enter length of side A: ")
    b = get_valid_input("Enter length of side B: ")
    c = get_valid_input("Enter length of side C: ")

    # Check if the input sides form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        print("Error: The input sides do not form a valid triangle.")
    else:
        # Calculate and display perimeter and area
        perimeter = calculate_perimeter(a, b, c)
        area = calculate_area(a, b, c)
        print(f"Perimeter: {perimeter:.2f}")
        print(f"Area: {area:.2f}")


if __name__ == "__main__":
    main()
