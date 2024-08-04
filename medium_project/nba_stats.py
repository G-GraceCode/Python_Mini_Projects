from requests import get
from pprint import PrettyPrinter

BASE_URL = ""
ALL_JSON = ""

response = get(BASE_URL + ALL_JSON).json()
print(response)