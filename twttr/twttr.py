def main():
    prompt = input("Tweet: ")
    print(shorten(prompt))

def shorten(word):
    result = ""
    for i in word:
        if i not in "AIUEOaiueo":
            result += i
    return result


if __name__ == "__main__":
    main()
