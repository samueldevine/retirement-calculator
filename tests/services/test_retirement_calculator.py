from services.user import User
from services.retirement_calculator import RetirementCalculator


calc = RetirementCalculator(
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


def test_calculator_exists():
    assert type(calc) == RetirementCalculator


def test_calculator_has_attributes():
    assert calc.annual_inflation_rate == 0.03
    assert calc.annual_salary_increase == 0.02
    assert type(calc.user) == User


def test_calculate_saving_enough():
    calc.user.current_savings_rate = 100
    assert calc.calculate() == True


def test_calculate_not_saving_enough():
    calc.user.current_savings_rate = 9
    assert calc.calculate() == False


def test_amount_needed_at_retirement():
    assert calc._amount_needed_at_retirement(50000) == 436552
    assert calc._amount_needed_at_retirement(100000) == 873110
    assert calc._amount_needed_at_retirement(1000000) == 8731143


def test_future_withdrawal():
    assert calc._future_withdrawal(100000, 0) == 100000
    assert calc._future_withdrawal(100000, 5) == 115927
    assert calc._future_withdrawal(100000, 10) == 134391


def test_expected_savings_at_retirement():
    assert calc._expected_savings_at_retirement() == {
        "balance": 521516,
        "pre_retirement_income": 279418,
    }

    calc.user.current_savings_rate = 40
    calc.user.household_income = 60000

    assert calc._expected_savings_at_retirement() == {
        "balance": 609758,
        "pre_retirement_income": 74602,
    }
