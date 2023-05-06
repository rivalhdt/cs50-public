import random


def main():
    a = get_level()
    generate_integer(a)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    score = 0
    while True:
        try:
            for _ in range(10):
                if level == 1:
                    x = random.randint(0,9)
                    y = random.randint(0,9)
                elif level == 2:
                    x = random.randint(10,99)
                    y = random.randint(10,99)
                elif level == 3:
                    x = random.randint(100,999)
                    y = random.randint(100,999)
                z = x + y
                count = 0
                while True:
                    if count == 3:
                        print(f"{x} + {y} = {z}")
                        break
                    answer = int(input(f"{x} + {y} = "))
                    if z == answer:
                        score += 1
                        break
                    elif answer != z and count < 3:
                        count += 1
                        print("EEE")




            print(f"Scrore: {score}")
            break
        except ValueError:
            print("EEE")


if __name__ == "__main__":
    main()