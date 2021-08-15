# Created by Ademola Bhadmus on 15/08/2021
Feature: Alerts and Modals
  The Javascript Alerts will be tested

  Background:
    Given I am on the test page
    Then I should be able to check for the presence of a popup
    When I click the "alerts & modals" option
    Then I should be able to see the "javascript alerts" on the list
    When I click the "javascript alerts" option
    Then The "javascript alerts" page should load successfully

  Scenario: A user should see alert box and click ok
    When I click the "alert box" button
    And I click "ok" on the alert box
    Then The alert box should close

  Scenario: A user should be able to confirm an alert box
    When I click the "confirm box" button
    And I click "ok" on the alert box
    Then I should see a message for "ok" text

  Scenario: A user should be able to cancel an alert box
    When I click the "confirm box" button
    And I click "cancel" on the alert box
    Then I should see a message for "cancel" text

  Scenario: A user should be able to confirm an alert box with a text
    When I click the "prompt box" button
    And I insert a value into the input field on the alert
    And I click "ok" on the alert box
    Then I should see a message for "inserted" text