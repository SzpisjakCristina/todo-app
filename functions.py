def get_todos(filepath="todos.txt"):
    """ open the file in read mode
    read to the content that is in the file and create a list with that content """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="todos.txt"):
    """ create a new file, overwrite the existing file
    write that list of user's items """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)