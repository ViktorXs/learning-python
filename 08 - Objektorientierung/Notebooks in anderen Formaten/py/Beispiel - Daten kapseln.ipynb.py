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

# ## Beispiel: Daten kapseln
# 
# In dieser Lektion lernst du ein Beispiel kennen, warum es sich lohnen kann, Daten mit Objektorientierung zu kapseln.

# In[3]:


class PhoneBook():
    
    def __init__(self):
        self.__entries = {}
        
    # Nur mit der add-Methode können wir mit dem Dictionary kommunizieren    
    def add(self, name, phone_number):
        self.__entries[name] = phone_number
        
    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None
        
book = PhoneBook()
book.add("Mustermann", "+4912345678")
book.add("Müller", "+49123456789")

print(book.get("Mustermann2"))


# Vorteil: Übersichtlichkeit, Voraussetzung größere Anwendungen bauen (Modular)

# In[ ]:





