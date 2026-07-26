
from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """A simple calculator tool that evaluates mathematical expressions."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error evaluating expression: {e}"