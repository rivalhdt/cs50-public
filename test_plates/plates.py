def main():
    prompt = input("Plate: ")
    if is_valid(prompt):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alpha = ""
    number = ""
    for i in s:
        if i.isnumeric():
            number += i
        else:
            alpha += i
    if number == "":
        a = True
    else:
        a = number[0] != "0"

    return (len(alpha) > 1) and (1 < len(s) < 7) and (alpha+number == s) and a and (s.isalnum())


if __name__ == "__main__":
    main()