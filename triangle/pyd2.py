# using python programming language and Pydantic library version 2 write code that calculates the area and perimeter  of a triangle under the following conditions:
# do not use decorators and lambda
# 1. user must be prompted to input the side length from the keyboard
# 2. side length must be always positive and should be checked for being positive when inserted by user
# 3. The rule of the sides of a triangle must be used for checking if the lengths correspond to condition
# 4. the Pydantic library version 2 for Python should be used for validation of side length
# 5. in case user input is incorrect loop the iteration until user inserts correct value
# 6. do not use @decorator in Pydantic, use Field
# 7.  from typing_extensions import Annotated
# 8. create a class Triangle that should have the generic variable side and afterwards when creating the object triangle
# the validation should compare the a, b and c sides length with variable side

from typing_extensions import Annotated
from pydantic import BaseModel, Field, ValidationError


class Triangle(BaseModel):
    side: Annotated[float, Field(gt=0)]


def calculate_triangle_area_and_perimeter(a, b, c):
    """Calculates the area and perimeter of a triangle given its side lengths.

    Args:
        a, b, c: Side lengths of the triangle.

    Returns:
        Tuple containing the area and perimeter of the triangle.
    """

    # Check if the triangle inequality holds
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid side lengths: The triangle inequality does not hold.")

    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    # Calculate the perimeter
    perimeter = a + b + c

    return area, perimeter


while True:
    try:
        a = float(input("Enter side length a: "))
        b = float(input("Enter side length b: "))
        c = float(input("Enter side length c: "))

        # Create a Triangle object to validate side lengths
        triangle = Triangle(side=a)
        triangle = Triangle(side=b)
        triangle = Triangle(side=c)

        # Calculate the area and perimeter
        area, perimeter = calculate_triangle_area_and_perimeter(a, b, c)

        print("Area:", area)
        print("Perimeter:", perimeter)
        break
    except ValidationError as e:
        print(f"Invalid side length: {e}")
