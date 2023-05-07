# Created by Hyun at 4/20/2023
Feature: CureSkin.com Automation
  Scenario: The user can search face wash products
    Given Open CureSkin Product main page
    When close the popup window
    And Click hamburger menu
    And Click shop by product
    And Click face washes
    Then The search results page URL contains face-wash

  @smoke
  Scenario: Shop All section is functional
    Given Open CureSkin Product main page
    When close the popup window
    And Click hamburger menu
    And Click on Shop All section
#    And Adjust the Price lower
#    And Adjust the Price upper
#    Then Verify that number of products changes
#    And Verify that products displayed within the Price filter

#exploratory testing
#  Scenario: User can login and logout
#    Given
#
#  Scenario: User can Login and Logout
#  Scenario: User can Search for products
#  Scenario: User can Add to cart
#  Scenario: User can Checkout process
#  Scenario: User can update their personal information
#  Scenario: User can manage their account settings
#  Scenario: User can leave a review