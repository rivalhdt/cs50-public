import sys
import csv

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif ".csv" not in sys.argv[1]:
            sys.exit("File not CSV")
        else:
            table = []
            with open(f"{sys.argv[1]}") as file:
                read = csv.DictReader(file)
                for i in read:
                    table.append(i)

            with open(f"{sys.argv[2]}", "w") as file:
                write = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                write.writeheader()
                for i in table:
                    write.writerow({"first":i["name"].split(",")[1].strip(), "last":i["name"].split(",")[0], "house":i["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()