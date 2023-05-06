from validators import email, ValidationFailure

def main():
    print(valid(input("What's your email address? ")))

def valid(s):
    result = email(s)
    if result:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
