from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml') 
job = soup.find('li', class_="clearfix job-bx wht-shd-bx")
compagny_name = job.find('h3', class_='joblist-comp-name').text.strip()
all_skills = job.find('div', class_='more-skills-sections').find_all('span')
skills = [x.text.strip() for x in all_skills]
for x in skills:
    if skills[-1] != x: print(x, ",", end="")
    else: print(x)