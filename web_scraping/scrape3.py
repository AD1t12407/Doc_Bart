from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

def fetch_entire_page(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(url)
        page_source = driver.page_source
        return page_source
    except WebDriverException as e:
        print(f"Error: {e}")
        return None
    finally:
        driver.quit()

url = input("Enter the publication link: ")
page_content = fetch_entire_page(url)

if page_content:
    print(page_content)
else:
    print("Failed to retrieve the page content.")
