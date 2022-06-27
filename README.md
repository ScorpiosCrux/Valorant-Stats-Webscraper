# Valorant Stats Webscraper

- This code uses `tracker.gg` to obtain information.


## Setting up Python Virtual Environment

- I don't like installing python packages globally, thus:

- Instructions are from: https://docs.python.org/3/tutorial/venv.html

1. python3 -m venv *valorant-stats-webscraper* <br />
replace *valorant-stats-webscraper* with whatever you desire

2. source *valorant-stats-webscraper*/bin/activate <br />
replace *valorant-stats-webscraper* with what you had in step 1.

3. pip install *package*

- Now you can use pip normally

- `deactivate` to **exit**

## Prereqs: 
- You need chromedriver in your path.
- You will need to check the compatibility with chromedriver and chrome
- `brew install cask chromedriver` is the command on **MacOS**

## Known Issues:
* With Chrome v103 there an error when running with VSCode debugger. Try running without break points.
