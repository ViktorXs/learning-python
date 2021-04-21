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

# ## In dieser Lektion lernst du, wie du Module schon benutzt hast!

# In[2]:



import matplotlib.pyplot

matplotlib.pyplot.plot([1, 2, 3], [5, 4, 5])
matplotlib.pyplot.show()


# In[5]:


from matplotlib import pyplot

pyplot.plot([1, 2, 3], [5, 4, 5])
pyplot.show()


# In[6]:



import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [5, 4, 5])
plt.show()


# In[ ]:





