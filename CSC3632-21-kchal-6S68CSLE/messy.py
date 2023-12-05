import requests
import re
import json

# Make a session object
session = requests.Session()

# Define the URLs
url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideYearDoB=on&hideLastDigitZIP=on&hideLastThreeDigitZIP=on&hideLastFourDigitZIP=on&hideLastFiveDigitZIP=on"

# Make the first request and store cookies in the session
response1 = session.get(url1)

# Make the second request using the same session
response2 = session.get(url2)

# Extract data_csv from response2.text using regex
match = re.search(r'let data_csv = "(.*?)";', response2.text)
if match:
    data_csv = match.group(1)

    # Parse data_csv in Python
    data_list = [row.split(',') for row in data_csv.split('\n') if row]
    headers = data_list[0]
    data_rows = [dict(zip(headers, row)) for row in data_list[1:]]

    # Now you can use data_rows in your Python script
    print(data_rows)
else:
    print("data_csv not found in response2.text")

# URL3 Processing
url3 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/PKHGDNHMXH.php?solution=DoB,ZIP code,Gender,Disease\\n**/**/1960,121**,F,Cardiomyopathy\\n**/**/1970,121**,F,Cardiomyopathy \\n**/**/1970,121**,M,High Cholesterol \\n**/**/1970,121**,M,Pneumonia \\n**/**/1960,121**,F,Stroke\\n**/**/1960,121**,M,Flu\\n**/**/1960,121**,F,Hepatitis\\n**/**/1970,121**,F,Erythema \\n**/**/1970,121**,M,Hepatitis \\n**/**/1960,121**,F,Angina Pectoris \\n**/**/1970,121**,F,High Cholesterol \\n**/**/1960,121**,F,Stroke\\n**/**/1960,121**,F,Stroke\\n**/**/1960,121**,F,Stroke\\n**/**/1970,121**,M,Angina Pectoris \\n**/**/1970,121**,F,Eczema"

# Make the third request using the same session
response3 = session.get(url3)
print("**RESPONSE 3**")
print(response3.text)
print("Response 3 Status Code:", response3.status_code)

# Optionally, you can clear cookies after the second request if needed
session.cookies.clear()
