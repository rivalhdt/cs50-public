def main():
    get_adieu()

def get_adieu():
    name = []
    while True:
        try:
            name.append(input("Name: "))
        except EOFError:
            if len(name) == 0:
                break
            elif len(name) == 1:
                print(f"Adieu, adieu, to {name[0]}")
            elif len(name) == 2:
                print(f"Adieu, adieu, to {name[0]} and {name[1]}")
            else:
                print(f"Adieu, adieu, to", end=" ")
                for i in name[:-1]:
                    print(i, end=", ")
                print(f"and {name[-1]}")
            break

main()