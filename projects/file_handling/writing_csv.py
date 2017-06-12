#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import csv

with open("data.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Col 1", "Col 2", "Col 3"])
    writer.writerow(["item1", "item2", "item3"])

#print(open(os.getcwd() + "/data.csv").read())

with open("data.csv", "r+") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv", "a+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Item4", "Item5"])
    
with open("data.csv", "r+") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        
with open("data.csv", "a") as csvfile:
    fieldnames = ["ABC", "PQR"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({"ABC": 123, "PQR": 456})
    
with open("data.csv", "a") as csvfile:
    fieldnames = ["Head1", "Head2"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Head1": "Apples", "Head2": "Mangoes"})