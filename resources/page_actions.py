from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from webconfig import Driver


class SeleniumEasy:
    """
    This class file handles all interactions with the
    web page and also creates generic methods for
    common actions.
    """
    def __init__(self):
        """
        This is the first method that creates the webdriver
        that will be accessible to other generic methods
        """
        # instatiate the Driver class from webconfig.py
        # to have access to selenium Webdriver
        self.driver = Driver()
        # create a smarter variable naming for better readability
        self.browse = self.driver.driver
        self.browse.maximize_window()
        # Create basic action initiator like a pause or hovering
        # over an element
        self.wait = WebDriverWait(self.browse, 30)

    def open_site(self, url):
        """
        This method opens the test site
        :param url: the url of the test site
        :return: a fully loaded test site
        """
        self.browse.get(url)

    def click_an_element(self, selector, element):
        """
        This method helps to click any element using any selector
        :param selector: This specifies the identifier type e.g. id, css or xpath
        :param element: This specifies the element to be clicked
        :return: An expected result from the action
        """
        self.browse.find_element(selector, element).click()

    def type_a_value(self, text):
        """
        This method helps to type any value using any selector
        :param selector: This specifies the identifier type
        :param field: This specifies the field to insert the text
        :param text: The specifies the text value
        :return: A field that has an input value
        """
        self.browse.switch_to_alert().send_keys(text)

    def page_wait(self, selector, element):
        """
        This waits for the page to load
        :param selector: This specifies the identifier type
        :param element: An element to wait for its visibility
        :return: A visible element
        """
        self.wait.until(ec.visibility_of_element_located((selector, element)))

    def verify_text(self, selector, element, word):
        """
        This method verifies that a text is present on the page
        :param selector: This specifies the identifier type
        :param element: the element containing the text
        :param word: The text present
        :return: boolean
        """
        web_element = self.browse.find_element(selector, element)
        try:
            assert word in web_element.text
            print('Text Found!')
        except AssertionError:
            print("Not Found!")

    def check_popup(self, selector, element, close):
        """
        This method closes a pop up if and only if one is present
        :param selector: This specifies the identifier type
        :param element: An element representing the popup
        :param close: An element to close the popup
        :return: A page without popup
        """
        popup = self.browse.find_element(selector, element)
        try:
            if popup:
                self.browse.find_element(selector, close).click()
        except NoSuchElementException:
            raise NoSuchElementException('Element not found')

    def scroll_down(self):
        self.browse.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def check_text(self, selector, element, text):
        """
        This method helps to check that a text is present on an element
        :param selector: This specifies the identifier type
        :param element: This specifies the element to be identified
        :param text: The text to verify
        :return:
        """
        word = self.browse.find_element(selector, element)
        try:
            assert text in word.text
            print('Text Present')
        except AssertionError:
            print("Not Found")

    def locate_attribute(self, selector, element, value):
        """
        This methods gets an attribute from an element
        :param selector: This specifies the identifier type
        :param element: Element to be queried
        :param value: value of the attribute
        :return:
        """
        button = self.browse.find_element(selector, element)
        button_value = button.get_attribute(value)
        try:
            if button_value:
                print('Attribute Present')
        except AssertionError:
            print("Not Found")

    def accept_alert(self):
        """
        This presses ok on a alert box
        :return: no alert boxes
        """
        self.browse.switch_to_alert().accept()

    def dismiss_alert(self):
        """
        This presses ok on a alert box
        :return: no alert boxes
        """
        self.browse.switch_to_alert().dismiss()

    def select_an_item(self, selector, element, identifier):
        """
        This uses the selenium select option to pick an element
        :param selector: This specifies the identifier type
        :param element: Element to be queried
        :param identifier: This could be a value, index, or visible text
        :return:
        """
        select = Select(self.browse.find_element(selector, element))
        select.select_by_visible_text(identifier)
