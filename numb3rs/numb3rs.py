import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    result = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if result and int(result.group(1)) < 256 and int(result.group(2)) < 256 and int(result.group(3)) < 256 and int(result.group(4)) < 256:
        return True
    else:
        return False

if __name__ == "__main__":
    main()