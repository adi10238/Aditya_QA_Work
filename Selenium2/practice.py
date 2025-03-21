from selenium import webdriver


driver = webdriver.Chrome()
#navigate to URL
driver.get("https://www.google.com")
#maximize the browser
driver.maximize_window()
#take a screenshot
driver.get_screenshot_as_file("ss.png")
