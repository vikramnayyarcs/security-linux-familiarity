import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Make a session object
session = requests.Session()

# Define the URLs
url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastTwoDigitZIP=on"

# Make the first request and store cookies in the session
response1 = session.get(url1)

# Extract the relevant JavaScript code from the HTML response
script_code = response1.text.split('<script>', 1)[1].split('</script>', 1)[0]

# Set up a headless Chrome browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run headless (without opening a browser window)
driver = webdriver.Chrome(options=options)

try:
    # Load the extracted JavaScript code into the browser
    driver.execute_script(script_code)

    # Wait for the script to execute
    element_present = EC.presence_of_element_located((By.ID, 'table6'))
    WebDriverWait(driver, 1).until(element_present)  # Adjust timeout if needed

    # Additional actions if needed after script execution
    # For example, you can print the updated HTML content
    print(driver.page_source)

finally:
    # Close the browser window
    driver.quit()

# Make the second request using the same session
response2 = session.get(url2)

# Print the content of the second response
print(response2.text)

# Optionally, you can clear cookies after the second request if needed
session.cookies.clear()
