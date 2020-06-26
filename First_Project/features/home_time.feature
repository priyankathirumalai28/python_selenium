Feature: List Of leave Of an employee
  Testing For LeaveList To Employee

  Scenario: Test To View LeaveList To Employee
    Given I login to the OrangeHRMS
    When  I click on the "Time"
    And I click on the "Attendance"
    And I click on the "Employee Records"
    And I fill the input field
    Then I must navigate to the View Table

  Scenario: Test To View Project Customer To Employee
    Given I login to the OrangeHRMS
    When  I click on the "Time"
    And I click on the "Project Info"
    And I click on the "Customers"
    Then I must navigate to the View Project Customer Table

#  Scenario: Test To View Project Customer To Employee
#    Given I login to the OrangeHRMS
#    When  I click on the "Time"
#    And I click on the "Project Info"
#    And I click on the "Customers"
#    And I Click on "Add" Button
#    And I Fill the customer details
#    And I Click on "Save" Button
#    Then I must navigate to the View Project Customer Table