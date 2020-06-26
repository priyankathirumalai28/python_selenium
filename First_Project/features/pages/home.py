from .locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.btn_welcome = Locators.btn_welcome_xpath
        self.btn_logout = Locators.btn_logout_xpath
        self.span_assign_leave = Locators.span_assign_leave_xpath
        self.span_leave = Locators.span_leave_xpath
        self.span_quick_assign_leave = Locators.span_quick_assign_leave_xpath
        self.span_time = Locators.span_time_xpath
        self.span_time_attendance = Locators.span_time_attendance_xpath
        self.span_time_attendance_employee_report = Locators.span_time_attendance_employee_report_xpath
        self.span_time_project_info = Locators.span_time_project_info_xpath
        self.span_time_project_customers = Locators.span_time_project_customers_xpath

    def click_welcome(self):
        return self.driver.find_element_by_xpath(self.btn_welcome).click()

    def click_logout(self):
        return self.driver.find_element_by_xpath(self.btn_logout).click()

    def click_leave(self):
        return self.driver.find_element_by_xpath(self.span_leave).click()

    def click_assign_leave(self):
        return self.driver.find_element_by_xpath(self.span_assign_leave).click()

    def click_quick_assign_leave(self):
        return self.driver.find_element_by_xpath(self.span_quick_assign_leave).click()

    def click_time(self):
        return self.driver.find_element_by_xpath(self.span_time).click()

    def click_time_attendance(self):
        return self.driver.find_element_by_xpath(self.span_time_attendance).click()

    def click_time_attendance_employee_report(self):
        return self.driver.find_element_by_xpath(self.span_time_attendance_employee_report).click()

    def click_time_project_info(self):
        return self.driver.find_element_by_xpath(self.span_time_project_info).click()

    def click_time_project_customers(self):
        return self.driver.find_element_by_xpath(self.span_time_project_customers).click()