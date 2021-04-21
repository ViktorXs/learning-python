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

# # Musterlösung: Übungsblatt Funktionsparameter & Sortierfunktionen

# ### Aufgabe 1
# 
# Vervollständige die Funktion `shortest_word()`: Ihr sollen mehrere Strings übergeben werden (KEINE Liste von Strings!), von denen sie den String mit den wenigsten Zeichen zurückliefert.
# 
# Hinweis: Benutze variable Parameter (mit Sternchen `*` oder doppelten Sternche `**`)

# In[15]:


def shortest_word(first, *words):
    shortest = first
    for word in words:
        if len(word) < len(shortest):
            shortest = word      
    return shortest
    
print(shortest_word("Max", "Moritz", "Monika", "Tim", "Jo"))


# ### Aufgabe 2

# **a.)**
# 
# Sortiere die Tupel in der Liste `tupels` aufsteigend nach ihrer Summe.
# 
# **Hinweis:**  Schreibe dazu zuerst eine normale Funktion, und löse die Aufgabe anschließend nochmal mit einer lambda - Funktion.

# In[1]:


tupels = [(10, 2), (4, 1), (0, 17), (3, 3), (5, 7), (11, 3)]

def tupels_sort(a):
    return a[0] + a[1]

tupels.sort(key = tupels_sort)

print(tupels)


# In[18]:


tupels = [(10, 2), (4, 1), (0, 17), (3, 3), (5, 7), (11, 3)]

tupels.sort(key = lambda t: t[0] + t[1])

print(tupels)


# **b.)** 
# 
# Sortiere die Liste `names` mit Namen nach dem Nachnamen. Du kannst annehmen, dass alle Namen in der Liste nur einen Vornamen enthalten. 
# 
# Überlege dir dazu zuerst, wie du den Nachnamen ermittelst, und schreibe dann die entsprechende Funktion, die du der `.sort()` - Funktion übergibst.
# 
# **Hinweis:**  Schreibe dazu zuerst eine normale Funktion, und löse die Aufgabe anschließend nochmal mit einer lambda - Funktion.

# In[21]:


names = ["Elif Else", "Sebastian Klarnamen", "Anna Boa", "Anton Adel", "Conny Coder", "Anne Wortmann", "Willy Cordes"]

def tupels_sort(s):
    return s.split()[1]

names.sort(key = tupels_sort)
print(names)


# In[16]:


names = ["Elif Else", "Sebastian Klarnamen", "Anna Boa", "Anton Adel", "Conny Coder", "Anne Wortmann", "Willy Cordes"]

names.sort(key = lambda s: s.split()[1])

print(names)


# **c.)**
# 
# Sortiere die Liste `sentences` absteigend nach der Anzahl der Wörter, die ein Element aus `sentences` jeweils enthält. Du kannst annehmen, dass in den Sätzen alle Wörter ordnungsgemäß mit Leerzeichen voneinander getrennt sind. :-)
# 
# **Hinweis:**  Schreibe dazu zuerst eine normale Funktion, und löse die Aufgabe anschließend nochmal mit einer lambda - Funktion.

# In[25]:


sentences = ["Sie liefen weiter den Strand entlang.", "Der Hund bellte laut.", "Er rutschte aus.", "Sie lachte."]

def tupels_sort(s):
    return len(s.split())

sentences.sort(key = tupels_sort, reverse = True)

print(sentences)


# In[11]:


sentences = ["Der Hund bellte laut.", "Sie lachte.", "Sie liefen weiter den Strand entlang.", "Er rutschte aus."]

sentences.sort(key = lambda s: len(s.split()), reverse = True)

print(sentences)


# ### Zusatzaufgabe (schwer)
# 
# Verändere den folgenden Code, sodass die Liste `l` nicht mehr innerhalb der Funktion `make_row()` überschrieben wird. Die Liste, die `make_row()`ausgibt soll also identisch mit der bisherigen sein, `l` soll aber am Ende in seiner ursprünglichen Form ausgegeben werden.

# In[28]:


l = ["o", "x", "o"]

def make_row(row):
    new_row = row[:]
    # oder: new_row = row.copy()
    # oder: new_row = [i for i in row]
    new_row[2] = "x"
    print(new_row)
    
make_row(l)
print(l)


# In[ ]:





