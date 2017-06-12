#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import datetime

class MsgUser():
    user_details = []
    messages = []
    base_msg = """ """
    
    def add_user_details(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%0.2f" %(amount)
        today = datetime.date.today()
        today_formatted = text = today.strftime('%-m/%-d/%y')
        details = {
            "name": name,
            "amount": amount,
            "date": today_formatted
        }
        if email is not None:
            details["email"] = email
        self.user_details.append(details)
     
    def get_user_details(self):
        return self.user_details
        
    def make_msg(self):
        if len(self.user_details) > 0:
            for detail in self.user_details:
                msg = self.base_msg
                formatted_msg = msg.format(
                    name=detail["name"],
                    date=detail["date"],
                    price=detail["amount"]
                )
                self.messages.append(formatted_msg)
            return self.messages
        else: return []
        
    