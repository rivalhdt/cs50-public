def main():
    total_price()

def total_price():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0
    while True:
        try:
            order = input("Menu name: ").title()
            if order in menu:
                total += menu[order]
            if order == "Exit":
                break
        except EOFError:
            break
        else:
            print(f"Total: ${total:.2f}")

main()