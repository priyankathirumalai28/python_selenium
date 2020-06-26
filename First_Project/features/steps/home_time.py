from behave import *
from selenium.webdriver.support.select import Select
import time
use_step_matcher("re")


@when('I click on the "Time"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.home.click_time()

@when('I click on the "Attendance"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.home.click_time_attendance()


@when('I click on the "Employee Records"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.home.click_time_attendance_employee_report()

@when('I fill the input field')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.time.set_employee_name_attendance_xpath("All")
    context.time.set_date_attendance_xpath('2020-25-06')
    context.time.click_view()
    time.sleep(20)

@then("I must navigate to the View Table")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.browser.current_url == "https://opensource-demo.orangehrmlive.com/index.php/attendance/viewAttendanceRecord"

@when('I click on the "Project Info"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.home.click_time_project_info.click()

@when('I click on the "Customers"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.home.click_time_project_customers.click()

@when('I click on the "Add" Button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@when('I Fill the customer details')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # https: // opensource - demo.orangehrmlive.com / index.php / admin / addCustomer
    pass

@when('I Click on "Save" Button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # https: // opensource - demo.orangehrmlive.com / index.php / admin / viewCustomers
    pass