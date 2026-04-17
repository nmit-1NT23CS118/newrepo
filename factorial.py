# Method 1: Using recursion
def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Method 2: Using iteration (more efficient)
def factorial_iterative(n):
    """
    Calculate factorial using iteration.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Method 3: Using Python's built-in math module
import math

def factorial_builtin(n):
    """
    Calculate factorial using Python's math module.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The factorial of n
    """
    return math.factorial(n)


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_numbers = [0, 1, 5, 10, 15]
    
    print("Factorial Calculation Examples:")
    print("-" * 50)
    
    for num in test_numbers:
        print(f"Factorial of {num}:")
        print(f"  Recursive:  {factorial_recursive(num)}")
        print(f"  Iterative:  {factorial_iterative(num)}")
        print(f"  Built-in:   {factorial_builtin(num)}")
        print()