import requests

# Make a session object
session = requests.Session()

# Define the URLs
url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?"
url_when_2 = "PKHGDNHMXH.php?solution='DoB,ZIP code,Gender,Disease\n05/09/1970,94155,M,Pneumonia \n02/08/1960,94153,F,Stroke\n02/09/1970,94152,M,Hepatitis \n12/09/1970,94148,F,Eczema \n05/08/1970,94142,F,Erythema \n10/09/1960,94158,F,Angina Pectoris \n05/09/1960,94145,M,Flu\n02/09/1960,94147,M,Hepatitis\n10/08/1960,94140,M,Stroke\n01/08/1960,94154,F,Stroke\n20/09/1970,94143,F,Cardiomyopathy \n30/08/1970,94156,M,Angina Pectoris \n07/08/1970,94141,F,High Cholesterol \n20/08/1960,94141,M,Stroke\n25/08/1970,94153,M,High Cholesterol \n30/09/1960,94159,F,Cardiomyopathy'"

# Make the first request and store cookies in the session
response1 = session.get(url1)

# Make the second request using the same session
response2 = session.get(url2+url_when_2)

# Print the content of the second response
print(response2.text)

# Optionally, you can clear cookies after the second request if needed
session.cookies.clear()

