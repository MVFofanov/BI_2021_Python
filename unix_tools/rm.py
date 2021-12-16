#! /usr/bin/env python
import argparse
import os
import shutil


def parser_function_rm():
    parser = argparse.ArgumentParser(description="UNIX tool rm, python realization: remove file or directory")
    parser.add_argument("-r", action='store_true',
                        help="remove a directory with its subdirectories and nested files")
    parser.add_argument('input_names', nargs='+', help='enter names of files or directories')
    args = parser.parse_args()
    return args


def main(args):
    for name in args.input_names:
        if os.path.isfile(name) is True:
            os.remove(name)
        else:
            if args.r is True:
                shutil.rmtree(name)
            else:
                print(f"rm: {name}: is a directory")


if __name__ == "__main__":
    main(parser_function_rm())
