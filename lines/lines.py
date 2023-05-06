import sys


def main():
    lines = count_lines()
    strip = strip_lines(lines)
    print(len(strip))


def count_lines():
    try:
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        elif ".py" not in sys.argv[1]:
            sys.exit("Not a Python file")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            with open(f"{sys.argv[1]}") as file:
                file = file.readlines()
            return file

    except FileNotFoundError:
        sys.exit("File does not exist")

def strip_lines(a):
    result = []
    for i in a:
        i = i.strip()
        if i == "":
            pass
        elif i[0] == "#":
            pass
        else:
            result.append(i)
    return result

if __name__ == "__main__":
    main()
