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


# very simple arg decoding scheme, held together by sticks and spit
def next_arg(argv: list[str], cursor: int) -> None | str:
    if len(argv) > cursor:
        arg = argv[cursor]
        return arg
    return None


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
            else:
                output_file = str(arg)
        nt.ntgen(input_file, output_file, start_id=start_id, gen_table=gen_table)

    else:
        print("Usage: INPUT-FILE [OUTPUT-FILE] [START-ID] [-t --table]")


if __name__ == "__main__":
    main()
