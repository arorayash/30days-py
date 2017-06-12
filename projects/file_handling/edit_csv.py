#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile

file_name = "data2.csv"

def read_data(user_id=None):
    filename = "data2.csv"
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        unknown_user_id = None
        for row in reader:
            if user_id is not None:
                if int(user_id) == int(row.get("id")):
                    return row
                else:
                    unknown_user_id = user_id
        
        if unknown_user_id is not None:
            return "User id {user_id} not found".format(user_id=user_id)
    return None

print(read_data(4))
    

def get_id(file_path):
    with open("data2.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

def append(file_path, name, email):
    fieldnames = ["id", "name", "email", "amount", "sent", "date"]
    id_no = get_id(file_path)
    with open(file_path, "a+") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
                "id": id_no,
                "name": name,
                "email": email
                })

#append("data2.csv", "Mandy", "xoxo.gmail.com")

def edit_data(edit_id=None, email=None, amount=None, sent=None):
    filename = "data2.csv"
    tempfile = NamedTemporaryFile(delete=False)
    
    with open(filename, "rb") as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        fieldnames = ["id", "name", "email", "amount", "sent", "date"]
        writer = csv.DictWriter(tempfile, fieldnames)
        writer.writeheader()
        for row in reader:
            if edit_id is not None:
                #print(row)
                if int(row["id"]) == edit_id:
                    row["amount"] = amount
                    row["sent"] = sent
                    row["email"] = email
                    row["date"] = datetime.datetime.now()
            writer.writerow(row)
        shutil.move(tempfile.name, file_name)
        return True
    return False

edit_data(email="wayme@gmail.com", edit_id=2)

