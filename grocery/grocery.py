def main():
    grocery()

def grocery():
    items = []
    while True:
        try:
            items.append(input("").upper())
        except EOFError:
            unix = sorted(list(dict.fromkeys(items)))
            for i in unix:
                print(f"{items.count(i)} {i}")
            break

main()