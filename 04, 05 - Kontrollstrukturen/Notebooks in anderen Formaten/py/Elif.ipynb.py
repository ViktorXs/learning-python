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

# # elif - noch mehr Entscheidungen
# Wir können in einer if-else-Struktur nur zwei Fälle abfragen, nämlich, ob eine Bedingung wahr ist (True) oder nicht (False). Wenn wir ein Entscheidungsmodell programmieren wollen, in dem noch mehr Bedingungen gecheckt werden sollen, müssen wir bislang mehrere if-else-Strukturen ineinander verschachteln. 

# In[3]:


currency = "€"

if currency == "$":
    print("US-Dollar")
else:
    if currency == "¥":
        print("Japanischer Yen")
    else:
        if currency == "€":
            print("Euro")
        else:
            if currency == "฿":
                print("Thai Baht")


# Durch die Erweiterung um elif können wir innerhalb einer if-else-Struktur beliebig viele Bedingungen checken. 
# 
# elif ist die Kurzfassung von else if: Eine elif-Option deckt also den Fall ab, dass die if-Bedingung nicht erfüllt (False) ist, aber eine weitere Bedingung True ist.

# In[1]:


currency = "HKD"

if currency == "$":
    print("US-Dollar")
elif currency == "¥":
    print("Japanischer Yen")
elif currency == "€":
    print("Euro")
elif currency == "฿":
    print("Thai Baht")
else:
    print("Sonst")


# ### Spiel doch jetzt ein wenig mit dem, was du gelernt hast, herum:
# - Baue selbst eine if-elif-else-Struktur! :-)

# In[ ]:






