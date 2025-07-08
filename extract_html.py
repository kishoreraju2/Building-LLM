import urllib.request
from bs4 import BeautifulSoup

url = "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0153.html"
html = urllib.request.urlopen(url).read()
file_path = "thirukkural.txt"
soup = BeautifulSoup(html, "html.parser")
plain_text = soup.get_text()
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(plain_text)
