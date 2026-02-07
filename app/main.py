import os


def move_file(command: str) -> None:
    command_in_list = command.split()
    if len(command_in_list) != 3 or command_in_list[0] != "mv":
        return
    source_file = command_in_list[1]
    destination_file = command_in_list[2]
    path = command_in_list[2].split("/")
    for element_of_path in range(len(path)):
        if element_of_path == len(path) - 1 and path[element_of_path]:
            try:
                with (open(source_file, "r") as file_in,
                      open(destination_file, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                return
            os.remove(source_file)
        else:
            if not os.path.isdir("/".join(path[0:element_of_path + 1])):
                os.mkdir("/".join(path[0:element_of_path + 1]))
