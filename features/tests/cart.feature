# Created by khalinaboyce at 3/19/25
Feature:Cart

    Scenario: Verify empty cart message
    Given the user is on the Target homepage with an empty cart
    When the user clicks on the Cart icon
    Then the message "Your cart is empty" should be displayed

