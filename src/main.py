import ntgen as nt
import sys


def is_start_id(arg: str) -> bool:
    """Decide arg is some start ID provided by user"""
    try:
        int(arg)
        return True
    except ValueError:
        return False


def is_table_flag(s: str) -> bool:
    """Decide if this is a flag for table generation"""
    if s.__eq__("-t") or s.__eq__("--table"):
        return True
    return False


def is_sep_flag(s: str) -> bool:
    if s.__eq__("-s") or s.__eq__("--sep"):
        return True
    return False


def next_arg(argv: list[str], cursor: int) -> None | str:
    """very simple arg decoding scheme, held together by sticks and spit"""
    if len(argv) > cursor:
        arg = argv[cursor]
        return arg
    return None


global sep_filename


def main():
    """Main method"""
    if len(sys.argv) > 1:
        cursor = 1
        # decode output_file, should always be the first passed arg
        input_file = str(next_arg(sys.argv, cursor))
        cursor += 1
        # initialize default state of optional args
        start_id: int = 1
        gen_table: bool = False
        sep_filename: str | None = None
        output_file = None
        # begin decode args
        while True:
            arg = next_arg(sys.argv, cursor)
            cursor += 1
            if arg is None:
                break
            # begin decodng arg
            if is_start_id(str(arg)):
                start_id = int(arg)
            elif is_table_flag(str(arg)):
                gen_table = True
            elif is_sep_flag(str(arg)):
                sep_filename = str(next_arg(sys.argv, cursor))
                cursor += 1
            else:
                output_file = str(arg)
        nt.ntgen(
            input_file,
            output_file,
            start_id=start_id,
            gen_table=gen_table,
            sep_filename=sep_filename,
        )

    else:
        print(
            "Usage: INPUT-FILE [OUTPUT-FILE] [START-ID] [-t --table] [-s --sep FILENAME]"
        )


if __name__ == "__main__":
    main()
