"""
arithmetic_operations.py

Defines a function perform_operation(num1, num2, operation)
that performs basic arithmetic operations.
"""

from typing import Union

def perform_operation(num1: float, num2: float, operation: str) -> Union[float, str]:
    """
    Perform a basic arithmetic operation.

    Parameters:
        num1 (float): First operand.
        num2 (float): Second operand.
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float | str: Result of the operation, or an error message string
                     (e.g., 'Error: Division by zero' or
                     'Error: Invalid operation').
    """
    try:
        op = operation.strip().lower()
    except Exception:
        return "Error: Invalid operation. Operation must be a string."

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
        return "Error: Invalid operation. Choose add, subtract, multiply, or divide."

