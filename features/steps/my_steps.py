from time import sleep

from behave import *
from selenium.webdriver.common.by import By

from resources.page_actions import SeleniumEasy
from data import element_mapper as em

use_step_matcher("parse")


@given("I am on the test page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver = SeleniumEasy()
    context.driver.open_site(em.home)


@then("I should be able to check for the presence of a popup")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.page_wait(By.ID, em.popup)
    context.driver.check_popup(By.ID, em.popup, em.close_popup)


@when('I click the "{text}" option')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "input forms":
        context.driver.click_an_element(By.CSS_SELECTOR, em.input_forms)
    elif text == "checkbox demo":
        context.driver.click_an_element(By.CSS_SELECTOR, em.checkbox_demo)
    elif text == "single box":
        context.driver.click_an_element(By.CSS_SELECTOR, em.checkbox_single)
    elif text == "alerts & modals":
        context.driver.scroll_down()
        context.driver.click_an_element(By.CSS_SELECTOR, em.alerts_modals)
    elif text == "javascript alerts":
        context.driver.click_an_element(By.CSS_SELECTOR, em.js_alerts)
    elif text == "list box":
        context.driver.scroll_down()
        context.driver.click_an_element(By.CSS_SELECTOR, em.list_box)
    elif text == "jquery list box":
        context.driver.click_an_element(By.CSS_SELECTOR, em.jq_list_box)


@then('I should be able to see the "{text}" on the list')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "checkbox demo":
        context.driver.page_wait(By.CSS_SELECTOR, em.checkbox_demo)
    elif text == "javascript alerts":
        context.driver.page_wait(By.CSS_SELECTOR, em.js_alerts)
    elif text == "jquery list box":
        context.driver.page_wait(By.CSS_SELECTOR, em.jq_list_box)


@then('The "{text}" page should load successfully')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "checkbox":
        context.driver.page_wait(By.CSS_SELECTOR, em.checkbox_single)
    elif text == "javascript alerts":
        context.driver.page_wait(By.CSS_SELECTOR, em.js_alert_box)


@then("I should be able to see a success message")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.check_text(By.ID, em.success_check, em.success_check_message)


@when('I click the "{text}" button')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "check all":
        context.driver.click_an_element(By.ID, em.check_all_btn)
    elif text == "uncheck all":
        for i in range(2):
            context.driver.click_an_element(By.ID, em.check_all_btn)
    elif text == "alert box":
        context.driver.click_an_element(By.CSS_SELECTOR, em.js_alert_box)
    elif text == "confirm box":
        context.driver.click_an_element(By.CSS_SELECTOR, em.js_confirm_box)
    elif text == "prompt box":
        context.driver.click_an_element(By.CSS_SELECTOR, em.js_prompt_box)
    elif text == "add":
        context.driver.click_an_element(By.CSS_SELECTOR, em.add_button)
    elif text == "add all":
        context.driver.click_an_element(By.CSS_SELECTOR, em.add_all_button)
    elif text == "remove all":
        context.driver.click_an_element(By.CSS_SELECTOR, em.remove_all_button)


@then('All the multiple check boxes should be "{text}"')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "checked":
        context.driver.locate_attribute(By.ID, em.check_all_btn, em.uncheck)
    elif text == "unchecked":
        context.driver.locate_attribute(By.ID, em.check_all_btn, em.check)


@when('I click "{text}" checkbox')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "one":
        context.driver.click_an_element(By.CSS_SELECTOR, em.checkbox_one)


@then("The box should be checked")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.locate_attribute()


@step('I click "{text}" on the alert box')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "ok":
        context.driver.accept_alert()
    elif text == "cancel":
        context.driver.dismiss_alert()


@then("The alert box should close")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('Testing')


@then('I should see a message for "{text}" text')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "ok":
        context.driver.verify_text(By.ID, em.confirm_demo, em.ok_text)
    elif text == "cancel":
        context.driver.verify_text(By.ID, em.confirm_demo, em.cancel_text)
    elif text == "inserted":
        context.driver.verify_text(By.ID, em.prompt_demo, em.sample_name)


@step("I insert a value into the input field on the alert")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.type_a_value(em.sample_name)


@when('I select "{text}" of the names')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "any":
        context.driver.select_an_item(By.CSS_SELECTOR, em.data_box, em.luiza)
    elif text == "some":
        context.driver.select_an_item(By.CSS_SELECTOR, em.data_box, em.valentina)
        context.driver.select_an_item(By.CSS_SELECTOR, em.data_box, em.giovanna)
        context.driver.select_an_item(By.CSS_SELECTOR, em.data_box, em.luiza)


@then('I should see "{text}" name in the result box')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "that":
        context.driver.verify_text(By.CSS_SELECTOR, em.result_box, em.luiza)
    elif text == "those":
        context.driver.verify_text(By.CSS_SELECTOR, em.result_box, em.giovanna)
        context.driver.verify_text(By.CSS_SELECTOR, em.result_box, em.valentina)
    elif text == "all":
        context.driver.verify_text(By.CSS_SELECTOR, em.result_box, em.sophia)
        context.driver.verify_text(By.CSS_SELECTOR, em.result_box, em.manuela)
        context.driver.verify_text(By.CSS_SELECTOR, em.result_box, em.isabella)


@then('I should see "{text}" name in the data box')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    if text == "all":
        context.driver.verify_text(By.CSS_SELECTOR, em.data_box, em.sophia)
        context.driver.verify_text(By.CSS_SELECTOR, em.data_box, em.manuela)
        context.driver.verify_text(By.CSS_SELECTOR, em.data_box, em.isabella)
