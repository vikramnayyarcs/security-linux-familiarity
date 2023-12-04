import requests
from itertools import product

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

# URL to test
base_url = "http://10.0.0.5/ctf_deploy2/kchal/Clyhbjgi/JGWPPWTCHR.php"

# Set flag condition
flag_condition = 'flag'

while True:
    # Generate all possible combinations of options
    combinations = list(product(['on', ''], repeat=len(options)))

    # Iterate through combinations
    for combo in combinations:
        # Construct the URL with the current combination
        query_params = "&".join(f"{option}={state}" for option, state in zip(options, combo))
        full_url = f"{base_url}?{query_params}"

        # Make the request
        response = requests.get(full_url)

        # Log the response
        print(f"URL: {full_url}")
        print(f"Response: {response.status_code}")
        print(f"Content: {response.text}")
        print()

        # Clear cookies (PHPSESSIONID)
        response.cookies.clear()

        # Check for the flag in the response text
        if flag_condition in response.text:
            print("Flag found! Exiting.")
            exit()

    # Add your code here to close the web page if needed
