#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from Today import Today
import urllib2, re, json

class ScraperMimolett():

    def __init__(self):
        name = 'Mimolett'
        url = "http://www.mimolett.se/dagens-lunch/"
        dishes = []
        price = 'xxx'
        self.restaurant = { 'name': name, 'url': url, 'price': price, 'dishes': dishes }

    def get_text(self):
        url = self.restaurant['url'] 
        content = urllib2.urlopen(url).read()
        soup = BeautifulSoup(content)
        div = soup.find('div', attrs={'class': 'entry'})
        for e in div.findAll('br'):
            e.replaceWith('newline')
        text = []
        paras = [x for x in div.findAllNext('p')]
        for p in paras:
            line = p.text
            line = line.strip()
            for l in line.split('newline'):
                text.append(l)
        return text

    def get_todays_dishes(self, text, day='Fredag'):
    #There are always two dishes at mimolett
        for index, elem in enumerate(text):
            if elem == day:
                dishes = text[index+1:index+3]
                return dishes
        return 'no dishes found'

    def get_pasta(self, text):
        for index, elem in enumerate(text):
            if 'VALFRI DAGENS PASTAR' in elem:
                pasta_dishes = text[index+1:]
                return pasta_dishes
    
    def get_price(self, text):
        for line in text:
            if 'DAGENS LUNCH' in line:
              numbers = re.findall(r'\d+', line) 
              price = numbers[0]
              return price
        return 'xxx'
    
    def get_dishes(self):
        dishes = []
        text = self.get_text()
        today = Today()
        day = today.get_swe()
        todays_dishes = scraper.get_todays_dishes(text, day)
        pasta_dishes = scraper.get_pasta(text)
        dishes.extend(todays_dishes)
        dishes.extend(pasta_dishes)
        self.restaurant['dishes'] = dishes 
        self.restaurant['price'] = self.get_price(text)
        return self.restaurant

if __name__ == "__main__":
    scraper = ScraperMimolett()
    mimolett_dishes = scraper.get_dishes()
    print mimolett_dishes
    print json.dumps(mimolett_dishes)    
