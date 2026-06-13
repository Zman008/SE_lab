import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize browser
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # 1. Open the website
    driver.get("https://testsheepnz.github.io/BasicCalculator.html")
    time.sleep(2)
    
    driver.find_element(By.ID, "number1Field").send_keys("10")
    time.sleep(1)  
    driver.find_element(By.ID, "number2Field").send_keys("20a")
    time.sleep(1)  
    driver.find_element(By.XPATH, "/html/body/section/div/div/div/form[2]/div[3]/div[2]/select/option[3]").click()
    time.sleep(1)
    driver.find_element(By.ID, "calculateButton").click()
    
    time.sleep(4)  
    
    errorMsg = driver.find_element(By.ID, "errorMsgField").text
    time.sleep(1)

    if errorMsg == "Number 1 is not a number":
        print(f"First input is invalid")
    elif errorMsg == "Number 2 is not a number":
        print(f"Second input is invalid")
    else:
        print("Valid Number Entered")

finally:
    driver.quit()