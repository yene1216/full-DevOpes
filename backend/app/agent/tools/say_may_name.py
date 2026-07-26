from langchain.tools import tool


@tool
def say_my_name(input_text:str) -> str:
    """
    A tool to return the developer's name.
    This tool can be used to greet the user by their name.
    """
    return "your name is yenesew"