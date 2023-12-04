import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from itertools import product
from concurrent.futures import ThreadPoolExecutor

# Function to make a request and check K-anonymity
def check_k_anonymity(params):
    base_url = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php"
    full_url = f"{base_url}?{urlencode(params)}"
    response = requests.get(full_url)

    # Log the attempt
    print(f"Attempted URL: {full_url}")
    print(f"Response: {response.status_code}")
    print(f"Content: {response.text}")
    print()

    # Clear cookies (PHPSESSIONID)
    response.cookies.clear()

    # Check if 'flag' is in the response text
    if 'flag' in response.text:
        print("Flag found! Exiting.")
        exit()

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
    k_anonymity = int(''.join(filter(str.isdigit, k_anonymity_element.text)))

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

    # Use ThreadPoolExecutor to parallelize requests
    with ThreadPoolExecutor(max_workers=10) as executor:  # You can adjust the number of max workers as needed
        # Generate all possible combinations of options
        combinations = list(product(['on', ''], repeat=len(options)))

        # Submit tasks to the executor
        executor.map(check_k_anonymity, [{option: state for option, state in zip(options, combo)} for combo in combinations])

    # Add your code here to close the web page if needed
    print(f"No successful attempt for K-anonymity {k_anonymity}. Retrying...")
else:
    print("K-anonymity element not found. Check the HTML structure.")
