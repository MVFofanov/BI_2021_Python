#! /usr/bin/env python

import argparse
import os


def parser_function_wc():
    parser = argparse.ArgumentParser(description="UNIX tool wc, python realization: count lines, words and bytes")
    parser.add_argument("-l", action='store_true',
                        help="The lines number from input file will be printed")
    parser.add_argument("-w", action='store_true',
                        help="The words number from input file will be printed")
    parser.add_argument("-c", action='store_true',
                        help="The bytes number from input file will be printed")
    parser.add_argument('file', help='enter the filename')
    args, _ = parser.parse_known_args()
    return args


def count_lines(file):
    with open(file) as f:
        return len(f.readlines())


def count_words(file):
    with open(file) as f:
        return len(f.read().split())


def count_bytes(file):
    return os.path.getsize(file)


def main(args):
    args = parser_function_wc()
    input_file = args.file
    if args.l is True:
        print(f'{count_lines(input_file)} {input_file}')
    if args.w is True:
        print(f'{count_words(input_file)} {input_file}')
    if args.c is True:
        print(f'{count_bytes(input_file)} {input_file}')


if __name__ == "__main__":
    main(parser_function_wc())
