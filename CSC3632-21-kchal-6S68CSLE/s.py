import requests
from py_mini_racer import py_mini_racer

# Make a session object
session = requests.Session()

# Define the URLs
url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastTwoDigitZIP=on"

# Make the first request and store cookies in the session
response1 = session.get(url1)

# Extract the relevant JavaScript code from the HTML response
script_code = response1.text.split('<script>', 1)[1].split('</script>', 1)[0]

# Execute the JavaScript code using PyMiniRacer
js_engine = py_mini_racer.MiniRacer()
result = js_engine.execute(script_code)

# Print the result (if needed)
print(result)

# Make the second request using the same session
response2 = session.get(url2)

# Print the content of the second response
print(response2.text)

# Optionally, you can clear cookies after the second request if needed
session.cookies.clear()
