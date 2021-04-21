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

# ## Booleans (`and` und `or`)

# In[3]:


age = 35

if age >= 30 and age <= 39:
    print("Diese Person ist in ihren 30-ern")


# In[6]:


age = 45
if age < 30 or age >= 40:
    print("Diese Person ist nicht in ihren 30-ern")


# In[7]:


age = 25
print(age < 30)


# In[10]:


above_30 = age >= 30

print(above_30)


# In[14]:


age = 25

above_20 = age >= 20
print(above_20)

if age >= 20:
    print("if-Abfrage wurde ausgeführt")


# In[15]:


print(True and True)
print(True and False)
print(False and True)
print(False and False)


# In[16]:


print(True or True)
print(True or False)
print(False or True)
print(False or False)


# In[17]:


country = "US"
age = 20

if (country == "US" and age >= 21) or (country != "US" and age >= 18):
    print("Diese Person darf Alkohol trinken")


# In[ ]:





