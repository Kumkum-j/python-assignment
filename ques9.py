#9. Multiple Except Blocks

try:
    # Some code that may raise exceptions
    result = 10 / 0
    print(undefined_variable)
except (ZeroDivisionError, NameError, TypeError) as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
