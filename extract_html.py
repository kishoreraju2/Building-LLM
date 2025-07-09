import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://www.projectmadurai.org/pm_etexts/utf8/pmuni0153.html"
html = urllib.request.urlopen(url).read()
file_path = "thirukkural.txt"
soup = BeautifulSoup(html, "html.parser")
plain_text = soup.get_text()
# with open(file_path, 'w', encoding='utf-8') as f:
#     f.write(plain_text)

print("Total number of characters:", len(plain_text))
preprocessed = re.split(r'([,.:;?_!"()\']|\s)', plain_text)
preprocessed = [item for item in preprocessed if item.strip()]
all_words = sorted(set(preprocessed))
total_words = len(all_words)
print(total_words)

vocab = {token:integer for integer,token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break
