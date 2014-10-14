import sys


def concat():
    filename = sys.argv[1]
    file = open(filename, "r")
    content = file.read()
    print(content)
    file.close()

def main():
    return concat()

if __name__ == '__main__':
    main()