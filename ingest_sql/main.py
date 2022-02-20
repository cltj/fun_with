from datetime import datetime
import requests
import pandas as pd
import bs4
from pydantic import BaseModel
import time

# # # # # # # # # # # # # # # # # #
#  CONFIG
# # # # # # # # # # # # # # # # # #

class user(BaseModel):
    id: int
    name: str
    updated: datetime


def get_apple_store_data(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, 'html.parser')

    if r.status_code == 404:
        return r.status_code

    keys_list = []
    values_list = []

    # Finds and extract values
    info_divs = soup.find(name='dl', attrs={'class': lambda string: 'information-list' in string})

    for element in info_divs.contents:
        if element.name == 'div':
            for content in element.contents:
                if content.name == 'dt':
                    key = content.text.strip()
                    k1 = key.replace(' ','_')
                    k2 = k1.replace('-','_')
                    keys_list.append(k2.lower())
                if content.name =='dd':
                    value = content.text.strip()
                    values_list.append(value)
                else:
                    pass

    zip_iterator = zip(keys_list, values_list)
    dictionary = dict(zip_iterator) # creates a dict of what was found
    dictionary.pop("copyright") # Removes copyright value
    dictionary["currency"] = 'kr' # Adds currency

    if "in_app_purchases" in dictionary: # Format fields in dict
        dictionary.update({"in_app_purchases":True})
    else:
        dictionary.update({"in_app_purchases":False}) # Betyr at det ikke er listet på store siden, men ikke at det ikke finnes

    for elem in dictionary:
        if elem == 'size':
            x = dictionary['size']
            if 'MB' in x:
                x1 = x.replace('MB','')
                x2 = x1.replace(' ','')
                x3 = float(x2)
                dictionary.update({elem:x3})
            elif 'GB' in x:
                x1 = x.replace('GB','')
                x2 = x1.replace(' ','')
                x3 = x2.replace('.','')
                x4 = x3 * 1000
                x5 = float(x4)
                dictionary.update({elem:x5})
        elif elem == 'compatibility':
            x = dictionary['compatibility']
            x1 = x.replace(' ','')
            x2 = x1.replace('\n','')
            x3 = x2.replace('Requires','')
            x4 = x3.replace('orlater','')
            x5 = x4.replace('iPhoneiOS',' iPhone: ')
            x6 = x5.replace('iPadiPadOS',' iPad: ')
            x7 = x6.replace('iPod\xa0touchiOS',' iPod: ')
            x8 = x7.replace('MacmacOS',' macOS: ')
            x9 = x8.replace('andaMacwiththe',' and ')
            dictionary.update({elem:x9})
        elif elem == 'age_rating':
            x = dictionary['age_rating']
            x1 = x[:2]
            x2 = x1.replace('+','')
            x3 = int(x2)
            dictionary.update({elem:x3})
        elif elem == 'price':
            x = dictionary['price']
            x1 = x.replace('Free','0.0')
            x2 = x1.replace(',','.')
            x3 = x2.replace('\xa0','')
            x4 = x3.replace('kr','')
            x5 = float(x4)
            dictionary.update({elem:x5})
        else:
            pass

    # Get and adds external urls to dict
    external_urls = soup.find(name='ul', attrs={'class': lambda string: 'inline-list--app-extensions' in string})
    for item in external_urls:
        if item.name == 'li':
            for e in item.contents:
                if e.name == 'a':
                    e_url = e.attrs
                    for i in e_url:
                        if i == 'href':
                            a_url = e_url.get('href')
                    n = str(e.next.strip())
                    n1 = n.replace(' ','_')
                    dictionary.update({n1.lower():a_url})

    return dictionary


def main():
    url = "https://apps.apple.com/no/app/musescore-sheet-music/id835731296"
    x = get_apple_store_data(url)
    print(x)


if __name__ == "__main__":
    main()