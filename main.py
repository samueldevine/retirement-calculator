import sys
import requests

from services.retirement_calculator import RetirementCalculator

if len(sys.argv) == 2:
    user_id = sys.argv[1]
else:
    print("User ID not understood. Proceeding with User #9 (default).")
    user_id = 9


def api_call(user_id):
    url = "https://pgf7hywzb5.execute-api.us-east-1.amazonaws.com/users"
    r = requests.get(f"{url}/{user_id}")
    return r.json()


resp = api_call(user_id)
calc = RetirementCalculator(resp)
calc.calculate()
