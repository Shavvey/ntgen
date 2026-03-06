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


def ntgen(input_filename: str, output_filename: str | None = None, ids: int = 1):
    nterms = get_terminal_names(collect_lines(get_file_lines(input_filename)))
    if output_filename != None:
        with open(output_filename, "w") as ofile:
            ofile.write("/* Generated from external program, do not modify */\n")
            ofile.write("#ifndef INCLUDE_NTGEN_NTERM_H_\n")
            ofile.write("#define INCLUDE_NTGEN_NTERM_H_\n")
            for nterm in nterms:
                ofile.write(f"#define {nterm.upper()} {ids}\n")
                ids += 1
            ofile.write("#endif  // INCLUDE_NTGEN_NTERM_H_")
    else:
        print("/* Generated from external program, do not modify */\n")
        print("#ifndef INCLUDE_NTGEN_NTERM_H_")
        print("#define INCLUDE_NTGEN_NTERM_H_")
        for nterm in nterms:
            print(f"#define {nterm.upper()} {ids}")
            ids += 1
        print("#endif  // INCLUDE_NTGEN_NTERM_H_")
