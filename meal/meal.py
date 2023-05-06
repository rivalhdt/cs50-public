def main():
    prompt = input("Input time: ")
    converted_time = convert(prompt)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
    time = time.replace(":", ".")
    return float(time)


if __name__ == "__main__":
    main()