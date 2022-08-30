from datetime import datetime


class User:
    def __init__(self, data) -> None:
        self.date_of_birth = data["user_info"]["date_of_birth"]
        self.household_income = data["user_info"]["household_income"]
        self.current_savings_rate = data["user_info"]["current_savings_rate"]
        self.current_retirement_savings = data["user_info"][
            "current_retirement_savings"
        ]
        self.full_name = data["user_info"]["full_name"]
        self.address = data["user_info"]["address"]
        self.pre_retirement_income_percent = data["assumptions"][
            "pre_retirement_income_percent"
        ]
        self.life_expectancy = data["assumptions"]["life_expectancy"]
        self.expected_rate_of_return = data["assumptions"]["expected_rate_of_return"]
        self.retirement_age = data["assumptions"]["retirement_age"]

    def years_until_retirement(self) -> int:
        """Return the number of years remaining until the user's desired
        retirement age, rounded down to the nearest whole number."""

        dob = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        age_in_days = (datetime.today() - dob).days
        age = int(age_in_days / 365.25)

        return self.retirement_age - age
