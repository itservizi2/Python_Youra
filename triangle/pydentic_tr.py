from math import sqrt

from typing_extensions import Annotated
from pydantic import BaseModel, Field, validator


# Define a Pydantic model for the triangle sides
class TriangleSides(BaseModel):
    side1: Annotated[float, Field(gt=0)]
    side2: Annotated[float, Field(gt=0)]
    side3: Annotated[float, Field(gt=0)]

    @validator('*', pre=True)
    def check_positive(cls, v):
        if v <= 0:
            raise ValueError("Side length must be positive")
        return v

    @validator('side1', 'side2', 'side3')
    def check_triangle_inequality(cls, v, values, **kwargs):
        if not cls.is_valid_triangle(values['side1'], values['side2'], values['side3']):
            raise ValueError("The given sides do not form a valid triangle")
        return v

    @staticmethod
    def is_valid_triangle(a: float, b: float, c: float) -> bool:
        return a + b > c and a + c > b and b + c > a


# Function to get valid side lengths from the user
def get_valid_sides() -> TriangleSides:
    while True:
        try:
            side1 = float(input("Enter the first side length: "))
            side2 = float(input("Enter the second side length: "))
            side3 = float(input("Enter the third side length: "))
            sides = TriangleSides(side1=side1, side2=side2, side3=side3)
            return sides
        except ValueError as e:
            print(f"Invalid input: {e}")


# Prompt user for valid side lengths
sides = get_valid_sides()

# Calculate perimeter and area
perimeter = sides.side1 + sides.side2 + sides.side3
s = perimeter / 2
area = sqrt(s * (s - sides.side1) * (s - sides.side2) * (s - sides.side3))

# Print the results
print(f"The area of the triangle is {area:.2f}")
print(f"The perimeter of the triangle is {perimeter:.2f}")
