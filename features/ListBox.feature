# Created by Ademola Bhadmus on 15/08/2021
Feature: List Box
  The JQuery List Box

  Background:
    Given I am on the test page
    Then I should be able to check for the presence of a popup
    When I click the "list box" option
    Then I should be able to see the "jquery list box" on the list
    When I click the "jquery list box" option
    Then The "jquery list box" page should load successfully

  Scenario: A user should be able to add one name
    When I select "any" of the names
    And I click the "add" button
    Then I should see "that" name in the result box

  Scenario: A user should be able to add more than one name
    When I select "some" of the names
    And I click the "add" button
    Then I should see "those" name in the result box

  Scenario: A user should be able to add all names
    When I click the "add all" button
    Then I should see "all" name in the result box

  Scenario: A user should be able to remove all names
    When I click the "add all" button
    Then I should see "all" name in the result box
    When I click the "remove all" button
    Then I should see "all" name in the data box