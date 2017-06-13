#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, csv
from bs4 import BeautifulSoup

def beautify(text):
    return text.strip(" \n\t\r").encode('utf-8')

def scrap():
    url = "http://www.sansfrancis.co/"
    res = requests.get(url)
    res_feeds = BeautifulSoup(res.text, "html.parser")
    feed_list = []
    for feed in res_feeds.findAll("div", {"class": "resource"}):
        title = beautify(feed.findAll("h3")[0].text).replace(" ", '')
        link = feed.findAll('a')[0]["href"]
        desc = beautify(feed.find('p', {"class":"resourceDescription"}).text)
        feedDict = {
                "title":title,
                "link":link,
                "desc":desc
                }
        feed_list.append(feedDict)
    return feed_list

        
def makefile(feeddb):
    filename = "db.csv"
    fieldnames = ["id", "title", "link", "description"]
    i = 0
    with open(filename, "w+") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        for feed in feeddb:
            i += 1
            writer.writerow({
                    "id": i,
                    "title": feed["title"],
                    "link": feed["link"],
                    "description": feed["desc"]
            })
            
db = scrap()
makefile(db)

    
