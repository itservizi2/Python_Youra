from pydantic import BaseModel, Field, ValidationError
from typing_extensions import Annotated
import math


class Triangle(BaseModel):
    side: Annotated[float, Field(gt=0)]


def validate_triangle(a: float, b: float, c: float) -> None:
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("Invalid triangle: Sides do not satisfy the triangle inequality theorem.")


def calculate_perimeter(a: float, b: float, c: float) -> float:
    return a + b + c


def calculate_area(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


if __name__ == "__main__":
    while True:
        try:
            # Get user input for triangle sides
            a = float(input("Enter the length of side a: "))
            b = float(input("Enter the length of side b: "))
            c = float(input("Enter the length of side c: "))

            # Create Triangle instance using the first side as `side`
            side_a = Triangle(side=a)
            side_b = Triangle(side=b)
            side_c = Triangle(side=c)

            # Validate the triangle inequality theorem
            validate_triangle(side_a.side, side_b.side, side_c.side)

            # Calculate perimeter and area
            perimeter = calculate_perimeter(side_a.side, side_b.side, side_c.side)
            area = calculate_area(side_a.side, side_b.side, side_c.side)

            print(f"Perimeter of the triangle: {perimeter}")
            print(f"Area of the triangle: {area:.2f}")
            break
        except (ValueError, ValidationError) as e:
            print(f"Error: {e}")
