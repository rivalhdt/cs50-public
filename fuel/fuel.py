def main():
    print(fraction())


def fraction():
    while True:
        try:
            f = input("Fraction: ")
            x, y = f.split("/")
            result = round(int(x)/int(y)*100)
            if result > 100:
                raise ValueError
            elif result > 98:
                return "F"
            elif result < 2:
                return "E"
            else:
                return f"{result}%"
        except ZeroDivisionError:
            pass
        except ValueError:
            pass

main()