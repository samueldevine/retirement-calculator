# Retirement Calculator

_This is a coding exercise for an interview, not real financial advice!_

Retirement Calculator is a small python script that calls an API endpoint to generate some random user data, and then calculates how much money that user will have saved by the time they retire, and how much they'll actually need in their account to maintain their current standard of living until the end of their life expectancy.

I spent about 4 hours total on this project over two days. With limited time to work on it, I focused on creating clean, readable code to satisfy the basic requirements, added a few unit tests for peace of mind, then refactored the code and file structure slightly to polish everything up.

Given more time, I'd love to add functionality that allows users to enter their own data, either via command line prompts, a web-based frontend, or even an API endpoint. I'd also like to spend more time expanding the test coverage and searching for edge cases.

## Getting started

I made minimal use of three external libraries:
- [babel](https://babel.pocoo.org/en/latest/api/numbers.html) to quickly format currencies
- [requests](https://requests.readthedocs.io/en/latest/) to easily call the api endpoint
- [requests-mock](https://requests-mock.readthedocs.io/en/latest/) to mock api calls during testing

To install them with pip, simply run:

```bash
$pip3 install -r requirements.txt
```
You may wish to set up a virtual environment before doing this, but I won't go into the details of that here.

Before running the script, you'll need to select a user id. There are an
infinite number of users available, any number you choose will generate a
random unique user. Once you've chosen a number, head to your command line and
run the following command, replacing `{user_id}` with the id of your choice:

```bash
$python3 main.py {user_id}
```

If you don't choose a user id, or if you enter too many commands, the calculator will choose `9` as a default.

## Output

When running, the script will write the results of the calculations to the console. Different users will produce different results, but it should look something like this:

```
To retire at age 58:

You will need $2,439,635.00
You will have saved $521,516.00
Increase your savings rate to meet your goal!
```

## Running the test suite

There are some basic tests included which can be run simply using

```bash
$pytest
```

The tests are located in a `tests/` directory and will be automatically
detected.

## Final thoughts

This was a fun project to work on, and I'm excited for a chance to discuss it further! I was surprised by the complexity of the calculations required to work backwards from a $0 balance like this, which led to some funky workarounds (like calculating an annual return from investments before the user withdraws money, thereby overestimating ROI in the `_amount_needed_at_retirement` method).

Feel free to reach out with questions or comments, I'm definitely open to feedback.

Thank you!
