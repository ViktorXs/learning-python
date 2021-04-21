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

# ## In Python gibt es ein paar besondere Methoden, die unsere Klasse implementieren kann...
# 
# Damit kannst du dafür sorgen, dass:
# 
# - deine Klasse direkt ausgegeben werden kann,
# - du len(variable) berechnen kannst.

# Die str-Funktion

# In[5]:


class PhoneBook():
    def __init__(self):
        self.__entries = {}
        
    def add(self, name, phone_number):
        self.__entries[name] = phone_number
        
    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None
    
    def __str__(self):
        return "PhoneBook(" + str(self.__entries) + ")"
    
book = PhoneBook()
book.add("Mustermann", "+4912345678")
book.add("Müller", "+49123456789")

print(book)


# Die repr-Methode

# In[12]:


class PhoneBook():
    def __init__(self):
        self.__entries = {}
        
    def add(self, name, phone_number):
        self.__entries[name] = phone_number
        
    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None
    
    def __str__(self):
        return "PhoneBook(" + str(self.__entries) + ")"
    
    def __repr__(self):
        return self.__str__()

        
book = PhoneBook()
book.add("Mustermann", "+4912345678")
book.add("Müller", "+49123456789")

print(book)


# Die len-Methode

# In[13]:


class PhoneBook():
    def __init__(self):
        self.__entries = {}
        
    def add(self, name, phone_number):
        self.__entries[name] = phone_number
        
    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None
    
    def __len__(self):
        return len(self.__entries)

        
book = PhoneBook()
book.add("Mustermann", "+4912345678")
book.add("Müller", "+49123456789")

print(len(book))


