import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        search = re.search(r"^([0-9]+):?([0-9]+)? (.M) to ([0-9]+):?([0-9]+)? (.M)", s)
        f = search.group(1)
        fm = search.group(2)
        m = search.group(3)
        t = search.group(4)
        tm = search.group(5)
        m2 = search.group(6)

        if len(f) == 1:
            f = f"0{f}"
        if int(f) > 12:
            raise ValueError


        if not fm:
            fm = f"00"
        if int(fm) >= 60:
            raise ValueError

        if len(t) == 1:
            t = f"0{t}"
        if int(t) > 12:
            raise ValueError

        if not tm:
            tm = f"00"
        if int(tm) >= 60:
            raise ValueError

        if m == "PM" and f != "12":
            f = f"{int(f)+12}"
        if m2 == "PM" and t != "12":
            t = f"{int(t)+12}"

        if m == "AM" and f == "12":
            f = f"00"
        if m2 == "AM" and t == "12":
            t = f"00"



        return f"{f}:{fm} to {t}:{tm}"
    except:
        raise ValueError



if __name__ == "__main__":
    main()