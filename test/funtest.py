from funlogic import add, sub, mul

def main():
    a, b = 5, 3

    addition = add(a, b)
    subtraction = sub(a, b)
    multiplication = mul(a, b)

    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")

if __name__ == "__main__":
    main()