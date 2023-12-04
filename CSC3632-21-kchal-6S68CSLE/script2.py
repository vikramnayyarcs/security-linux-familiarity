import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures.thread

# Function to make a request and check K-anonymity
def check_k_anonymity(params):
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

# Find the target line using a CSS selector
target_line = soup.select_one('div:contains("Select a combination of modifiers so that the resulting table has a k-anonymity equal to:")')

# Check if target_line is not None before accessing its attributes
if target_line:
    k_anonymity_line = target_line.find_next('p').text

    # Extract the K-anonymity value from the line
    k_anonymity = int(''.join(filter(str.isdigit, k_anonymity_line)))

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

    # URL for making requests
    base_url = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JTDIFDVIUX.php"

    # Continue making attempts until 'flag' is found
    while True:
        # Generate all possible combinations of options
        combinations = list(product(['on', ''], repeat=len(options)))

        # Use ThreadPoolExecutor to parallelize requests
        with ThreadPoolExecutor(max_workers=concurrent.futures.thread._threads_queues.MaxSize) as executor:
            executor.map(check_k_anonymity, [{option: state for option, state in zip(options, combo)} for combo in combinations])

        # Add your code here to close the web page if needed
        print(f"No successful attempt for K-anonymity {k_anonymity}. Retrying...")
else:
    print("Target line not found. Check the HTML structure.")
