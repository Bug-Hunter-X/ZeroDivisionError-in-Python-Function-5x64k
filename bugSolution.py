def function_with_uncommon_error(a, b):
    if a == 0:
        return "Division by zero!"  # Handle the error gracefully
    else:
        return a / b