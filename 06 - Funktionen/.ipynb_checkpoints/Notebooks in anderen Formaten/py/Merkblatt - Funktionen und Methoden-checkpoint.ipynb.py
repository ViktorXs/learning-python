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

# # Merkblatt: Funktionen & Methoden
# 
# ## Funktionen
# Funktionen sind zusammengefasste Codeblöcke. Mittels Funktionen können wir es vermeiden, mehrmals verwendete Codeblöcke zu wiederholen. Wir definieren stattdessen einmal eine Funktion, die diese Codeblöcke enthält und brauchen an weiteren Stellen nur noch (kurz) die Funktion aufzurufen, ohne die in ihr enthaltenen Codezeilen zu kopieren.

# ### Eine Funktion definieren und aufrufen
# Wir haben schon einige Funktionen kennengelernt, die uns Python zur Verfügung stellt. Die Funktion, die wir bislang wohl am häufigsten verwendet haben, ist die print-Funktion:

# In[1]:


print("HALLO WELT")


# Wenn wir eine eigene Funktion verwenden wollen, müssen wir sie zuerst definieren. Eine solche Funktionsdefinition hat die allgemeine Syntax:
# 
# **def Funktionname():**
# <br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Code**

# In[4]:


def multi_print():
    print("Hallo Welt!")
    print("Hallo Welt!")


# Um eine Funktion auszuführen, die definiert wurde, schreiben wir: **Funktionname()**

# In[5]:


multi_print()


# ### Funktionen mit einem Argument
# Man kann Funktionen ein **Argument** übergeben, d.h. einen Wert, von dem der Code innerhalb der Funktion abhängt.
# 
# 
# **def Funktionsname(Argument):**
# <br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Code in dem mit dem spezifischen Argument gearbeitet wird**

# In[6]:


def multi_print2(name):
    print(name)
    print(name)
    
multi_print2("HALLO")
multi_print2("WELT")


# Du kannst dir einen solchen Parameter als eine zu einer Funktion gehörige Variable vorstellen. Vermeide es, einen Funktionsparameter wie eine bereits bestehende Variable zu benennen - Verwirrungsgefahr!

# In[7]:


name = "MARS"

def multi_print2(name):
    print(name)
    print(name)
    
multi_print2("HALLO")
multi_print2("WELT")

print(name)


# Du siehst, dass der Wert der Variable _name_ keinen Einfluss auf das Argument _name_ der Funktion hat!

# ### Weitere Funktionen in Python

# Auch die len-Funktion für Listen kennst du schon. :-) 

# In[1]:


print(len(["Hallo", "Welt"]))


# Du kannst die len-Funktion auch auf Strings anwenden.

# In[2]:


print(len("Hallo"))


# Eine Übersicht über Funktionen in Python findest du hier: https://docs.python.org/3/library/functions.html

# ### Funktionen mit mehreren Argumenten
# 
# Eine Funktion darf auch mehrere Argumente enthalten.
# 
# **def Funktionenname(Argument1, Argument2, ...):**
# <br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Code in dem mit Argument1, Argument2,... gearbeitet wird**

# In[1]:


def multi_print(name, count):
    for i in range(0, count):
        print(name)
        
multi_print("Hallo!", 5)


# ### Funktionen in Funktionen
# Funktionen können auch ineinander geschachtelt werden:

# In[5]:


def weitere_funktion():
    multi_print("Hallo!", 3)
    multi_print("Welt!", 3)


# In[6]:


weitere_funktion()


# ### Einen Wert zurückgeben
# Bislang führen wir mit Funktionen einen Codeblock aus, der von Argumenten abhängen kann. Funktionen können aber auch mittels des Befehls **return** Werte zurückgeben:

# In[2]:


def return_element(name):
    return name

print(return_element("Hi"))


# Solche Funktionen mit return können wir dann wie Variablen behandeln:

# In[10]:


def return_with_exclamation(name):
    return name + "!"

if return_with_exclamation("Hi") == "Hi!":
    print("Right!")
else:
    print("Wrong.")


# In[1]:


def maximum(a, b):
    if a < b:
        return b
    else:
        return a

result = maximum(4, 5)
print(result)


# # Funktionen vs. Methoden

# ### Funktionen
# Bei ihrem Aufruf stehen Funktionen "für sich" und das, worauf sie sich beziehen steht ggf. als Argument in den Klammern hinter ihnen:

# In[36]:


liste = [1, 2, 3]


# In[28]:


print(liste)


# In[29]:


print(len(liste))


# ### Methoden
# Daneben kennen wir aber auch schon Befehle, die mit einem Punkt an Objekte angehängt werden. Eine Liste ist ein solches **Objekt**. Jedes Objekt hat Methoden, auf die wir zurückgreifen können. Diese Methoden können wir aber nicht auf ein Objekt eines anderen Typs anwenden (meistens zumindest).
# 
# Schauen wir uns einige nützliche Methoden des Listen-Objektes an :-) (du brauchst sie dir nicht alle merken)

# In[37]:


# ein Element anhängen
liste.append(4)

print(liste)


# In[39]:


# ein Element an einem bestimmten Index entfernen
liste.pop(2)


# In[ ]:


# wir sehen, dass die Methode nicht die aktualisierte Liste, sondern das entfernte Element liefert


# In[40]:


print(liste)


# In[41]:


# Ein Element an einer bestimmten Stelle einfügen
# das erste Argument bei insert gibt an, welches Element in die Liste eingefügt wird, 
# das zweite Argument bei insert gibt an, an welcher Stelle das Element eingefügt wird; 
# beachte, dass der Index des ersten Elements in einer Liste 0 ist! 
liste.insert(1, 4)

print(liste)


# In[ ]:


# ein Element entfernen
liste.remove(4)

print(liste)


# In[21]:


# den Index eines Elementes angeben (die erste Stelle, an der es vorkommt)
print(liste.index(3))


# In[23]:


print(liste.index(4))


# In[24]:


print(liste.count(4))


# In[19]:


# mit reverse können wir die Reihenfolge einer Liste umkehren
liste.reverse()
print(liste)


# In[ ]:





