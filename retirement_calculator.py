import requests
from babel.numbers import format_currency

from user import User

ANNUAL_INFLATION_RATE = 0.03
ANNUAL_SALARY_INCREASE = 0.02


def get_user_data(user_id):
    url = "https://pgf7hywzb5.execute-api.us-east-1.amazonaws.com/users"
    resp = requests.get(f"{url}/{user_id}")

    return resp.json()


def calculate(user_data):
    user = User(user_data)

    savings_data = expected_savings_at_retirement(user)
    retirement_savings = savings_data["balance"]
    pre_retirement_income = savings_data["pre_retirement_income"]
    retirement_goal = amount_needed_at_retirement(user, pre_retirement_income)

    print(f"\nTo retire at age {user.retirement_age}:\n")
    print(
        f"You will need {format_currency(retirement_goal, 'USD', locale='en_US', currency_digits=False)}"
    )
    print(
        f"You will have saved {format_currency(retirement_savings, 'USD', locale='en_US', currency_digits=False)}"
    )

    if retirement_goal < retirement_savings:
        return "You're on track, nice job!\n"
    else:
        return "Increase your savings rate to meet your goal!\n"


def amount_needed_at_retirement(user, pre_retirement_income):
    years_in_retirement = user.life_expectancy - user.retirement_age
    annual_withdrawal = pre_retirement_income * user.pre_retirement_income_percent / 100
    print(f"years in retirement: {years_in_retirement}")

    # determine what final withdrawal will be (during last year of life expectancy)
    withdrawal_at_year_37 = annual_withdrawal_after_x_years(
        annual_withdrawal, years_in_retirement - 1
    )
    print(f"withdrawal_at_year_37: {withdrawal_at_year_37}")

    # determine how much you needed in your acc before this year
    bal_needed = withdrawal_at_year_37 / (1 + user.expected_rate_of_return / 100)
    print(f"bal_needed: {bal_needed}")

    # loop it
    total_bal_needed = 0
    for year in reversed(range(years_in_retirement)):
        """looping backwards over range"""
        withdrawal_needed = annual_withdrawal_after_x_years(annual_withdrawal, year)
        total_bal_needed += withdrawal_needed
        roi = total_bal_needed / (1 + user.expected_rate_of_return)
        total_bal_needed -= roi
        print(
            f"year {year}: withdrawal_needed is {int(withdrawal_needed)}, roi is {int(roi)}, bal needed is {int(total_bal_needed)}"
        )

    # total_balance_needed = 0
    # for year in range(0, years_in_retirement):
    #     total_balance_needed += annual_withdrawal
    #     annual_withdrawal *= 1 + ANNUAL_INFLATION_RATE / 100

    return int(total_bal_needed)


def annual_withdrawal_after_x_years(withdrawal_at_year_0, year_of_retirement):
    return withdrawal_at_year_0 * (1 + ANNUAL_INFLATION_RATE) ** year_of_retirement


def expected_savings_at_retirement(user) -> dict:
    savings_balance = user.current_retirement_savings
    income = user.household_income
    for year in range(0, user.years_until_retirement()):
        prev_year_income = round(income, 2)
        roi = savings_balance * (user.expected_rate_of_return) / 100
        savings_balance += income * user.current_savings_rate / 100
        savings_balance += roi
        income *= 1 + ANNUAL_SALARY_INCREASE

    return {
        "balance": int(savings_balance),
        "pre_retirement_income": int(prev_year_income),
    }


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
