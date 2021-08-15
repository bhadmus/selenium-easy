# Created by Ademola Bhadmus on 15/08/2021
Feature: Input Forms
  The checkbox demo will be tested

  Background:
    Given I am on the test page
    Then I should be able to check for the presence of a popup
    When I click the "input forms" option
    Then I should be able to see the "checkbox demo" on the list
    When I click the "checkbox demo" option
    Then The "checkbox" page should load successfully

  Scenario: A user should be able to click a single checkbox
    When I click the "single box" option
    Then I should be able to see a success message

  Scenario: A user should be able to click to check all checkboxes
    When I click the "check all" button
    Then All the multiple check boxes should be "checked"

  Scenario: A user should be able to click to uncheck all checkboxes
    When I click the "uncheck all" button
    Then All the multiple check boxes should be "unchecked"

