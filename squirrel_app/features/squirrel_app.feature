Feature: Squirrel Town management with built-ins
  As the mayor of Squirrel Town
  I want to add, remove, and edit squirrels
  So that the squirrels are well kept and orderly


  Background:
    Given I open the url "http://localhost:8000/index.html"

  Scenario: Squirrel Town website opens
    Then I expect that element "h1" contains any text

  Scenario: I want the squirrel list to be empty at first
    When I pause for 500ms
    Then I expect that element "#squirrels-list" is empty

  Scenario: I see the add squirrels dialog only when it should be there
    Then I expect that element "#squirrel-dialog" is not visible
    When I click on the button "#add-button"
    Then I expect that element "#squirrel-dialog" is visible
    When I click on the button "#cancel-button"
    Then I expect that element "#squirrel-dialog" is not visible

  Scenario: I click on the add squirrel button
    When I click on the button "#add-button"
    Then I expect that element "#dialog-title" contains any text

  Scenario: I see a list of squirrels
    When I pause for 500ms
    Then I expect that element "#squirrels-list" does exist

  Scenario: I can add a squirrel
    When I click on the button "#add-button"
    When I add "Chippy" to the inputfield "#squirrel-name-input"
    When I add "small" to the inputfield "#squirrel-size-input"
    When I click on the button "#save-button"
    When I pause for 500ms
    Then I expect that element "#squirrel-dialog" is not visible
    And I expect that element "#squirrels-list" contains the text "Chippy"

  Scenario: I can delete a squirrel
    When I click on the button ".fa-trash"
    When I accept the alertbox
    When I pause for 500ms
    Then I expect that element "#squirrels-list" is empty

  Scenario: Entering just a squirrel name should not work
    When I click on the button "#add-button"
    When I add "Nuttie" to the inputfield "#squirrel-name-input"
    When I click on the button "#save-button"
    When I pause for 500ms
    Then I expect that element "#squirrel-dialog" is visible

  Scenario: Entering just a squirrel size should not work
    When I click on the button "#add-button"
    When I add "small" to the inputfield "#squirrel-size-input"
    When I click on the button "#save-button"
    When I pause for 500ms
    Then I expect that element "#squirrel-dialog" is visible

  Scenario: Entering nothing should not work
    When I click on the button "#add-button"
    When I click on the button "#save-button"
    When I pause for 500ms
    Then I expect that element "#squirrel-dialog" is visible
