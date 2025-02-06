# signal_detection.py

def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtracts the second number from the first and returns the result.
    """
    return a - b


# Basic test cases to verify functionality
def run_tests():
    print("Running Tests...")

    # Test addition
    assert add_numbers(5, 3) == 8, "Addition Test Failed"
    
    # Test subtraction
    assert subtract_numbers(5, 3) == 2, "Subtraction Test Failed"
    
    # Test with negative numbers
    assert add_numbers(-2, -4) == -6, "Negative Addition Test Failed"
    assert subtract_numbers(-2, -4) == 2, "Negative Subtraction Test Failed"
    
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
