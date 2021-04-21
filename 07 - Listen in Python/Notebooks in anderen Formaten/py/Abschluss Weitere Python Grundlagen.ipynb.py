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

# # Abschluss Weitere Python Grundlagen

# ### Alternative Benutzernamen
# Zurück zum Zauber-Online-Shop. Diesmal sind Funktionen gewünscht, die alternative Nutzernamen vorschlagen, sofern der Name des neuen Nutzers schon als Nutzername belegt ist.
# 

# #### a.) Abgekürzte Vornamen
# 
# Du sollst eine Funktion schreiben, der zwei Parameter übergeben werden: ein Vorname und ein Nachname. Die Funktion soll daraus einen Nutzernamen liefern, der aus dem Anfangsbuchstaben des Vornamens und dahinter, ohne Leerzeichen, dem ganzen Nachnamen besteht.

# In[19]:


def user_name(first, last):
    # hier kommt dein Code hin

print(user_name("Willy", "Wizard"))


# In[4]:


def user_name(first, last):
    return first[0] + last

print(user_name("Willy", "Wizard"))


# #### b.) Verbotene Zeichen
# 
# Viele Nutzer hängen aus Glauben die Zahl 666 an den Benutzernamen. Doch so viel Magie stört die Shopsoftware! Wenn also ein Nutzername auf 666 endet, muss die Zahl entfernt werden. Schreibe eine Funktion, die als Parameter einen Namen erhält und diesen gegebenenfalls bereinigt zurückliefert.
# 
# Nur die Folge 666 ist verboten, 66 und 6666 sollen erlaubt sein.

# In[13]:


def legit_name(name):
    #hier steht dein Code
    
legit_name("Hexer666")


# In[ ]:


def legit_name(name):
    if name[-3:] == "666":
        return name[:-3]
    else:
        return name
    
legit_name("Hexer666")


# #### c.) Nummerierte Nutzernamen
# In Fällen, dass der gewünschte Nutzername auf eine Zahl endet, soll der Name mit der nächsthöheren (ganzen) Zahl vorgesschlagen werden. Ausser, die letzte Ziffer des Nutzernamens ist schon eine 9. Dann soll einfach wieder eine 1 an den bereits bestehenden Nutzernamen angehängt werden. Schreibe eine Funktion, die als Parameter einen String erhält! Du kannst annehmen, dass der String auf eine Zahl endet. Die Funktion soll einen String zurückliefern, worin die Zahl aus dem Ausgangsstring aber um 1 erhöht bzw. eine 1 angehängt wurde.
# 
# Du kannst davon ausgehen, dass mit der Funktion nur Namen bearbeitet werden sollen, die bereits auf verbotene Zeichen geprüft wurden.

# In[14]:


def user_name(name):
    # hier kommt dein Code hin

print(user_name("Teufelchen699"))


# In[3]:


def user_name(name):
    
    number = int(name[-1])
    
    if number < 9:
        number += 1
        return name[:-1] + str(number)
    else:
         return name + str(1)
        
print(user_name("Teufelchen699"))


# #### d.) Liste mit Kunstwörtern
# Die Mathemagierin braucht Inspiration bei der Benennung neuer Produkte! Sie gibt dir eine Liste mit Strings und wünscht sich auf dieser Grundlage von dir eine Liste mit Kunstwörtern. Ein solches Kunstwort soll aus einem Wort von der Liste gebildet werden, indem man bei jedem Wort die ersten vier Buchstaben weglässt und dahinter nochmal das Wort, aber ohne den ersten und die letzten beiden Buchstaben gehängt wird. 
# 
# Du fragst dich, ob noch alles mit der Mathemagierin in Ordnung ist und machst dich dann an die Aufgabe, eine solche Liste mit den komischen Kunstwörtern möglichst schnell zu erstellen.

# In[62]:


words = ["Karten", "Sägeblatt", "Teller", "Tasse", "Vogel", "Kraut", "Faden"]


# In[63]:





# In[65]:


[i[3:] + i[1:-2] for i in words]


# ### Gut gemacht :-)

