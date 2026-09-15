import pytest
from selenium import webdriver
from urls import URLs

@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URLs.MAIN_PAGE_URL)
    yield driver
    driver.quit()
