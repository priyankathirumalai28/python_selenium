from .locators import Locators


class TimePage:

    def __init__(self, driver):
        self.driver = driver

        self.txt_employee_name_attendance_xpath = Locators.txt_employee_name_attendance_xpath
        self.date_pick_date_attendance_xpath = Locators.date_pick_date_attendance_xpath
        self.btn_view_attendance_xpath = Locators.btn_view_attendance_xpath

    def set_employee_name_attendance_xpath(self, emp_name):
        self.driver.find_element_by_xpath(self.txt_employee_name_attendance_xpath).clear()
        return self.driver.find_element_by_xpath(self.txt_employee_name_attendance_xpath).send_keys(emp_name)

    def set_date_attendance_xpath(self, emp_name):
        self.driver.find_element_by_xpath(self.date_pick_date_attendance_xpath).clear()
        return self.driver.find_element_by_xpath(self.date_pick_date_attendance_xpath).send_keys(emp_name)

    def click_view(self):
        return self.driver.find_element_by_xpath(self.btn_view_attendance_xpath).click()
