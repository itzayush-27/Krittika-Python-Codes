import pandas as pd
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://krittikaiitb.github.io/team/').text
soup = BeautifulSoup(html_text , 'lxml')
yr = soup.find_all('img' , class_ = 'card-img-top')
names = soup.find_all('h5', class_='card-title mb-0')
positions = soup.find_all('p' , class_='card-text')
y = []
nme = []
pstn = []

for name in names:
    nme.append(name.text)

for position in positions:
    pstn.append(position.text)

for year in yr:
    y.append(year['src'])

df = pd.DataFrame(list(zip(nme, pstn)), columns=["Name", "Designation"])
df['Year'] = '0'

i=0
print()
for years in y:
    if years[13] == '2':
       df.loc[i]['Year'] = '2022'
    elif years[13]=='1':
       df.loc[i]['Year']= '2021'
    elif years[13]=='0':
        df.loc[i]['Year'] = '2020'
    elif years[13]=='9':
        df.loc[i]['Year'] = '2019'
    i=i+1
df.to_csv("Krittika.csv" , index = False)