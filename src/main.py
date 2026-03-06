import ntgen as nt
import sys


def main():
    argc = len(sys.argv)
    if argc > 1:
        lines = nt.get_file_lines(sys.argv[1])
        file_content = nt.collect_lines(lines)
        nterms = nt.get_terminal_names(file_content)
        print(nterms)


if __name__ == "__main__":
    main()
