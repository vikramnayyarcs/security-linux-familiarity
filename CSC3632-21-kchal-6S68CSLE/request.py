import requests

# Make a session object
session = requests.Session()

# Define the URLs
url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastThreeDigitZIP=on&hideYearDoB=on"
url3 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/PKHGDNHMXH.php?solution=%27DoB,ZIP%20code,Gender,Disease\n30/08/1970,1215*,*,Angina%20Pectoris%20\n17/08/1960,1215*,*,Stroke\n23/08/1970,1215*,*,High%20Cholesterol%20\n07/08/1970,1214*,*,High%20Cholesterol%20\n20/09/1970,1214*,*,Cardiomyopathy%20\n02/08/1960,1215*,*,Stroke\n10/09/1960,1215*,*,Angina%20Pectoris%20\n12/09/1960,1215*,*,Cardiomyopathy\n02/09/1960,1214*,*,Hepatitis\n04/09/1970,1215*,*,Hepatitis%20\n10/08/1960,1214*,*,Stroke\n05/09/1960,1215*,*,Flu\n12/09/1970,1215*,*,Eczema%20\n05/09/1970,1215*,*,Pneumonia%20\n20/08/1960,1214*,*,Stroke\n05/08/1970,1214*,*,Erythema%27"

# Make the first request and store cookies in the session
response1 = session.get(url1)

# Make the second request using the same session
response2 = session.get(url2)

# Print the content of the second response
print(response2.text)

response3 = session.get(url3)
print("**RESPONSE 3**")
print(response3.text)

# Optionally, you can clear cookies after the second request if needed
session.cookies.clear()