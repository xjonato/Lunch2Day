#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import datetime

class Today():
    def __init__(self):
        self.days = {
                 'Monday': 'Måndag',
                 'Tuesday': 'Tisdag',
                 'Wednesday': 'Onsdag',
                 'Thursday': 'Torsdag',
                 'Friday': 'Fredag',
                 'Saturday': 'Lördag', 
                 'Sunday': 'Söndag'
                }
    
    def get_swe(self):
        now = datetime.datetime.now()
        today = now.strftime("%A")
        today_swe = self.days[today]
        return today_swe

if __name__ == "__main__":
    today = Today()
    print today.get_swe()
