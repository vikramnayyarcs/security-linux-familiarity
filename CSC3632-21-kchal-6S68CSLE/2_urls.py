import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
import time

# Function to make a request and check K-anonymity
def check_k_anonymity(params, k_anonymity_target):
    base_url = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
    full_url = f"{base_url}?{urlencode(params)}"
    response = requests.get(full_url)

    # Log the attempt to a file
    with open('log.txt', 'a') as log_file:
        log_file.write(f"Attempted URL: {full_url}\n")
        log_file.write(f"Response: {response.status_code}\n")
        log_file.write(f"Content: {response.text}\n\n")

    # Check if 'flag' is in the response text
    if 'flag' in response.text:
        print("Flag found! Exiting.")
        exit()

    # Clear cookies
    response.cookies.clear()

    # Close the webpage
    response.close()

# URL to visit
url_1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"

while True:
    # Make initial request to get the K-anonymity value
    response_1 = requests.get(url_1)
    soup_1 = BeautifulSoup(response_1.text, 'html.parser')

    # Find the K-anonymity value directly from the <p> element
    k_anonymity_element = soup_1.find('p', text=lambda text: 'k-anonymity equal to:' in text)

    # Check if k_anonymity_element is not None before accessing its attributes
    if k_anonymity_element:
        # Extract the K-anonymity value from the element's text
        k_anonymity_target = int(''.join(filter(str.isdigit, k_anonymity_element.text)))

        # List of options for URL 2
        options = [
            'hideMonthDoB',
            'hideGender',
            # 'hideLastThreeDigitZIP',
            # 'hideLastFourDigitZIP',
            # 'hideLastTwoDigitZIP',
            'hideLastDigitZIP',
            'hideLastFiveDigitZIP',
            'hideDayDoB',
            # 'hideYearDoB',

        ]

        # URL 2 with parameters
        # url_2 = f"http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php?{urlencode(url_2_params)}"
        
        #Always 2:
        url_2 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php?hideMonthDoB=on&hideDayDoB=on&hideLastFiveDigitZIP=on&hideGender=on"


        # Send a request to URL 2 with ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=1) as executor:
            executor.submit(check_k_anonymity, {}, k_anonymity_target)

        print(f"No successful attempt for K-anonymity {k_anonymity_target}. Retrying...")
    else:
        print("K-anonymity element not found. Check the HTML structure.")

    # Wait for 1 second before the next attempt
    time.sleep(1)
