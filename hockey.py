import requests
from bs4 import BeautifulSoup
import csv







def connection_and_creation_hockey():
    url = 'https://www.scrapethissite.com/pages/forms/?page_num=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    csv_file = 'drużyny_hokejowe.csv'