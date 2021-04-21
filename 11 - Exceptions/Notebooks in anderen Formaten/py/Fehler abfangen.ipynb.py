# Diese .py - Datei wurde automatisch aus dem IPython - Notebook (.ipynb) generiert.
# 
# Gelegentlich wurde ich von Teilnehmern gefragt, ob ich die Kursmaterialien nicht 
# auch als normale .py - Datien bereitstellen könne. Dadurch ist es möglich, den Code
# ohne Jupyter zu öffnen, beispielsweise wenn Python-Programme in einem Terminal oder in 
# Eclipse entwickelt werden.
# 
# Dem möchte ich hiermit nachkommen. Ich empfehle dir aber trotzdem, schau' dir lieber die
# IPython - Notebooks direkt an, oder den HTML-Export eben dieser. Dieser reine .py-Export
# ist meiner Meinung nach etwas unübersichtlich.
# 
# Bitte beachte zudem, dass du Pfadangaben ggf. manuell korrigieren musst!
# 
#!/usr/bin/env python
# coding: utf-8

# ## Exceptions in Python
# 
# In dieser Lektion lernst du:
# 
# - Wie du damit umgehst, wenn während der Laufzeit deines Programms ein Fehler auftritt.

# In[2]:


x = 0


print(5 / x)


# In[3]:


with open("datei.xyz", "r") as file:
    print(file)


# In[6]:


try:
    print(5 / 0)
    print(4)
except ZeroDivisionError:
    print("Durch null teilen ist nicht erlaubt!")
print(5)


# In[7]:


try:
    with open("datei.xyz", "r") as file:
        print(file)
except FileNotFoundError:
    print("Die Datei konnte nicht geöffnet werden")


# ## Exceptions in Python
# 
# In dieser Lektion lernst du:
# 
# - Wie du mehrere Exceptions abfangen kannst
# - Und wie du eigene Exceptions erstellen kannst

# In[3]:


try:
    with open("datei.xyz", "r") as file:
        print(file)
    print(5 / 0)
except ZeroDivisionError:
    print("Du darfst nicht durch 0 teilen")
except FileNotFoundError:
    print("FileNotFoundError ist aufgetreten")


# In[4]:


def do_something():
    print(5 / 0)
    
try:
    do_something()
except ZeroDivisionError:
    print("Du darfst nicht durch 0 teilen")


# In[8]:


class InvalidEmailError(Exception):
    pass

def send_mail(email, subject, content):
    if not "@" in email:
        raise InvalidEmailError("email does not contain an @")
try:     
    send_mail("hallo", "Betreff", "Inhalt")
except InvalidEmailError:
    print("Bitte gebe eine gültige E-Mail ein")


# In[ ]:


## Exceptions in Python

In dieser Lektion lernst du:

- Wie du mehrere Exceptions abfangen kannst
- Und wie du eigene Exceptions erstellen kannst

try:
    with open("datei.xyz", "r") as file:
        print(file)
    print(5 / 0)
except ZeroDivisionError:
    print("Du darfst nicht durch 0 teilen")
except FileNotFoundError:
    print("FileNotFoundError ist aufgetreten")

def do_something():
    print(5 / 0)
    
try:
    do_something()
except ZeroDivisionError:
    print("Du darfst nicht durch 0 teilen")

class InvalidEmailError(Exception):
    pass

def send_mail(email, subject, content):
    if not "@" in email:
        raise InvalidEmailError("email does not contain an @")
try:     
    send_mail("hallo", "Betreff", "Inhalt")
except InvalidEmailError:
    print("Bitte gebe eine gültige E-Mail ein")


