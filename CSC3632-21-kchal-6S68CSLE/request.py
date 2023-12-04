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

response3 = session.get("http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/PKHGDNHMXH.php?solution=%27DoB,ZIP%20code,Gender,Disease\n30/08/1970,12156,M,Angina%20Pectoris%20\n17/08/1960,12154,F,Stroke\n23/08/1970,12153,M,High%20Cholesterol%20\n07/08/1970,12141,F,High%20Cholesterol%20\n20/09/1970,12143,F,Cardiomyopathy%20\n02/08/1960,12153,F,Stroke\n10/09/1960,12158,F,Angina%20Pectoris%20\n12/09/1960,12159,F,Cardiomyopathy\n02/09/1960,12147,F,Hepatitis\n04/09/1970,12152,M,Hepatitis%20\n10/08/1960,12140,F,Stroke\n05/09/1960,12145,M,Flu\n12/09/1970,12148,F,Eczema%20\n05/09/1970,12155,M,Pneumonia%20\n20/08/1960,12141,F,Stroke\n05/08/1970,12142,F,Erythema%27")
print("**RESPONSE 3**")
print(response3.text)

# Optionally, you can clear cookies after the second request if needed
session.cookies.clear()
    



