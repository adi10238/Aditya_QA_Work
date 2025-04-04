import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setup_and_teardown")
class Test_Search:

    def test_search_valid_product(self):
        self.driver.find_element(By.NAME,"search").send_keys("HP")
        self.driver.find_element(By.CSS_SELECTOR,".btn-default").click()
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()


    def test_search_invalid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("Honda")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
        expected_text="There is no product that matches the search criteria."
        fetched_text = self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text
        assert expected_text == fetched_text



    def test_search_no_product(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
        expected_text="There is no product that matches the search criteria."
        fetched_text= self.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text
        assert expected_text == fetched_text


