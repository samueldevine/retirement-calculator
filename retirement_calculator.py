from babel.numbers import format_currency

from user import User


class RetirementCalculator:
    def __init__(self, user_data) -> None:
        self.annual_inflation_rate = 0.03  # initialize inflation rate and salary increase as percentages to avoid division by 100 later
        self.annual_salary_increase = 0.02  # initialize inflation rate and salary increase as percentages to avoid division by 100 later

        self.user = User(user_data)

    def calculate(self) -> bool:
        """Returns a boolean value set to True if the user is on track to meet
        their retirement goal, or False if they are not."""

        savings_data = self._expected_savings_at_retirement()
        retirement_savings = savings_data["balance"]
        pre_retirement_income = savings_data["pre_retirement_income"]
        retirement_goal = self._amount_needed_at_retirement(pre_retirement_income)

        print(f"\nTo retire at age {self.user.retirement_age}:\n")
        print(
            f"You will need {format_currency(retirement_goal, 'USD', locale='en_US', currency_digits=False)}"
        )
        print(
            f"You will have saved {format_currency(retirement_savings, 'USD', locale='en_US', currency_digits=False)}"
        )

        if retirement_goal < retirement_savings:
            print("You're on track, nice job!\n")
            return True
        print("Increase your savings rate to meet your goal!\n")
        return False

    def _amount_needed_at_retirement(self, pre_retirement_income) -> int:
        """Returns an integer representing the savings balance needed at the
        user's desired retirement age.

        Keyword args:
        pre_retirement_income (int): the user's expected income during their
            last year of employment"""

        years_in_retirement = self.user.life_expectancy - self.user.retirement_age
        annual_withdrawal = (
            pre_retirement_income * self.user.pre_retirement_income_percent / 100
        )

        total_bal_needed = 0
        for year in reversed(range(years_in_retirement)):
            withdrawal_needed = self._future_withdrawal(annual_withdrawal, year)
            total_bal_needed += withdrawal_needed
            roi = total_bal_needed / (1 + self.user.expected_rate_of_return)
            total_bal_needed -= roi

        return int(total_bal_needed)

    def _future_withdrawal(self, init_withdrawal, year_of_retirement) -> int:
        """Returns an integer representing the withdrawal amount needed in a
        given year of retirement. Accounts for inflation to allow the retiree
        to maintain a similar quality of life.

        Keyword args:
        init_withdrawal (float): total withdrawals in the first year of
            retirement, calculated from pre-retirement income and
            pre-retirement income percentage
        year_of_retirement (int): how many years the user has been retired"""

        return int(
            init_withdrawal * (1 + self.annual_inflation_rate) ** year_of_retirement
        )

    def _expected_savings_at_retirement(self) -> dict:
        """Returns a dictionary with two integer values representing the user's
        total expected savings balance at retirement, and the user's final
        pre-retirement-income after annual salary increases."""

        savings_balance = self.user.current_retirement_savings
        income = self.user.household_income
        for year in range(0, self.user.years_until_retirement()):
            prev_year_income = income
            roi = savings_balance * self.user.expected_rate_of_return / 100
            savings_balance += (income * self.user.current_savings_rate / 100) + roi

            income *= 1 + self.annual_salary_increase

        return {
            "balance": int(savings_balance),
            "pre_retirement_income": int(prev_year_income),
        }
