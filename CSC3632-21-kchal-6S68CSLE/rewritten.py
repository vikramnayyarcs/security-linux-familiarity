import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from itertools import product
from concurrent.futures import ThreadPoolExecutor

while True:
    base_url = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"

    #Make the initial request.
    response_1 = requests.get(base_url)
    soup_1 = BeautifulSoup(response_1.text, 'html.parser')

    k_anonymity_element = soup_1.find('p', text=lambda text: 'k-anonymity equal to:' in text)

    response_1.cookies.clear()
    response_1.close()

    #Work out what we need to work towards.
    if k_anonymity_element:
        k_anonymity_target = int(''.join(filter(str.isdigit, k_anonymity_element.text)))

        if k_anonymity_target == 4:
            url_2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideDayDoB=on&hideLastThreeDigitZIP=on"

            response_2 = requests.get(url_2)

            print(response_2.text)

            response_2.cookies.clear()
            response_2.close()

