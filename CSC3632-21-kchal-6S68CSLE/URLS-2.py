import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import time

# URL to visit
url_1 = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
url_2_base = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php"

# Target K-anonymity value
target_k_anonymity = 1  # You can set your target value here

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
            'hideLastThreeDigitZIP',
            'hideLastFourDigitZIP',
            'hideLastTwoDigitZIP',
            'hideLastDigitZIP',
            'hideLastFiveDigitZIP',
            'hideDayDoB',
            'hideYearDoB',
        ]

        # Try different combinations of modifiers to achieve the target K-anonymity
        for i in range(2**len(options)):
            url_2_params = {options[j]: 'on' if (i & (1 << j)) != 0 else 'off' for j in range(len(options))}

            # Remove parameters with value 'off'
            url_2_params = {key: value for key, value in url_2_params.items() if value == 'on'}

            # URL 2 with parameters
            url_2 = f"{url_2_base}?{urlencode(url_2_params)}"

            # Make a request to URL 2
            response_2 = requests.get(url_2)

            # Check if K-anonymity meets the target
            if 'flag' in response_2.text and k_anonymity_target == target_k_anonymity:
                print("Flag found! Exiting.")
                exit()

            # Print the attempt for debugging
            print(f"Attempted URL 2: {url_2}, K-anonymity: {k_anonymity_target}")

            # Clear cookies
            response_2.cookies.clear()

        print(f"No successful attempt for K-anonymity {k_anonymity_target}. Retrying...")
    else:
        print("K-anonymity element not found. Check the HTML structure.")

    # Wait for 1 second before the next attempt
