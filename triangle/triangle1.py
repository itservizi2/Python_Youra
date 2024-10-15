from pydantic import BaseModel, Field
from typing_extensions import Annotated


class TriangleSide(BaseModel):
    length: Annotated[float, Field(gt=0)]


# Get side lengths from the user repeatedly until valid
while True:
    try:
        side1 = float(input("Enter side 1 length: "))
        side2 = float(input("Enter side 2 length: "))
        side3 = float(input("Enter side 3 length: "))

        # Use Pydantic to validate side lengths
        triangle_sides = TriangleSide(length=side1), TriangleSide(length=side2), TriangleSide(length=side3)

        # Check triangle inequality theorem
        if (
                side1 + side2 > side3
                and side1 + side3 > side2
                and side2 + side3 > side1
        ):
            break
        else:
            print("Invalid triangle sides. Try again.")

    except ValueError as e:
        print(f"Invalid input: {e}")

# Calculate area and perimeter
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
perimeter = side1 + side2 + side3

print(f"Area of the triangle: {area:.2f}")
print(f"Perimeter of the triangle: {perimeter:.2f}")
