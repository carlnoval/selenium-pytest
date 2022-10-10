"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

# dependencies
# from typing import KeysView
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class DuckDuckGoSearchPage:

  URL = "https://www.duckduckgo.com"

  # search input locator as tuple class variables since only one immutable varaibale is needed
  SEARCH_INPUT = (By.ID, "search_form_input_homepage")
  INCOGNITO_SEARCH_INPUT = (By.ID, "searchbox_input")
  
  # dunder init method constructor
  def __init__(self, browser):
    self.browser = browser

  # loads a web page in the current browser session
  def load(self):
    self.browser.get(self.URL)

  # 
  def search(self, phrase):
    # passing class variable tuple as *args for find_element
    # driver sometimes open incognito/normal page of duckduckgo
    # if the normal page loads, have to wait for 10 seconds
    try:
      search_input = self.browser.find_element(*self.INCOGNITO_SEARCH_INPUT)
    except NoSuchElementException:
      search_input = self.browser.find_element(*self.SEARCH_INPUT)
    # search_input = self.browser.find_element(*self.SEARCH_INPUT)

    # this does not work
    # search_intput =self.browser.find_element(*self.SEARCH_INPUT) or self.browser.find_element(*self.INCOGNITO_SEARCH_INPUT)

    # sends texts and return button to load search results page
    search_input.send_keys(phrase + Keys.RETURN)
    # hmmm what is this???
    # search_intput.send_keys(phrase + KeysView.RETURN)
