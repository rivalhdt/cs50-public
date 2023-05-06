from datetime import date
import re
import inflect
import sys

class Seasons:

    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return Seasons(self.value - other.value)

    def __str__(self):
        return f"{self.value}"

def main():
    date = valid_date(input("Date of Birth: "))
    minutes = count(date)
    inflector = inflect.engine()
    words = inflector.number_to_words(int(minutes))
    with_and = f"{words.capitalize()} minutes"
    result = with_and.replace("and ", "")
    print(result)


def valid_date(d):
    try:
        result = re.search(r"(\d+)-(\d+)-(\d+)", d)
        if not result:
            raise ValueError
        else:
            return f"{result.group(1)}-{result.group(2)}-{result.group(3)}"
    except ValueError:
        sys.exit("Invalid date")

def count(d):
    today = date.today()
    now = Seasons(today)

    a = date.fromisoformat(d)
    birth = Seasons(a)

    subs = now-birth
    result = f"{subs}".split(" ")[0]
    return f"{int(result)*60*24}"


if __name__ == "__main__":
    main()