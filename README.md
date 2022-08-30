# Retirement Calculator

This is a coding exercise for an interview, not real financial advice!

## Getting started

I used an external library called [babel](https://babel.pocoo.org/en/latest/api/numbers.html) to quickly format currencies. To install it with pip, simply run:

```bash
$pip3 install -r requirements.txt
```
You may wish to set up a virtual environment before doing this, but I won't go into the details of that here.

Before running the script, you'll need to select a user id. There are an
infinite number of users available, any number you choose will generate a
random unique user. Once you've chosen a number, head to your command line and
run the following command:

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
