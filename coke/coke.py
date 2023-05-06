def main():
    price = 50
    # I think i supposed use total as a list and sum the result, but still green
    total = 0
    while price > 0:
        prompt = int(input("insert: "))
        if prompt == 10 or prompt == 25 or prompt == 5:
            price = change(prompt, price)
            total += prompt
            if total > 50:
                print(total-50)
                break
            elif price == 0:
                print(f"Change owed: {price}")
                break
        print(f"Amount due: {price}")


def change(coin, price):
    return price - coin


main()