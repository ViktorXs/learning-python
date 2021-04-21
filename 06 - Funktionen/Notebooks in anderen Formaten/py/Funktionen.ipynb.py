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

# # Funktionen
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
# Man kann Funktionen ein **Argument** übergeben, d. h. einen Wert, von dem der Code innerhalb der Funktion abhängt:
# 
# 
# **def Funktionsname(Argument):**
# <br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Code, in dem mit dem spezifischen Argument gearbeitet wird**

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


# Du siehst, dass der Wert der Variable _name_ keinen Einfluss auf das Argument _name_ der Funktion hat! Die Variable _name_ außerhalb der Funktion ist also eine andere Variable als die Variable _name_ innerhalb der Funktion. 
# 
# Daher Achtung: Das macht den Code unübersichtlich!

# ### Weitere Funktionen in Python

# Auch die len-Funktion für Listen kennst du schon. :-) 

# In[1]:


print(len(["Hallo", "Welt"]))


# Du kannst die len-Funktion auch auf Strings anwenden.

# In[2]:


print(len("Hallo"))


# Eine Übersicht über Funktionen in Python findest du hier: https://docs.python.org/3/library/functions.html

# ### Spiel doch ein wenig mit weiteren Funktionen herum! Dazu kannst du auch nach Python Funktionen googlen. :-)

# In[ ]:






