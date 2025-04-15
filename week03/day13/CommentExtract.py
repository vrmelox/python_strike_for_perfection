from bs4 import BeautifulSoup
import requests
from docx import Document
from textblob import TextBlob

html_text = requests.get("https://fr.trustpilot.com/review/www.apple.fr", ).text
soup = BeautifulSoup(html_text, 'lxml')
company_name = soup.find('span', class_="typography_display-s__pKPhT typography_appearance-default__t8iAq title_displayName__9lGaz").text
commentsSection = soup.find('div', class_="styles_wrapper__Fi9KX")
articles = soup.findAll('div', class_="styles_cardWrapper__g8amG styles_show__Z8n7u")
comments = []
notesTotal = 0
for article in articles:
    person = {}
    person["name"] = article.find("span", class_="typography_heading-xs__osRhC typography_appearance-default__t8iAq").text
    person["time"] = article.find("time").text
    person["rating"] = article.find("div", class_="styles_reviewHeader__DzoAZ")["data-service-review-rating"]
    notesTotal += int(person["rating"])
    person["comment"] = article.find("p", class_=lambda c: c and "typography_body-l__v5JLj" in c).text
    comments.append(person)

tofile = ""
tofile += f"L'entreprise {company_name} dispose de {len(comments)} sur la première page de TrustPilot\n"
for x in comments:
    line = f'{x["name"]} a dit :\n{x["comment"]}\nCommentaire posté le : {x["time"]} dont une note de {x["rating"]} sur / 5\n\n'
    tofile += line

notesParfaites = len(comments) * 5

docName = "rapport_Truspilot_" + company_name
nomdocument = docName + ".docx"
docName = Document()
docName.add_heading('Rapport des retours à propos de ' + company_name + ' sur Truspilot', level=1)
docName.add_heading('Condensés de tous les commentaires sur la première page', level=2)
docName.add_paragraph(tofile)
docName.add_page_break()

docName.add_heading('Quelques analyses rapides', level=2)
docName.add_paragraph(f"Le total des notes est de {notesTotal} sur {notesParfaites}")
if ((notesParfaites / 4) > notesTotal):
    docName.add_paragraph("Les notes sont extrêmement négatives")
elif ((notesParfaites / 3) > notesTotal):
    docName.add_paragraph("Les notes sont très négatives")
elif ((notesParfaites / 2) > notesTotal):
    docName.add_paragraph("Les notes sont négatives")
else:
    docName.add_paragraph("Les notes sont positives")

pointNotes = [0] * 2
for x in comments:
    match x["rating"]:
        case 1:
            pointNotes[0] += 1
        case 2:
            pointNotes[0] += 2
        case 3:
            pointNotes[1] += 3
        case 4:
            pointNotes[1] += 4
        case 5:
            pointNotes[1] += 5
        case _:
            continue

docName.add_paragraph(f"{pointNotes[1]} personnes ont trouvé les produits de {company_name} relativement positifs")
docName.save(nomdocument)
