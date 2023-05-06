def main():
    f = input("Fraction: ")
    converted = convert(f)
    print(gauge(converted))


def convert(fraction):
        x, y = fraction.split("/")
        if y == "0":
            raise ZeroDivisionError
        if x > y:
            raise ValueError

        return round(int(x)/int(y)*100)


def gauge(percentage):
    try:
        if percentage > 100:
            raise ValueError
        elif percentage > 98:
            return "F"
        elif percentage < 2:
            return "E"
        else:
            return f"{percentage}%"
    except ValueError:
        main()


if __name__ == "__main__":
    main()