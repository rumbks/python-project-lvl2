import argparse
from gendiff import generate_diff
from gendiff.views import STYLISH


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format", default=STYLISH,
        metavar="FORMAT", help="set format of output"
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
