import requests

# Make a session object
session = requests.Session()

# Define the URLs
url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastTwoDigitZIP=on"

# Make the first request and store cookies in the session
response1 = session.get(url1)

# Make the second request using the same session
response2 = session.get(url2)

# Print the content of the second response
print(response2.text)

# Optionally, you can clear cookies after the second request if needed
session.cookies.clear()

session2 = requests.Session() 

# Define the URLs
url3 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideMonthDoB=on&hideLastDigitZIP=on"

# Make the first request and store cookies in the session
response3 = session.get(url1)

# Make the second request using the same session
response4 = session.get(url3)

# Print the content of the second response
print(response4.text)

# Optionally, you can clear cookies after the second request if needed
session.cookies.clear()


