# SlackBot Python Base Files
Testing a basic slackbot, currently it repeats any phrase back to you.

## Requirements
* Python 3.6
* Python module `slackclient` therefore:
  * `pip install slackclient`
* Environment variable of `SLACK_BCHBOT` set to your slack bot key, therefore:
  * Windows - `setx SLACK_BCHBOT <MYKEY>`
  * Linux - `export SLACK_BCHBOT=<MYKEY>`

## To Run
Using Python 3.6:  
`python main.py`