import requests_mock

import main


def test_api_call():
    with requests_mock.Mocker() as mocker:
        user_id = 9
        url = f"https://pgf7hywzb5.execute-api.us-east-1.amazonaws.com/users/{user_id}"
        expected_response = {
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

        mocker.get(url, json=expected_response)
        resp = main.api_call(user_id)

        assert mocker.called_once
        assert resp == expected_response
