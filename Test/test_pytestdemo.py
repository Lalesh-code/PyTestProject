from selenium import webdriver
import pytest

class TestDemo():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(r"C:\Users\Admin\PycharmProjects\Lalesh_Python\Drivers\chromedriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        driver.implicitly_wait(3)
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_login(self, test_setup):
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()

        x=driver.title
        assert x=="OrangeHRM"
