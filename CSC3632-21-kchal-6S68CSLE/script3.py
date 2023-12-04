from selenium import webdriver
import time

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Define URLs
url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php?hideDayDoB=on&hideLastTwoDigitZIP=on"

# Open the first URL
driver.get(url1)
time.sleep(2)

# Clear cookies after opening the first URL
driver.delete_all_cookies()

# Open the second URL
driver.get(url2)

# Close the browser window when done
driver.quit()
