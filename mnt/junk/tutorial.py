from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

def start_browser_and_navigate():
    # Setting up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Starting the Chrome browser with the specified options
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    
    # Navigating to the first URL and waiting for 10 seconds
    browser.get("https://administrator:BI.fon!@bi-test.mojasrednjaskola.gov.rs/reports/powerbi/test-dashboard?rs:embed=true")
    browser.get("https://bi-test.mojasrednjaskola.gov.rs/reports/powerbi/test-dashboard?rs:embed=true")
    
    # time.sleep(10)
    
    iframe_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    browser.switch_to.frame(iframe_element)
    # Waiting for the div with the imageBackground class after login
    image_element = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'imageBackground'))
    )

    # Extracting the background-image URL
    style_value = image_element.get_attribute('style')
    start_index = style_value.find('url("') + 5
    end_index = style_value.find('")')
    image_url = style_value[start_index:end_index]

    print("Image URL:", image_url)



start_browser_and_navigate()