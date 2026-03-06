def get_file_lines(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

