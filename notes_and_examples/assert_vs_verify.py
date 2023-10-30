# Assert example
def test_assert(expected, actual):
    assert expected == actual, f"Assertion failed: Expected '{expected}' but got '{actual}'"
    print("Assertion passed. Test continues...")

# Verify-like behavior using try-except
def test_verify(expected, actual):
    try:
        if expected != actual:
            raise AssertionError(f"Verification failed: Expected '{expected}' but got '{actual}'")
        print("Verification passed. Test continues...")
    except AssertionError as e:
        print(e)
        # Test can continue despite the failure

# Test cases
test_assert(5, 5)  # This assertion will pass
test_assert(5, 6)  # This assertion will fail

test_verify(10, 10)  # This verification will pass
test_verify(10, 11)  # This verification will fail, but the test will continue


"""

This code includes two functions: test_assert and test_verify.

test_assert uses the assert statement to perform an assertion. 

If the assertion fails, it raises an AssertionError and stops the execution immediately.

test_verify demonstrates a "verify"-like behavior using a try-except block. 

It checks a condition and, if the condition is not met, raises an AssertionError. 
However, it catches the error using the except block and allows the test to continue running.

"""