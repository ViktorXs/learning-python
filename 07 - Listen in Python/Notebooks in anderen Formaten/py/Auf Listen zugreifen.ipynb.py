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

# In[6]:


students = ["Max", "Monika", "Erik", "Franziska", "ABC"]


# In[9]:


print(students[-1])
print(students[-2])


# ## List Slicing

# In[17]:


print(students[2:4])


# In[18]:


print(students[1:-1])


# In[21]:


print(students[0:-1])
print(students[:-1])


# In[22]:


print(students[1:])


# ### List Slicing funktioniert auf auf Strings!

# In[23]:


print("Hallo Welt"[0:5])


# In[24]:


print("Hallo Welt"[-4:])


# In[25]:


print("Hallo Welt"[1:5])


# In[ ]:





