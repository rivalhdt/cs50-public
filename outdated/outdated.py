def main():
    print(outdated())

def outdated():
    month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            date = input("Date: ").strip()
            if date[0].isalpha():
                if "," not in date:
                    raise ValueError
                else:
                    a = date.split()
                    m = month.index(a[0])+1
                    d = a[1].strip(",")
                    y = a[2]
            else:
                a = date.replace("/", " ").split()
                m = a[0]
                d = a[1].strip(",")
                y = a[2]
            if int(d) > 31 or int(m) > 12:
                raise ValueError
        except ValueError:
            pass
        else:
            return f"{y}-{str(m).zfill(2)}-{str(d).zfill(2)}"

main()