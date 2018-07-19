from bs4 import BeautifulSoup
import requests
import random
import urllib.request
import time
import shutil
import os

print("Welcome to pyRipper by Wanmiet.")
print('\n')

def get_links():
    user_input = input("Enter your website: ")
    url = user_input
    r = requests.get(url)
    filename = input("Enter name of txt file: ")

    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    #body = soup.body

    with open(filename + ".txt", 'w') as out:
        for url in soup.find_all('img'):
            out.write(str(url.get('src')))
    print('\n')
    print("Saved " + filename + ".txt" + " in directory.")

def dl_images():
    while True:
        url = input("Enter image link: ")
        name = random.randrange(1, 100000)
        full_name = str(name) + ".jpg"
        urllib.request.urlretrieve(url, full_name)

while True:
    u_i = input(
        "1 - Download image links 2 - Download images 3 - Exit. ")
    if u_i == "1":
        get_links()
    elif u_i == "2":
        dl_images()
    elif u_i == "3":
        print("Goodbye.")
        time.sleep(3)
        break
    else:
        print("Command not recognized. Try again.")
