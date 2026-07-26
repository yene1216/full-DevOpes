from langchain.tools import tool
@tool
def save_notes(note: str) -> str:
    """
    A tool to save important notes.
    this tool can be used to store and retrieve important information for future reference.
    """
    print("SAVE NOTES TOOL CALLED:", note)
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
        
    return f"Note saved: {note}"