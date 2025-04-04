import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class Test_Login:

    def test_login_valid_credentials(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"My Account").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("danny2@yopmail.com")
        self.driver.find_element(By.ID,"input-password").send_keys("Qwerty@123")
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        assert self.driver.find_element(By.PARTIAL_LINK_TEXT,"Edit your account information").is_displayed()



    def test_login_invalid_credentials(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"My Account").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("danny2@yopmail.com")
        self.driver.find_element(By.ID,"input-password").send_keys("Qwert@123")
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        time.sleep(3)
        expected_text="Warning: No match for E-Mail Address and/or Password."
        actual_text = self.driver.find_element(By.XPATH,"//div[text()='Warning: No match for E-Mail Address and/or Password.']").text
        assert expected_text == actual_text


    def test_login_no_credentials(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"My Account").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Login").click()
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        actual_text = self.driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text
        assert expected_text == actual_text
