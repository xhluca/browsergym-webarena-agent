# Simple BrowserGym Agent

This agent will execute your action based on what you say in the chat, directly as commands.

[Simple BrowserGym Agent Demo](demo.mp4)

## Quickstart

```bash
# Clone the repository
git clone https://github.com/xhluca/browsergym-simple-agent
cd browsergjson-simple-agent

# Create a virtual environment and install the dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# run the agent
python run.py
```

## Usage

Simply type one of the following lines in the chat and see what happens!
```python
# say action
say("hello") # first arg is the utterance
say(utterance="hi") # default speaker is "instructor"
say(speaker="instructor", utterance="I am the instructor")

# textinput (change uid to the id of the input field)
textinput(uid="111", value="agents")


# click action (change uid to the id of the element you want to click)
click(uid="245")


# loading urls
load(url="https://webllama.github.io")

# scrolling
scroll(x=0, y=300)
```

## Quickstart

```bash
python run.py
```
