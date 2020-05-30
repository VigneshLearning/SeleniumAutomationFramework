import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Chrome("C://Users//Vignesh//PycharmProjects//Selenium//driver//chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Podu Thakida Thakida")