import sys


def wc():
    chars = lines = words = 0
    source = open(sys.argv[2], "r")
    for line in source.readlines():
        lines += 1
        words += len(line.split())
        chars += len(line)
    if sys.argv[1] == "chars":
        for line in source.readlines():
            words += len(line.split())
        print(chars)
    elif sys.argv[1] == "words":
        for line in source.readlines():
            words += len(line.split())
        print(words)
    elif sys.argv[1] == "lines":
        for line in source.readlines():
            lines += 1
        print(lines)
    else:
        print("Incorrect command!")
    source.close()

def main():
    return wc()

if __name__ == '__main__':
     main() 