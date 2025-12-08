import sys


def get_file_data() -> str:
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} <input file")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        return f.read()
