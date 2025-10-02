# ==================================================
#           REVERSE A NUMBER USING MATH
# ==================================================

def reverse_number_math(num):
    """
    Reverses the digits of a number using a mathematical algorithm.
    Correctly handles negative numbers.
    """
    # Handle the sign separately
    sign = -1 if num < 0 else 1
    num = abs(num)

    reversed_num = 0
    while num > 0:
        # 1. Get the last digit
        last_digit = num % 10
        
        # 2. Append this digit to the reversed number
        reversed_num = (reversed_num * 10) + last_digit
        
        # 3. Remove the last digit from the original number
        num = num // 10
        
    return reversed_num * sign

# --- Example ---
original_number = -12345
reversed_num = reverse_number_math(original_number)

print(f"Original Number: {original_number}")
print(f"Reversed Number: {reversed_num}")