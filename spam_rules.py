import re

def is_suspicious(number):
    """
    Detects suspicious phone numbers based on length, digit patterns, and repetitions.
    """
    # Ensure the number is a string of digits
    if not number.isdigit():
        return True

    # Check number of digits (e.g., only 10-digit numbers allowed)
    if len(number) != 10:
        return True

    # All digits are the same
    if number == number[0] * len(number):
        return True

    # Check for exact sequential or reverse sequential patterns
    sequential_patterns = ['0123456789', '1234567890', '9876543210', '0987654321']
    if number in sequential_patterns:
        return True

    # Check for repeated blocks like 1212121212, 9090909090
    for i in range(1, len(number)//2 + 1):
        block = number[:i]
        if block * (len(number) // len(block)) == number:
            return True

    # Detect mirrored patterns (e.g., 1233211233)
    if number == number[::-1]:
        return True

    # Detect if most digits are same (8 or more same digits)
    for digit in set(number):
        if number.count(digit) >= 5:
            return True

    # Optional: Check if it starts with strange prefixes
    suspicious_prefixes = ['000', '666', '911']
    if any(number.startswith(prefix) for prefix in suspicious_prefixes):
        return True

    return False
