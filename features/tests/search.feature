# Created by khalinaboyce at 3/19/25
Feature:  Search for products on Target

 #   Scenario Outline: User searches for a product
  #  Given the user is on the Target homepage
   # When they search for "<search_term>"
    #Then verify results for "<search_term>" should be displayed


    #  Examples:
     #   | search_term |
      #  | laptop       |
       # | iPhone       |
        #| sneakers     |


  Scenario Outline: Add product to cart
    Given the user is on the Target homepage with an empty cart
    When the user searches for "<search_term>"
    And the user clicks the add to cart button
    And confirm add to cart on side navigation
    And click view cart
    Then verify cart has 1 item


      Examples:
        | search_term |
        | cup       |


