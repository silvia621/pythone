import urllib.request
from bs4 import BeautifulSoup
import requests

address = 'https://www.comuni-italiani.it/index.html'
response = urllib.request.urlopen(address) #leggere i dati dell'url
theBytes = response.read() #il metodo read() traduce in byte i dati dell'url
html = theBytes.decode(encoding = 'iso-8859-1') #trasformo i dati testuali in una stringa

doc = BeautifulSoup(html, "html.parser")
links = doc.find_all('a', href = True) #cerco tutti i tag 'a href'
lista_link_nf = [] #creo una lista con i link presenti nella pagina web
for link in links :
    href = link.get('href') #prendo l'URL associato a ciascun href
    if href != None : #escludo i risultati None
        url = urllib.request.urljoin(address, href)
    try:
        response = requests.get(url)
        if response.status_code != 200 :
            lista_link_nf.append(url)
    except: pass
print(f"I link non funzionanti sono: {lista_link_nf}")