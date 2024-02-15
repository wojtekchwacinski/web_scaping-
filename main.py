import requests
from bs4 import BeautifulSoup
import csv


def kraje():
    same_kraje = []
    kraje = soup.findAll('h3')

    for kraj in kraje:
        kraj_bez_spacji_na_poczatku = kraj.text.lstrip()
        kraj_bez_spacji_na_koncu = kraj_bez_spacji_na_poczatku.rstrip()
        kraj_bez_spacji_na_koncu = kraj_bez_spacji_na_koncu.replace(" ", "_")
        same_kraje.append(kraj_bez_spacji_na_koncu)

    return same_kraje


def informacje(kraje):
    label_info = soup.findAll('strong')
    info = soup.findAll('span')
    #print(info)
    storage = {}
    x = 0
    f = 0
    for i, l in zip(label_info, info):
        #print(i.text, l.text)
        if kraje[x] in storage:
            storage[kraje[x]].extend([i.text, l.text])
        else:
            storage[kraje[x]] = [i.text, l.text]

        if (f + 1) % 3 == 0:
            x = x + 1
        f = f + 1

    return storage

if __name__ == '__main__':
    url = 'https://www.scrapethissite.com/pages/simple/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    csv_file = 'wszystkie_kraje_swiat.csv'


    countries = kraje()
    info = informacje(countries)

    plik_csv = open(csv_file, mode='w',  encoding='utf-8', newline='')
    # tu bedzie się róznić w zalezności od tego gdzie
    #chemy otwierać plik gdy w exccelu to musmy ustwic rozdielannie na ";"
    #a gdy w libra office to ","
    #excel
    writer = csv.writer(plik_csv, delimiter=';')
    #libre office
    #writer = csv.writer(plik_csv, delimiter=',')

    writer.writerow(["Kraj", "Info"])

    for i in countries:
        print(i)
        print(info[i])
        writer.writerow([i, info[i]])

    plik_csv.close()




