from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
def my_function(driver):
    driver.maximize_window()
    driver.get("https://www.python.org/")
    driver.find_element(By.ID, "id-search-field").send_keys("bla bla")
    driver.find_element(By.ID, 'submit').click()
    result = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/form/ul/p').text
    if result == "No results found.":
        print ('True')
    else:
        print ('False')
    print(driver.title)
    print(driver.current_url)
    driver.close()
my_function(driver = webdriver.Chrome(ChromeDriverManager().install()))
my_function(driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()))