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

# # Jupter Widgets: Erstelle interaktive Notebooks
# 
# In dieser Lektion lernst du, wie du:
# 
# - Texteingabefelder, Buttons und Slider erstellst
# - Und mit denen interagieren kannst.

# In[2]:


import ipywidgets as widgets
from IPython.display import display


# In[9]:


age = widgets.IntText(description="Alter:", value=25)
display(age)


# In[12]:


print(age.value)


# In[18]:


button = widgets.Button(description="OK")
display(button)

def on_button_click(p):
    print("on_button_click()")

# Wenn geklickt wird: on_button_click(button)
button.on_click(on_button_click)


# In[19]:


age = widgets.IntText(description="Alter:", value=25)
display(age)
button = widgets.Button(description="OK")
display(button)

def on_button_click(p):
    print(age.value)

# Wenn geklickt wird: on_button_click(button)
button.on_click(on_button_click)


# In[ ]:





