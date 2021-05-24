#!/usr/bin/python3


def main(argc, argv):
    if argc != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    print('worked')
        
     
if __name__ == '__main__':
    import sys
    main(len(sys.argv), sys.argv)