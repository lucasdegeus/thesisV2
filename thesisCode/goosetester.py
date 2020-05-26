import requests
import justext
from bs4 import BeautifulSoup
response = requests.get("https://www.snap.com/en-US/privacy/privacy-policy")
paragraphs = justext.justext(response.content, justext.get_stoplist('English'))
returningParagraphs = list()
for item in paragraphs:
    returningParagraphs.append(item.text)

cleantext = BeautifulSoup(returningParagraphs, "lxml").text
print(cleantext)