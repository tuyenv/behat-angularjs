Feature: Authentication
  In order to gain access to the site management area
  As an admin
  I need to be able to login and logout
  
  Scenario: Logging in
    Given I visit "/login"
    When I fill "username" with "foo"
    And I fill "password" with "bar"
    And I press "Login"
    Then I should get a "200" HTTP response