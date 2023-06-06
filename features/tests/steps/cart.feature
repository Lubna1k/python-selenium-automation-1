#Created by lubna khan at 6/5/2023
Feature: If no product has been added the shopping cart is empty

Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify "Your Shopping Cart is empty" text present