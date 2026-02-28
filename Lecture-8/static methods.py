class MathUtilities:
    @staticmethod
    def add(x, y):
        """Performs addition of two numbers."""
        return x + y

# Calling the static method using the class name
result = MathUtilities.add(5, 10)
print(f"The sum is: {result}")
# Output: The sum is: 15
