import requests  # requires the excellent requests library `pip install requests`

headers = {'Accept': 'text/plain'}
response = requests.get("http://www.codingexcuses.com", headers=headers)

print response.content
