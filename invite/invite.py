import requests
from bs4 import BeautifulSoup

url = 'https://www.hackthebox.eu/api/generate/'

#_token = 'Lllq8yqoS52dcSDcnrrW14ybslIBswABtIYu1hDG'

r = requests.post(url = url)#, data = _token)

data = r.text

#soup = BeautifulSoup(data)

#prett = soup.prettify().encode('utf-8')

#print(prett)
print(r.text)