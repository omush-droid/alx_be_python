def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation.

    Parameters:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float | str: Result of the operation, or an error message string
                     if invalid or division by zero.
    """
    try:
        op = operation.strip().lower()
    except Exception:
        return "Error: Invalid operation"

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
