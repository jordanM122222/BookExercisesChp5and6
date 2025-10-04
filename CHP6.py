def absolute_value_one_liner(x):
    return -x if x < 0 else x

def absolute_value_improved(x):
    if x < 0:
        return -x
    else:
        return x


def is_divisible_improved(x, y):
    """
    Checks if x is evenly divisible by y.

    Args:
        x: The number to be divided.
        y: The divisor.

    Returns:
        True if x is divisible by y, False otherwise.
    """
    return x % y == 0

def hypot(leg1, leg2):
    """
    Calculates the length of the hypotenuse of a right triangle.
    """
    return 0.0

# Test the function with placeholder values
print(hypot(3, 4))


def is_between(x, y, z):
    """
    Checks if y is between x and z (inclusive).

    Args:
        x (int/float): The first number.
        y (int/float): The number to check.
        z (int/float): The third number.

    Returns:
        bool: True if y is between x and z, False otherwise.
    """
    return (x <= y <= z) or (z <= y <= x)


# --- Test cases ---

# Case 1: y is between x and z
print(f"Is 5 between 1 and 10? {is_between(1, 5, 10)}")
print(f"Is -3 between -5 and 0? {is_between(-5, -3, 0)}")

# Case 2: y is between z and x
print(f"Is 5 between 10 and 1? {is_between(10, 5, 1)}")
print(f"Is -3 between 0 and -5? {is_between(0, -3, -5)}")

# Case 3: y is equal to one of the endpoints
print(f"Is 1 between 1 and 10? {is_between(1, 1, 10)}")
print(f"Is 10 between 1 and 10? {is_between(1, 10, 10)}")

# Case 4: y is not between x and z
print(f"Is 12 between 1 and 10? {is_between(1, 12, 10)}")
print(f"Is -7 between -5 and 0? {is_between(-5, -7, 0)}")

def ackermann(m, n):
    """
    Evaluates the Ackermann function recursively.

    Args:
        m (int): A non-negative integer.
        n (int): A non-negative integer.

    Returns:
        int: The result of the Ackermann function.
    """
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
    else:
        # This case handles invalid inputs (e.g., negative numbers)
        raise ValueError("Inputs m and n must be non-negative integers.")

def gcd_recursive(a, b):
    """
    Calculates the greatest common divisor (GCD) of two integers recursively.
    """
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

# Test cases
print(f"The GCD of 48 and 18 is: {gcd_recursive(48, 18)}")
print(f"The GCD of 10 and 15 is: {gcd_recursive(10, 15)}")
print(f"The GCD of 7 and 13 is: {gcd_recursive(7, 13)}")
