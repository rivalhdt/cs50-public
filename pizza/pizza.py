import tabulate
import sys
import csv

def main():
    try:
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        elif ".csv" not in sys.argv[1]:
            sys.exit("Not a CSV file")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            table = []
            with open(f"{sys.argv[1]}") as file:
                read = csv.reader(file)
                for row in read:
                    table.append(row)
            # print(table)
            headers = table[0]
            body = table[1:]
            # print(headers)
            print(tabulate.tabulate(body, headers, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
