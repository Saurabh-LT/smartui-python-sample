from lambdatest_selenium_driver import smartui_snapshot
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

username = "<USERNAME>"  # Replace the username
access_key = "<ACCESS_KEY>"  # Replace the access key
class FirstSampleTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.browser_version = "118.0"
        options.platform_name = "Windows 11"
        lt_options = {};
        lt_options["resolution"] = "1024x768";
        lt_options["project"] = "Python_SDK";
        lt_options["name"] = "Python_Build";
        lt_options["w3c"] = True;
        lt_options["plugin"] = "python-python";
        lt_options["console"] = True
        lt_options["network"] = True
        lt_options["selenium_version"] = "4.0.0"
        options.set_capability('LT:Options', lt_options);
        self.driver = webdriver.Remote(
            command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            options=options
        )
    def tearDown(self):
        self.driver.quit()
    def test_demo_site(self):
        try:
            driver = self.driver
            driver.implicitly_wait(10)
            driver.set_page_load_timeout(30)
            print('Loading URL')
            driver.get("https://www.lambdatest.com/")
            smartui_snapshot(driver,"1st SS")
            print("1st screenshot")
            driver.implicitly_wait(10)
            driver.execute_script("lambda-status=passed")
        except:
            driver.execute_script("lambda-status=failed")
            print("Failed")
            
if __name__ == "__main__":
    unittest.main()
