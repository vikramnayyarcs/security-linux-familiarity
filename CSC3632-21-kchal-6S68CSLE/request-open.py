import mechanize

# Make a Browser object
br = mechanize.Browser()

# Define the URLs
url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideYearDoB=on&hideLastDigitZIP=on&hideLastThreeDigitZIP=on&hideLastFourDigitZIP=on&hideLastFiveDigitZIP=on"
url3 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/PKHGDNHMXH.php?solution=%27DoB,ZIP%20code,Gender,Disease\n**/09/****,*****,M,Flu\n**/09/****,*****,F,Angina%20Pectoris%20\n**/08/****,*****,F,Stroke\n**/08/****,*****,F,Erythema%20\n**/08/****,*****,M,Angina%20Pectoris%20\n**/08/****,*****,M,Stroke\n**/08/****,*****,M,High%20Cholesterol%20\n**/09/****,*****,F,Cardiomyopathy\n**/09/****,*****,F,Cardiomyopathy%20\n**/08/****,*****,M,Stroke\n**/09/****,*****,F,Eczema%20\n**/09/****,*****,M,Pneumonia%20\n**/08/****,*****,F,High%20Cholesterol%20\n**/08/****,*****,F,Stroke\n**/09/****,*****,M,Hepatitis\n**/09/****,*****,M,Hepatitis%27"

# Make the first request
br.open(url1)

# Make the second request
br.open(url2)

# Make the third request
br.open(url3)

# Print the content of the third response
print("**RESPONSE 3**")
print(br.response().read())
