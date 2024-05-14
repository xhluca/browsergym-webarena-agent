# these are just for linting
from browsergym.core.action.utils import get_elem_by_bid
import playwright.sync_api

page: playwright.sync_api.Page = None
send_message_to_user: callable = None

def say(utterance: str, *args, **kwargs):
    """
    Sends a message to the user.

    Examples:
        say("Based on the results of my search, the city was built in 1751.")
    """
    send_message_to_user(utterance)


def click(uid: str):
    """
    Click an element.

    Examples:
        click('51')
    """
    elem = get_elem_by_bid(page, uid)
    elem.click()

def textinput(uid: str, value: str):
    """
    Fill out a form field. It focuses the element and triggers an input event with the entered text.
    It works for <input>, <textarea> and [contenteditable] elements.

    Examples:
        textinput('237', 'example value')
        textinput('45', "multi-line\\nexample")
        textinput('32-12', "example with \\"quotes\\"")
    """
    elem = get_elem_by_bid(page, uid)
    elem.fill(value)

def load(url: str, *args, **kwargs):
    """
    Navigate to a url.

    Examples:
        goto('http://www.example.com')
    """
    page.goto(url)

def scroll(x: float, y: float):
    """
    Scroll horizontally and vertically. Amounts in pixels. Dispatches a wheel event.

    Examples:
        scroll(0, 200)
        scroll(-50.2, -100.5)
    """
    page.mouse.wheel(x, y)

def wait(seconds: float=1):
    """
    Does nothing. Useful for when you want to wait for something to happen.

    Examples:
        wait(2)
    """
    page.wait_for_timeout(seconds * 1000)