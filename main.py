#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import simpledialog
from tkinter import *

USER_INP = "https://example.com"

ROOT = tk.Tk()

ROOT.withdraw()

USER_INP = simpledialog.askstring(title="Url", prompt="What's the Url?:")

r = requests.get(USER_INP)
soup = BeautifulSoup(r.text, 'html.parser')

print(USER_INP)
# Example Domain

print(soup.a['href'])
# http://www.iana.org/domains/example

absaetze = soup.find_all('a') # Speichert alle Absätze als Liste

print(absaetze)

for absatz in absaetze: # Loopt über die Liste
    print(absatz.text) # Gibt jeden Absatz in der Konsole aus
#     This domain is established to be used for illustrative examples in documents. You may use this
#     domain in examples without prior coordination or asking for permission.
#     More information...

def code1():
    code1.config(text='Danke!')
    print("fick dich!")
    exit()
fenster = Tk()
code1 = Button(fenster, text='code1', command=code1)
code1.pack(pady=10)
fenster.mainloop()