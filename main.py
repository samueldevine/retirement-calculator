import sys
import requests

from retirement_calculator import RetirementCalculator

if len(sys.argv) == 2:
    user_id = sys.argv[1]
else:
    print("User ID not understood. Proceeding with User #9 (default).")
    user_id = 9

url = "https://pgf7hywzb5.execute-api.us-east-1.amazonaws.com/users"
resp = requests.get(f"{url}/{user_id}").json()

calc = RetirementCalculator(resp)
calc.calculate()
