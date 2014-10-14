import sys


def cat2():
    for i in range(1, len(sys.argv)):
        filename = sys.argv[i]
        file = open(filename, "r")
        content = file.read()
        print(content)
        print()
        file.close()

def main():
    return cat2()

if __name__ == '__main__':
    main()