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

# Find the line containing "Select a combination of modifiers so that the resulting table has a k-anonymity equal to:"
target_line = soup.find('div', text=lambda text: 'Select a combination of modifiers so that the resulting table has a k-anonymity equal to:' in text)
k_anonymity_line = target_line.find_next('p').text

# Extract the K-anonymity value from the line
k_anonymity = int('
