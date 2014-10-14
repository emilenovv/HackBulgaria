import sys

def sum_numbers():
    total = 0
    numbers = []
    filename = sys.argv[1]
    file = open(filename, "r")
    content = file.read()
    content = content.split()
    for i in content:
        numbers.append(int(i))
    print(sum(numbers))
    file.close()

def main():
    return sum_numbers()

if __name__ == '__main__':
    main()
