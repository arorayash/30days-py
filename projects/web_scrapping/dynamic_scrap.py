#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os, shutil

url = "https://dribbble.com/"

req = requests.get(url)
web_soup = BeautifulSoup(req.text, "html.parser")
#firefox_capabilities = DesiredCapabilities.FIREFOX
#firefox_capabilities['marionette'] = True

driver = webdriver.Firefox();
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, "html.parser")

images = []
for img in sel_soup.find_all("img"):
    src = ["src"]
    images.append(src)
    
current_path = os.getcwd()
for img in images:
    file_name = os.path.basename(img)
    img_requested = requests.get(img)
    new_path = os.path.join(current_path, file_name)
    with open(new_path, "wb") as output_file:
        shutil.copyfileobj(img_requested.raw, output_file)
    del img_requested 