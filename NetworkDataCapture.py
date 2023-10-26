from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

# Initialize Firefox Options
options = webdriver.FirefoxOptions()
#options.add_argument('--headless')

# Initialize WebDriver
driver = webdriver.Firefox(service=webdriver.firefox.service.Service(GeckoDriverManager().install()), options=options)

# Read URLs from file
with open('urls.txt', 'r') as f:
    urls = f.read().splitlines()

for i, url in enumerate(urls):
    print(f"Processing URL {i+1} of {len(urls)}: {url}")
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Wait for additional time to capture more network requests
    time.sleep(2)  # Adjust this value as needed

    # Get the performance logs using execute_script()
    logs = driver.execute_script("return window.performance.getEntries()")

    network_data = []
    for log in logs:
        if 'responseEnd' in log:  # Corrected line
            try:
                network_data.append(log)
            except:
                pass

    print(f"Captured {len(network_data)} network requests for this URL.")

    # Write network data to file after each URL is processed
    with open('output.txt', 'a') as f:
        for data in network_data:
            f.write("%s\n" % data)

print("Finished writing network data to output.txt.")

driver.quit()
