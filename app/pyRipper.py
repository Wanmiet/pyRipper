from bs4 import BeautifulSoup
import requests, random
import urllib.request

print("Welcome to pyRipper by Wanmiet.")


def get_links():
	user_input = input("Enter your website: ")
	url = user_input
	r = requests.get(url)

	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
	body = soup.body

	for url in soup.find_all('img'):
		print(url.get('src'))


def dl_images():
	url = input("Enter image link: ")
	name = random.randrange(1, 100000)
	full_name = str(name) + ".jpg"
	dld = urllib.request.urlretrieve(url, full_name)

print('\n')
while True:
	u_i = input("1 - Download image links 2 - Download images 3 - Exit. ")
	if u_i == "1":
		get_links()
	elif u_i == "2":
		dl_images()
	elif u_i == "3":
		break
	else:
		print("Command not recognized. Try again.")
