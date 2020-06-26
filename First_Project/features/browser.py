from selenium import webdriver


class Browser:
    driver = webdriver.Chrome(executable_path="/home/priyanka/Desktop/test_selenium/drivers/chromedriver")
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)
    driver.maximize_window()

    def get_driver(self):
        return self.driver
    # def quit(self):
    #     self.driver.quit()
