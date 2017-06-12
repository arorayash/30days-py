#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import csv

def get_id(file_path):
    with open("data.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append(file_path, name, email):
    fieldnames = ["id", "name", "email"]
    id_no = get_id(file_path)
    with open(file_path, "a+") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
                "id": id_no,
                "name": name,
                "email": email
                })

append("data.csv", "Mandy", "xoxo.gmail.com")