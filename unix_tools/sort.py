#! /usr/bin/env python
import argparse


def sort_file(file):
    with open(file) as f:
        file_line = f.read().splitlines()
        file_line.sort()
    return '\n'.join(file_line)


def parser_function_sort():
    parser = argparse.ArgumentParser(description="UNIX tool sort, python realization: sort file lines")
    parser.add_argument('file', help='enter the filename')
    args = parser.parse_args()
    return args


def main():
    args = parser_function_sort()
    print(sort_file(args.file))


if __name__ == "__main__":
    main()
