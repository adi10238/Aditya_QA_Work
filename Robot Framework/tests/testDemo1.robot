*** Settings ***
Documentation    Automate a Login & Search Functionality
Library    SeleniumLibrary


*** Variables ***
${URL}    https://www.saucedemo.com/
${user_name}    standard_user
${password}    secret_sauce
${FIRST_NAME}    Aditya
${LAST_NAME}    Sharma
${POSTAL_CODE}                201002

*** Test Cases ***
Opens a browser and navigate to website
    Opens a browser and navigate to website

Logs in using valid and invalid credentials
    Log in using invalid credentials
    Log in using valid credentials

Searches for an item after login
    Select items

Validates search results
    Verify added elements

Completing the checkout process
    Checkout process




*** Keywords ***
Opens a browser and navigate to website
    Create Webdriver    Chrome
    Go To    https://www.saucedemo.com/

Log in using invalid credentials
    Input Text    user-name    abc
    Input Text    password    ${password}
    Click Button    login-button
    Page Should Contain    match

Log in using valid credentials
    Input Text    user-name    ${user_name}
    Input Text    password    ${password}
    Click Button    login-button

Select items
    Click Button    add-to-cart-sauce-labs-backpack
    Sleep    3
    Click Element            css:.shopping_cart_link
    Capture Page Screenshot    screenshot.png

Verify added elements
    Element Should Be Visible    xpath://div[text()='Sauce Labs Backpack']
    Click Element    checkout

Checkout process
    Input Text    first-name    ${FIRST_NAME}
    Input Text    last-name    ${LAST_NAME}
    Input Text    postal-code    ${POSTAL_CODE}  
    Click Element    continue
    Page Should Contain    Total
    Click Element    finish
    Page Should Contain    Thank you for your order!
    Capture Page Screenshot