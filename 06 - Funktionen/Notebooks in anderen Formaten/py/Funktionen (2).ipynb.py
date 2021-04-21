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

# # Funktionen - Teil 2

# ### Funktionen mit mehreren Argumenten
# 
# Eine Funktion darf auch mehrere Argumente enthalten:
# 
# **def Funktionenname(Argument1, Argument2, ...):**
# <br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Code, in dem mit Argument1, Argument2,... gearbeitet wird**

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
# Bislang führen wir mit Funktionen einen Codeblock aus, der von Argumenten abhängen kann. Funktionen können aber auch mittels des Befehls **return** Werte zurückgeben. 

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


# In[5]:


def maximum(a, b):
    if a < b:
        return b
    else:
        return a

result = maximum(4, 5)
print(result)


# ### Zeit zu spielen
# - Schreibe jetzt selbst eine Funktion mit mehreren Argumenten und return! :-)

# In[ ]:






