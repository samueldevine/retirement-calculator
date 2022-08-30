from datetime import datetime
from services.user import User


user = User(
    {
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
)


def test_user_exists():
    assert type(user) == User


def test_user_has_attributes():
    assert user.date_of_birth == "1975-09-02"
    assert user.household_income == 224726
    assert user.current_savings_rate == 9
    assert user.current_retirement_savings == 15518
    assert user.full_name == "Danny Kane"
    assert user.address == "51495 Smith Crest\nNorth Samanthaview, AL 35953"
    assert user.pre_retirement_income_percent == 67
    assert user.life_expectancy == 95
    assert user.expected_rate_of_return == 10
    assert user.retirement_age == 58


def test_years_until_retirement():
    dob = datetime.strptime(user.date_of_birth, "%Y-%m-%d")
    assert dob == datetime(1975, 9, 2, 0, 0)

    age = int((datetime.today() - dob).days / 365.25)
    assert user.years_until_retirement() == user.retirement_age - age
