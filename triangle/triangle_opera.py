from pydantic import BaseModel, Field, ValidationError
from typing_extensions import Annotated


class Triangle(BaseModel):
    side_a: Annotated[float, Field(gt=0, description="Length of side A (must be positive)")]
    side_b: Annotated[float, Field(gt=0, description="Length of side B (must be positive)")]
    side_c: Annotated[float, Field(gt=0, description="Length of side C (must be positive)")]

    def validate_sides(self):
        if not (self.side_a + self.side_b > self.side_c and
                self.side_a + self.side_c > self.side_b and
                self.side_b + self.side_c > self.side_a):
            raise ValueError("The lengths do not satisfy the triangle inequality theorem.")

    def area(self):
        # Using Heron's formula
        s = (self.side_a + self.side_b + self.side_c) / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("The value must be positive.")
            return value
        except ValueError as e:
            print(e)


def main():
    print("Enter the lengths of the sides of the triangle:")

    while True:
        try:
            a = get_positive_float("Side A: ")
            b = get_positive_float("Side B: ")
            c = get_positive_float("Side C: ")

            triangle = Triangle(side_a=a, side_b=b, side_c=c)
            triangle.validate_sides()
            break  # Exit the loop if everything is valid
        except (ValidationError, ValueError) as e:
            print(e)

    print(f"Area of the triangle: {triangle.area():.2f}")
    print(f"Perimeter of the triangle: {triangle.perimeter():.2f}")


if __name__ == "__main__":
    main()
