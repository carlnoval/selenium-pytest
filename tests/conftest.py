"""
This module contains shared fixtures.
"""

import json                 # needed for parsing
import pytest
import selenium.webdriver


# scope = "session" makes it so the fixture is only ran once for the entire teset suite
@pytest.fixture
def config(scope = "session"):  

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file) # json to python dictionaries

    # Assert values are acceptable
    assert config['browser'] in ["Firefox", "Chrome", "Headless Chrome", "Headless Firefox"]
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config dictionary object so it can be used
    return config


# now depends on config fixture
# this browser fixture will still run for each test case
@pytest.fixture
def browser(config):

  # Initialize the WebDriver instance
    if config["browser"] == "Firefox":
        b = selenium.webdriver.Firefox()
    elif config["browser"] == "Chrome":
        b = selenium.webdriver.Chrome()
    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        b = selenium.webdriver.Chrome(options = opts)
    elif config["browser"] == "Headless Firefox":
        opts = selenium.webdriver.FirefoxOptions()
        opts.add_argument("-headless")
        b = selenium.webdriver.Firefox(options =opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Maximum wait time before waiting for elements to appear and locate
    b.implicitly_wait(config["implicit_wait"])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
