import random
# should split get level and number, but just for succinct

def main():
    level_number = get_number_and_level()
    print(guess_number(level_number))

def get_number_and_level():
    while True:
        try:
            level = int(input("Level: "))
            guess_this = random.randint(1, level)
            return guess_this
        except ValueError:
            pass

def guess_number(n):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                raise ValueError
            elif guess == n:
                return "Just right!"
            elif guess < n:
                print("Too small!")
            elif guess > n:
                print("Too large!")
        except ValueError:
            pass
if __name__ == "__main__":
    main()
