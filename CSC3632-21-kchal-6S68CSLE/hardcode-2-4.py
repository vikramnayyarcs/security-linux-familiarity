import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
import time

base_url = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"

while True:
    # Make initial request to get the K-anonymity value
    response_1 = requests.get(base_url)
    soup_1 = BeautifulSoup(response_1.text, 'html.parser')

    # Find the K-anonymity value directly from the <p> element
    k_anonymity_element = soup_1.find('p', text=lambda text: 'k-anonymity equal to:' in text)

    k_anonymity_target = 1
    # Check if k_anonymity_element is not None before accessing its attributes
    if k_anonymity_element:
        # Extract the K-anonymity value from the element's text
        k_anonymity_target = int(''.join(filter(str.isdigit, k_anonymity_element.text)))

        if k_anonymity_target == 2: 
            url_2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastThreeDigitZIP=on"
            response_2 = requests.get(url_2)

            print(response_2.text)

            response_2.cookies.clear()

        elif k_anonymity_target == 4: 
            url_2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastThreeDigitZIP=on&hideGender=on "
    
            response_2 = requests.get(url_2)

            print(response_2.text)

            response_2.cookies.clear()