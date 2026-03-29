"""
    Calculates the sum of a variable number of integers.

    Args:
        *args: A sequence of numbers to be added.

    Returns:
        The total sum of the numbers."""

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

# A good practice is to put your runnable code inside this block
if __name__ == "__main__":
    result = add(2, 3, 5)
    print(f"The sum is: {result}")
