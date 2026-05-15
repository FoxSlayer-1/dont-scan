import requests
from bs4 import BeautifulSoup
import re

url = "https://www.rockpapershotgun.com/wordle-past-answers"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

text = soup.get_text()

matches = re.findall(r'\b[A-Z]{5}\b', text)

answer = matches[0] if matches else "ERROR"

with open("answer.js", "w") as f:
    f.write(f'document.getElementById("answer").innerText = "{answer}";')
