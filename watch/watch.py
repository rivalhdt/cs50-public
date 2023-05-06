import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    result = re.search(r'^<iframe.+youtube.com\/embed\/(\w+)', s)
    if result:
        return f"https://youtu.be/{result.group(1)}"

if __name__ == "__main__":
    main()