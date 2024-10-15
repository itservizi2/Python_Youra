from typing_extensions import Annotated
from pydantic import BaseModel, Field, root_validator


class Triangle(BaseModel):
    side_a: Annotated[float, Field(gt=0)]
    side_b: Annotated[float, Field(gt=0)]
    side_c: Annotated[float, Field(gt=0)]

    @root_validator(pre=True)
    def check_positive(cls, values):
        for side in values:
            if values[side] <= 0:
                raise ValueError(f"{side} must be positive.")
        return values

    @root_validator(pre=True)
    def check_triangle_inequality(cls, values):
        sides = [values.get(f'side_{i}') for i in range(1, 4)]
        if not all(a + b > c for a, b, c in
                   [(sides[0], sides[1], sides[2]), (sides[0], sides[2], sides[1]), (sides[1], sides[2], sides[0])]):
            raise ValueError("The sides do not form a valid triangle.")
        return values


def calculate_triangle_properties():
    while True:
        try:
            triangle = Triangle(
                side_a=float(input("Please enter the length of side a: ")),
                side_b=float(input("Please enter the length of side b: ")),
                side_c=float(input("Please enter the length of side c: "))
            )
            break
        except ValueError as e:
            print(e)

    # Calculate the area and perimeter of the triangle
    s = (triangle.side_a + triangle.side_b + triangle.side_c) / 2
    area = (s * (s - triangle.side_a) * (s - triangle.side_b) * (s - triangle.side_c)) ** 0.5
    perimeter = triangle.side_a + triangle.side_b + triangle.side_c

    print(f"The sides of the triangle are: a = {triangle.side_a}, b = {triangle.side_b}, c = {triangle.side_c}")
    print(f"The area of the triangle is: {area:.2f}")
    print(f"The perimeter of the triangle is: {perimeter:.2f}")


calculate_triangle_properties()
