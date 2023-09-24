from locust import HttpUser, task
from locust_plugins.users.webdriver import WebdriverUser
from locust.env import Environment
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebUser(HttpUser):  # Inheriting from WebdriverUser instead of HttpUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.env = Environment()

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.browser = webdriver.Chrome(options=options)

    @task
    def load_and_wait(self):
        start_time = time.time()
        url = "https://bi-test.mojasrednjaskola.gov.rs/reports/powerbi/test-dashboard?rs:embed=true"
        try:
            self.browser.get("https://administrator:BI.fon!@bi-test.mojasrednjaskola.gov.rs/reports/powerbi/test-dashboard?rs:embed=true")
            self.browser.get(url)

            iframe_element = WebDriverWait(self.browser, 120).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
            self.browser.switch_to.frame(iframe_element)
            
            image_element = WebDriverWait(self.browser, 120).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'imageBackground'))
            )

            # Extracting the background-image URL
            style_value = image_element.get_attribute('style')
            start_index = style_value.find('url("') + 5
            end_index = style_value.find('")')
            image_url = style_value[start_index:end_index]

            print("Image URL:", image_url)
            
            total_time = int((time.time() - start_time) * 1000)  # get total time in milliseconds
            self.environment.events.request.fire(request_type="GET", name="Page Load", response_time=total_time, response_length=0)

        except Exception as e:
            # If any exception occurs, we fire a failure event for Locust.
            total_time = int((time.time() - start_time) * 1000)
            self.environment.events.request.fire(request_type="GET", name="Page Load", response_time=total_time, exception=e, response_length=0)

            
    def on_start(self):
        print('In on_start method')

    def on_stop(self):
        print('In on_stop method')
        self.browser.quit()
