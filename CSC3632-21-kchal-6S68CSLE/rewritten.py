import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from itertools import product
from concurrent.futures import ThreadPoolExecutor

#All in 1 second.

#Go to the first page.
base_url = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
response = requests.get(base_url)

soup_1 = BeautifulSoup(response.text, 'html.parser')

k_anonymity_element = soup_1.find('p', text=lambda text: 'k-anonymity equal to:' in text)

k_anonymity_target = 0

#Scrape the desired k anonymity.
if k_anonymity_element:
    # Extract the K-anonymity value from the element's text
    k_anonymity_target = int(''.join(filter(str.isdigit, k_anonymity_element.text)))

#Use one of the hardcoded results here:
hardcoded_ks = {
    # 1: "",
    2: "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastThreeDigitZIP=on",
    # 3: "",
    4: "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastThreeDigitZIP=on&hideGender=on",
    # 5: "",
}