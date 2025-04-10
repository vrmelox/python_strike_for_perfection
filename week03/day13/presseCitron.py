from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.presse-citron.net/').text
soup = BeautifulSoup(html_text, 'lxml')
main = soup.find('main', id="main")
articles = main.find_all('article')
presseCitron = []
for article in articles:
    latest_news = {}
    latest_news["title"] = article.find('h2').text.strip()
    latest_news["category"] = article.find('span', 'uppercase font-bold').text.strip()
    latest_news["time"] = article.find('time').text.split("Il y a")[-1].strip()
    latest_news["link"] = article.a['href'].strip()
    latest_news["resume"] = article.find('p').text.strip()
    presseCitron.append(latest_news)
for x in presseCitron:
    print(f"""
Titre : {x["title"]}\nCatégorie : {x["category"]}\nDepuis : {x["time"]}\nLien : {x["link"]}\nRésumé: {x["resume"]}\n\n""")