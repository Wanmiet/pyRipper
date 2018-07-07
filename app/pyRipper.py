from bs4 import BeautifulSoup
import requests 

user_input = input("Enter your website: ")
url = user_input
r = requests.get(url)

html = r.text
soup = BeautifulSoup(html, 'html.parser')
body = soup.body

for url in soup.find_all('img'):
	print(url.get('src'))