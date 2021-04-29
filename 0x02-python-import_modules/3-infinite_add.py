#!/usr/bin/python3


def main(argv):
    nums = len(argv) - 1
    if nums <= 0:
        print("{}".format(nums))
    elif nums > 0:
        add = 0
        for i in argv[1:]:
            add = add + int(i)
        print("{}".format(add))

if __name__ == '__main__':
    import sys
    main(sys.argv)
