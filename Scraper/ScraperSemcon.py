#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from Today import Today
import urllib2, re, json

class ScraperSemcon():
    
    def __init__(self):
        name = 'Semcon'
        url = "http://www.frontviewclub.se/guide.asp?PresentationId=11"
        dishes = []
        price = 'xxx'
        self.restaurant = { 'name': name, 'url': url, 'price': price, 'dishes': dishes }
    
    def get_text(self):
        url = self.restaurant['url'] 
        content = urllib2.urlopen(url).read()
        soup = BeautifulSoup(content)
        div = soup.find('div', attrs={'class': 'Content'})
        text = self.remove_all_tags(div.prettify())
        return text

    def remove_all_tags(self, content):
        text = []
        for line in content.split('\n'):
            line = line.strip()
            if not '<br' in line:
                text.append(line)
        return text

    def get_todays_dishes(self, text, day='Fredag'):
    #There are always two dishes at semcon
        for index, line in enumerate(text):
            if line == day:
                dishes = text[index+1:index+3]
                return dishes
        return 'no dishes found'

    def get_price(self, text):
        for line in text:
            if 'Pris' in line:
              numbers = re.findall(r'\d+', line) 
              price = numbers[0]
              return price
        return 'xxx'

    def get_dishes(self):
        today = Today()
        day = today.get_swe()
        text = self.get_text()
        self.restaurant['price'] = self.get_price(text)
        self.restaurant['dishes'] = self.get_todays_dishes(text,day)
        return self.restaurant

if __name__ == "__main__":
    scraper = ScraperSemcon()
    semcon_dishes = scraper.get_dishes()
    print json.dumps(semcon_dishes) 
