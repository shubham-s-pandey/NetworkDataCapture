# NetworkDataCapture
This script automates the process of capturing network data from a list of URLs using Selenium WebDriver with Firefox. It reads URLs from a text file, navigates to each URL, waits for the page to load, and captures the network data. The captured data is immediately written to an output file after each URL is processed, ensuring that progress is saved and reducing the risk of data loss. The script uses the performance logs from the browser’s window object and filters for logs with ‘responseEnd’. This script is particularly useful for web scraping, web testing, and data analysis tasks. Additionally, it can be used to fetch API endpoints.

# Prerequisites
Before running NetworkDataCapture.py, you need to install the following Python packages:

Selenium
WebDriver Manager
You can install these packages using pip:

pip install selenium webdriver_manager

# Dependencies
The script depends on the following Python packages:

selenium: For automating web browser interaction.
webdriver_manager: To manage the browser driver needed by Selenium.
Please ensure these dependencies are installed before running the script. If you encounter any issues, refer to the respective package documentation for troubleshooting tips.
