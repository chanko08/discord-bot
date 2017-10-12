# Discord Bot

## Current Features

* It is possible to pull tweets from Twitter and print them in the Discord channel

## Installation

To install this you need the latest Python 3, the discord.py and tweepy Python libraries.

Installing dependencies on Ubuntu 17.04 (and probably greater):
 
```
sudo apt-get install python3.6 python3-venv python3-pip

git clone https://github.com/chanko08/discord-bot.git

cd discord-bot

mkdir discord-python-env
cd discord-python-env
python3 -m venv .

source bin/activate

pip install discord.py
pip install tweepy
```

At this point you will have a Python 3 virtual environment setup with the appropriate libraries.
To run the discord bot right now you'll need to get a Discord access token as well as Twitter access tokens.