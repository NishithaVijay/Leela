#!/usr/bin/python3
import smtplib
message = "hi"
s = smtplib.SMTP('smtp.gmail.com', 587)
s.login("Nish9628@gmail.com", "006Nish#")
s.sendmail("Nish9628@gmail.com","Nish9628@gmail.com",message)