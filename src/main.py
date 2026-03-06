import ntgen as nt
import sys


def main():
    INPUT_ARG_POS = 1
    OUTPUT_ARG_POS = 2
    START_ID_ARG_POS = 3
    argc = len(sys.argv)
    if argc > 3:
        nt.ntgen(
            sys.argv[INPUT_ARG_POS],
            sys.argv[OUTPUT_ARG_POS],
            int(sys.argv[START_ID_ARG_POS]),
        )
    elif argc > 2:
        nt.ntgen(sys.argv[INPUT_ARG_POS], sys.argv[OUTPUT_ARG_POS])
    elif argc > 1:
        nt.ntgen(sys.argv[INPUT_ARG_POS])
    else:
        print("Usage: {input-file} [output-file] [start-id]")


if __name__ == "__main__":
    main()
