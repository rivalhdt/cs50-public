def main():
    prompt = input("to camel:  ")
    camel(prompt)

def camel(w):
    result = ""
    for i in w:
        if i.isupper():
            result += "_"
            result += i.lower()
        else:
            result += i
    print(result)

main()