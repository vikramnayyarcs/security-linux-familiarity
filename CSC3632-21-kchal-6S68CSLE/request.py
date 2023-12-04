import requests


# then make a url variable
url1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastTwoDigitZIP=on"

request_1 = requests.get(url1)

request_2 = requests.get(url2)

print(request_2.text)

request_2.cookies.clear()