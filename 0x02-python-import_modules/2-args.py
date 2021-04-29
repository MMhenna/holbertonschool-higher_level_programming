#!/usr/bin/python3


def main(argv):
    num = len(argv) - 1
    if num <= 0:
        print("{} arguments.".format(num))
    elif num > 0:
        print("{} argument{}:".format(num, "s" if num > 1 else ""))
        for i, arg in enumerate(argv[1:]):
            print("{}: {}".format(i + 1, arg))

if __name__ == '__main__':
    import sys
    main(sys.argv)
