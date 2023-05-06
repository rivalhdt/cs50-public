import requests
import sys

def main():
    btc()


def btc():
    try:
        if len(sys.argv) == 1:
            sys.exit("Missing command-line argument")
        n = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        btc_usd = response.json()["bpi"]["USD"]["rate"]
        b = btc_usd.replace(",", "")
        c = float(b)
        print(c)
        a = c * n
        print(f"${a:,.4f}")

    except ValueError:
        sys.exit("Command-line argument is not a number")

main()