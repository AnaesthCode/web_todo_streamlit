def get_todos(filepath="todo.txt"):
    """Read a text file and return a list of todo items"""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_text_file(todos, filepath="todo.txt"):
    """Save a list of items to the todo list"""
    with open(filepath, "w") as file:
        file.writelines(todos)


# __name__ returns a string that returns main when a certain python file is executed directly
# otherwise it returns the name of the file.

if __name__ == "__main__":
    print("Hello")
    print(get_todos())

