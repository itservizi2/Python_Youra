class Triangle:
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.validate_positive(side_a, "Side A")
        self.validate_positive(side_b, "Side B")
        self.validate_positive(side_c, "Side C")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @staticmethod
    def validate_positive(value, name):
        if value <= 0:
            raise ValueError(f"{name} must be positive")

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

            triangle = Triangle(a, b, c)
            triangle.validate_sides()
            break  # Exit the loop if everything is valid
        except ValueError as e:
            print(e)

    print(f"Area of the triangle: {triangle.area():.2f}")
    print(f"Perimeter of the triangle: {triangle.perimeter():.2f}")


if __name__ == "__main__":
    main()
