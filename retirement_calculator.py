import requests
from user import User

ANNUAL_INFLATION_RATE = 3
ANNUAL_SALARY_INCREASE = 2


def get_user_data(user_id):
    url = "https://pgf7hywzb5.execute-api.us-east-1.amazonaws.com/users"
    resp = requests.get(f"{url}/{user_id}")

    return resp.json()


def calculate(user_data):
    user = User(user_data)

    retirement_goal = amount_needed_at_retirement(user)
    retirement_savings = expected_savings_at_retirement(user)

    print(f"\nTo retire at age {user.retirement_age}:\n")
    print(f"You will need ${retirement_goal}")
    print(f"You will have saved ${retirement_savings}")

    if retirement_goal < retirement_savings:
        return "You're on track, nice job!\n"
    else:
        return "Increase your savings rate to meet your goal!\n"


def amount_needed_at_retirement(user):
    years_in_retirement = user.life_expectancy - user.retirement_age
    income_at_retirement = future_annual_income(
        user.household_income, user.years_until_retirement()
    )
    annual_withdrawal = income_at_retirement * user.pre_retirement_income_percent / 100
    print(annual_withdrawal)

    # total_balance_needed = 0
    # for year in range(0, years_in_retirement):
    #     total_balance_needed += annual_withdrawal
    #     annual_withdrawal *= 1 + ANNUAL_INFLATION_RATE / 100
    total_balance_needed = annual_withdrawal * 25
    return int(total_balance_needed)


def expected_savings_at_retirement(user):
    savings_balance = user.current_retirement_savings
    income = user.household_income
    for year in range(0, user.years_until_retirement()):
        savings_balance += income * user.current_savings_rate / 100
        savings_balance *= 1 + (user.expected_rate_of_return / 100)
        income *= 1 + (ANNUAL_SALARY_INCREASE / 100)

    return int(savings_balance)


def future_annual_income(income_today, years_from_today):
    return income_today * ((1 + ANNUAL_SALARY_INCREASE / 100) ** years_from_today)


user_9 = {
    "user_info": {
        "date_of_birth": "1975-09-02",
        "household_income": 224726,
        "current_savings_rate": 9,
        "current_retirement_savings": 15518,
        "full_name": "Danny Kane",
        "address": "51495 Smith Crest\nNorth Samanthaview, AL 35953",
    },
    "assumptions": {
        "pre_retirement_income_percent": 67,
        "life_expectancy": 95,
        "expected_rate_of_return": 10,
        "retirement_age": 58,
    },
}

print(calculate(user_9))
