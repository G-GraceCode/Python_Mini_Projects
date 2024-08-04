from requests import get
from pprint import PrettyPrinter
# import currencyapicom


# Incomplete project the api link needs subscription to get currency rateds

BASE_URL = "https://api.currencyapi.com"
API_KEY = "cur_live_ZcChuTBTz0OHt9O0f84pnIjxHsKJUuYXpLVnvi1S"

# client = currencyapicom.Client(API_KEY)
printer = PrettyPrinter()


def get_currency():
    currency_endpoint = f"/v3/currencies?apikey={API_KEY}"
    url = BASE_URL + currency_endpoint
    data = get(url).json()['data']

    data = list(data.items())
    data.sort()

    return data


def print_currencies(currenies):
    for name, currency in currenies:
        name = currency['name']
        _code = currency["code"]
        symbol = currency.get("symbol", "")
        # get() method helps to get an item from list if it exist else empty ""
        print(f"{_code} - {name} - {symbol}")


def exchange_rate(current1, currency2):
    endpoint = f"/v3/convert?value=12&apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    print(data)
    # if len(data) == 0:
    #     print("Invalide currencies")
    #     return
    # return list(data.values())


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print('invalide amount.')
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount}{currency2}")
    return currency2


def main():
    currencies = get_currency()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

     while True:
          command = input("Enter a command (q to quit): ").lower()

           if command == "q":
                break
            elif command == "list":
                print_currencies(currencies)
            elif command == "convert":
                currency1 = input("Enter a base currency: ").upper()
                amount = input(f"Enter an amount in {currency1}: ")
                currency2 = input("Enter a currency to convert to: ").upper()
                convert(currency1, currency2, amount)
            elif command == "rate":
                currency1 = input("Enter a base currency: ").upper()
                currency2 = input("Enter a currency to convert to: ").upper()
                exchange_rate(currency1, currency2)
            else:
                print("Unrecognized command!")
