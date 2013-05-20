#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import urllib2

class ScraperLindholmen():

    def get_all_classes(self):
	url="http://www.lindholmen.se/sv/restaurang/kooperativet"
	content = urllib2.urlopen(url).read()
        soup = BeautifulSoup(content)
	html_classes = soup.findAll('td', attrs={'class':'views-field views-field-title active'})
	return html_classes

    def get_dishes_from_classes(self, html_classes):
	dishes = []
	for elem in html_classes:
	    all_text =  html_classes.getText()
	    strong_text = html_classes.find('strong').getText()		   
	    description_text = all_text[len(strong_text):]
	    dishes.append(description_text) 
        return dishes

class Dishes():

    def __init__(self):
	self.dishes = None

    def dump(self):
        for dish in self.dishes :
            print dish

    def set(self, dishes):
	self.dishes = dishes 


if __name__ == "__main__":
    scraper = ScraperLindholmen()
    html_classes = scraper.get_all_classes()
    lindholmen_dishes = scraper.get_dishes_from_classes(html_classes)
    dishes = Dishes()
    dishes.set(lindholmen_dishes)
    dishes.dump()

