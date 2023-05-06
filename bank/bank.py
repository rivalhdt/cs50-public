def main():
    word = input("Hello ").lower().strip()
    result = greet(word)
    print(result)

def greet(w):
    if "hello" in w:
        return "$0"
    elif w[0] == "h":
        return "$20"
    else:
        return "$100"

main()