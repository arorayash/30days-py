#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import email
import imaplib

username = "arorayash.test@gmail.com"
password = "saiPHY999"

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

result, data = mail.uid("search", None, "ALL")
print(result)
print(mail.select("inbox"))

#list folders
mail.list()