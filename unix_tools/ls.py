#! /usr/bin/env python
import argparse
import os


def ls(args, dirname):
    all_list, directories = list(), list()
    for name in os.listdir(dirname):
        if name.startswith("."):
            all_list.append(name)
        else:
            directories.append(name)
    if args.a is True:
        all_list.sort()
        print(".", "..", sep="\n")
        print("\n".join(all_list))
    directories.sort()
    print("\n".join(directories))


def parser_function_ls():
    parser = argparse.ArgumentParser(description="UNIX tool ls, python realization: list the files and directories")
    parser.add_argument("-a", action='store_true', help="Print current, parent and hidden files and directories")
    parser.add_argument('directories', nargs='*', default=['./'], help='enter a directory name')
    args = parser.parse_args()
    return args


def main(args):
    for dirname in args.directories:
        if len(args.directories) != 1:
            print(dirname+":")
        ls(args, dirname)
        print()


if __name__ == "__main__":
    main(parser_function_ls())
