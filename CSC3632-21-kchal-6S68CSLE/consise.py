import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import itertools
import time

# Function to make a request and check K-anonymity
def check_k_anonymity(params, k_anonymity_target):
    base_url = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"
    full_url = f"{base_url}?{urlencode(params)}"
    
    # Make the request
    start_time = time.time()
    response = requests.get(full_url)
    elapsed_time = time.time() - start_time

    # Log the attempt to a file
    with open('log.txt', 'a') as log_file:
        log_file.write(f"Attempted URL: {full_url}\n")
        log_file.write(f"Response: {response.status_code}\n")
        log_file.write(f"Content: {response.text}\n")
        log_file.write(f"Elapsed Time: {elapsed_time} seconds\n\n")

    # Check if 'flag' is in the response text
    if 'flag' in response.text:
        flag = response.text.split('flag')[1].split('}')[0] + '}'
        print(f"Flag found: {flag}")
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Flag found: {flag}\n")
        exit()

    # Clear cookies
    response.cookies.clear()

    # Close the webpage
    response.close()

# URL to visit
url = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"

# Make initial request to get the K-anonymity value
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the K-anonymity value directly from the <p> element
k_anonymity_element = soup.find('p', text=lambda text: 'k-anonymity equal to:' in text)

# Check if k_anonymity_element is not None before accessing its attributes
if k_anonymity_element:
    # Extract the K-anonymity value from the element's text
    k_anonymity_target = int(''.join(filter(str.isdigit, k_anonymity_element.text)))
    print(f"Target K-anonymity: {k_anonymity_target}")

    # List of options
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

    # Generate all possible combinations of options with each parameter set to 'on'
    combinations = list(itertools.product(['on', 'off'], repeat=len(options)))

    # Iterate over combinations and check K-anonymity
    for combo in combinations:
        params = dict(zip(options, combo))
        check_k_anonymity(params, k_anonymity_target)

    print(f"No successful attempt for K-anonymity {k_anonymity_target}. Exiting...")
else:
    print("K-anonymity element not found. Check the HTML structure.")

# Close the initial webpage
response.close()
