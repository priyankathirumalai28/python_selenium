from .locators import Locators


class LeaveList:

    def __init__(self, driver):
        self.driver = driver

        self.date_picker_from_date_xpath = Locators.span_from_date_leave_list_xpath
        self.date_picker_to_date_xpath = Locators.span_to_date_leave_list_xpath
        self.show_leave_with_status_all_xpath = Locators.span_show_leave_with_status_all_xpath
        self.employee_xpath = Locators.span_employee_xpath
        self.sub_unit_xpath = Locators.span_sub_unit_xpath
        self.include_past_employee_xpath = Locators.span_include_past_employee_xpath
        self.click_search_button_xpath = Locators.btn_search_leave_list_xpath
        self.click_reset_button_xpath = Locators.btn_reset_leave_list_xpath

    def set_from_date(self, from_date):
        self.driver.find_element_by_xpath(self.date_picker_from_date_xpath).clear()
        return self.driver.find_element_by_xpath(self.date_picker_from_date_xpath).send_keys(from_date)

    def set_to_date(self, to_date):
        self.driver.find_element_by_xpath(self.date_picker_to_date_xpath).clear()
        return self.driver.find_element_by_xpath(self.date_picker_to_date_xpath).send_keys(to_date)

    def set_show_leave_with_status(self):
        return self.driver.find_element_by_xpath(self.show_leave_with_status_all_xpath).click()

    def set_employee(self, employee):
        self.driver.find_element_by_xpath(self.employee_xpath).clear()
        return self.driver.find_element_by_xpath(self.employee_xpath).send_keys(employee)

    def set_sub_unit(self):
        return self.driver.find_element_by_xpath(self.sub_unit_xpath)

    def set_include_past_employee(self):
        return self.driver.find_element_by_xpath(self.include_past_employee_xpath).click()

    def click_search_button(self):
        return self.driver.find_element_by_xpath(self.click_search_button_xpath).click()

    def click_reset_button(self):
        return self.driver.find_element_by_xpath(self.click_reset_button_xpath).click()
