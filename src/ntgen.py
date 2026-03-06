import re


def get_file_lines(filename: str) -> list[str]:
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines


def collect_lines(lines: list[str]) -> str:
    sb = ""
    for line in lines:
        sb += line
    return sb


def get_terminal_names(file_content: str) -> list[str]:
    matches = re.findall(r"\n+[a-z_]+\s*:\s*", file_content)
    sanitized_matches = []
    for match in matches:
        sanitized_match = str(match).replace("\n", "")
        idx = sanitized_match.find(":")
        sanitized_matches.append(sanitized_match[:idx])
    return sanitized_matches


def ntgen(filename: str) -> list[str]:
    return get_terminal_names(collect_lines(get_file_lines(filename)))
