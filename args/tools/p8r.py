#!/usr/bin/env python3
import argparse
import re
import subprocess
import sys

PROG8C = ["prog8c", "-quiet", "-vm"]
REGEX = r"^ubyte\[([0-9]+)\]\sargs.buffer="


def add_args(line, input):
    # start with ':' like from READY prompt
    temp = str(ord(":")) + ","
    text = ":".join(input)
    regex = re.search(REGEX, line)
    size = int(regex.group(1))
    result = f"ubyte[{regex.group(1)}] args.buffer="
    temp += ",".join([str(ord(x)) for x in text])
    if len(text) > 1:
        temp += ","
    # take off 2 from length.  ':' at the start and '0' at the end
    temp += ",".join(["00" for filler in range(2, size - len(text))])
    temp += ",0"
    result += temp
    result += " zp=DONTCARE\n"
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("program", help="Program to run.")
    parser.add_argument("input", nargs="*", help="input arguments")
    args = parser.parse_args()

    if not args.program:
        print("P8IR program name required.", file=sys.stderr)
        sys.exit(1)

    # Setup args...
    # Read in IR file
    try:
        with open(args.program, "r") as fileh:
            data = fileh.readlines()
    except Exception as error:
        print(f"Error reading file: {error}")
        sys.exit(1)

    # Write out modified file
    try:
        with open(args.program, "w") as fileh:
            for line in data:
                result = re.search(REGEX, line)
                if result:
                    fileh.write(add_args(line, args.input))
                else:
                    fileh.write(line)
    except Exception as error:
        print(f"Error reading file: {error}")
        sys.exit(1)

    # Run program.
    result = subprocess.run(PROG8C + [args.program])


if __name__ == "__main__":
    main()
