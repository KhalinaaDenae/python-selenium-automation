# Created by khalinaboyce at 3/16/25
Feature: Account sign in

  Scenario: Verify a logged out user can navigate to the sign in page
    Given the user is logged out
    And the user clicks on the "sign in" button
    And the side navigation menu opens
    When the user clicks on the "sign on" button on the side navigation
    Then the sign in form should be displayed for the user