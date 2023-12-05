import requests

# Make a session object
session = requests.Session()

# Define the URLs
url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideYearDoB=on&hideLastDigitZIP=on&hideLastThreeDigitZIP=on&hideLastFourDigitZIP=on&hideLastFiveDigitZIP=on"
# url3 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/PKHGDNHMXH.php?solution='DoB,ZIP code,Gender,Disease\\n12/09/1960,12159,F,Cardiomyopathy\\n20/09/1970,12143,F,Cardiomyopathy \\n23/08/1970,12153,M,High Cholesterol \\n05/09/1970,12155,M,Pneumonia \\n10/08/1960,12140,F,Stroke\\n05/09/1960,12145,M,Flu\\n02/09/1960,12147,F,Hepatitis\\n05/08/1970,12142,F,Erythema \\n04/09/1970,12152,M,Hepatitis \\n10/09/1960,12158,F,Angina Pectoris \\n07/08/1970,12141,F,High Cholesterol \\n17/08/1960,12154,F,Stroke\\n02/08/1960,12153,F,Stroke\\n20/08/1960,12141,F,Stroke\\n30/08/1970,12156,M,Angina Pectoris \\n12/09/1970,12148,F,Eczema'"
url3 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/PKHGDNHMXH.php?solution='DoB,ZIP code,Gender,Disease\\n**/**/1960,121**,F,Cardiomyopathy\\n**/**/1970,121**,F,Cardiomyopathy \\n**/**/1970,121**,M,High Cholesterol \\n**/**/1970,121**,M,Pneumonia \\n**/**/1960,121**,F,Stroke\\n**/**/1960,121**,M,Flu\\n**/**/1960,121**,F,Hepatitis\\n**/**/1970,121**,F,Erythema \\n**/**/1970,121**,M,Hepatitis \\n**/**/1960,121**,F,Angina Pectoris \\n**/**/1970,121**,F,High Cholesterol \\n**/**/1960,121**,F,Stroke\\n**/**/1960,121**,F,Stroke\\n**/**/1960,121**,F,Stroke\\n**/**/1970,121**,M,Angina Pectoris \\n**/**/1970,121**,F,Eczema'"
#


# Make the first request and store cookies in the session
response1 = session.get(url1)

# Make the second request using the same session
response2 = session.get(url2)

# Print the content of the second response
print(response2.text)

response3 = session.get(url3)
print("**RESPONSE 3**")
print(response3.text)
print("Response 3 Status Code:", response3.status_code)

# Optionally, you can clear cookies after the second request if needed
session.cookies.clear()