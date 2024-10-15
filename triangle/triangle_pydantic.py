from pydantic import BaseModel, ValidationError


class Triangle(BaseModel):
    a: float
    b: float
    c: float


def calculate_perimeter(triangle):
    return triangle.a + triangle.b + triangle.c


def calculate_area(triangle):
    import math
    s = (triangle.a + triangle.b + triangle.c) / 2
    return math.sqrt(s * (s - triangle.a) * (s - triangle.b) * (s - triangle.c))


if __name__ == "__main__":
    try:
        # Get user input for triangle sides
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))

        # Validate triangle inequality theorem
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Invalid triangle: Sides do not satisfy the triangle inequality theorem.")

        # Create Triangle instance using Pydantic
        triangle = Triangle(a=a, b=b, c=c)

        # Calculate perimeter and area
        perimeter = calculate_perimeter(triangle)
        area = calculate_area(triangle)

        print(f"Perimeter of the triangle: {perimeter}")
        print(f"Area of the triangle: {area:.2f}")

    except (ValueError, ValidationError) as e:
        print(f"Error: {e}")
