import requests

url = "http://10.0.0.5/ctf_deploy2/hijack/z422spDc/add_comments.php"
payload = {"msg": "SCRIPT"}

response = requests.post(url, data=payload)

print(response.text)
