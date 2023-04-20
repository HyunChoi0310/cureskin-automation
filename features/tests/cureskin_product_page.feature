# Created by Hyun at 4/20/2023
Feature: CureSkin.com Automation
  Scenario: The user can search face wash products
    Given Open CureSkin Product main page
    When Click hamburger menu
    And Click shop by product
    And Click face washes
    Then Verify the products showed