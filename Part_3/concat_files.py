import sys


def concat_files():
    output = open("MEGATRON.txt", "a")
    for i in range(1, len(sys.argv)):
        source = open(sys.argv[i], "r")
        for line in source.readlines():
            output.write(line)
        source.close()
        output.write("\n")
    output.close()


def main():
    return concat_files()


if __name__ == '__main__':
    main()