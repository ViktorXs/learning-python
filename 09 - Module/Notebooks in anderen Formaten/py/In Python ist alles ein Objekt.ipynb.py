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

# ## In Python ist alles ein Objekt
# 
# In Python ist sogar eine Zahl eine Instanz einer Klasse... Das wollen wir uns in dieser Lektion mal genauer anschauen! :) 

# In[6]:


a = 12.5

print(type(a))


# In[9]:


12.5 + 5


# In[10]:


a = 12.5
a.__add__(5)


# In[14]:


(12.5).__add__(5)


# In[15]:


s = "Hallo Welt"


# In[16]:


len(s)


# In[17]:


s.__len__()


# In[18]:


class A:
    def __len__(self):
        return 6

instance = A()
len(instance)


# In[ ]:





