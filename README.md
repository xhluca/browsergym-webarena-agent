# Simple BrowserGym Agent

This agent will execute your action based on what you say in the chat, directly as commands.

https://github.com/xhluca/browsergym-simple-agent/assets/21180505/7c12d147-698b-464b-8d74-886763125d2d


## Quickstart

```bash
# Clone the repository
git clone https://github.com/xhluca/browsergym-webarena-agent
cd browsergym-webarena-agent

# Create a virtual environment and install the dependencies
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# add necessary nltk tokenizer
python -c "import nltk; nltk.download('punkt')"

# Install playwright
playwright install

# Change to your own url
export BASE_URL="http://ec2-3-131-244-37.us-east-2.compute.amazonaws.com"
# Setup the URLs as environment variables
export SHOPPING="$BASE_URL:7770/"
export SHOPPING_ADMIN="$BASE_URL:7780/admin"
export REDDIT="$BASE_URL:9999"
export GITLAB="$BASE_URL:8023"
export WIKIPEDIA="$BASE_URL:8888/wikipedia_en_all_maxi_2022-05/A/User:The_other_Kiwix_guy/Landing"
export MAP="$BASE_URL:3000"
export HOMEPAGE="$BASE_URL:4399"

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
