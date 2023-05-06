def main():
    prompt = input("What is the answer of the Great Question of Life, the Universe, and Everything? ").lower().strip()
    print(deep(prompt))

def deep(w):
    match w:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"

main()