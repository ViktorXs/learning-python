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

# # Exceptions
# 
# Bei der Ausführung eines Programms kann es passieren, dass ein Fehler auftritt.
# 
# Beispielsweise kann dies bei einer Division durch 0 passieren, oder auch, wenn du versuchst, auf eine Datei zuzugreifen, die nicht (mehr) existiert:

# In[1]:


print(5 / 0)


# In[2]:


with open("datei.xyz", "r") as file:
    print(file)


# Manchmal möchtest du nicht, dass bei einem Fehler das Programm direkt beendet wird. 
# 
# Mit einem `try` ... `except` - Block kannst du diese Fehler abfangen, und darauf reagieren:

# In[3]:



try:
    print(5 / 0)
    print(4)
except ZeroDivisionError:
    print("Durch null teilen ist nicht erlaubt!")
print(5)


# ## Mehrere `try` ... `except` - Blöcke
# 
# Dein Programm kann auch mehrere Fehler per `except` abfangen und darauf reagieren:

# In[3]:


try:
    with open("datei.xyz", "r") as file:
        print(file)
    print(5 / 0)
except ZeroDivisionError:
    print("Du darfst nicht durch 0 teilen")
except FileNotFoundError:
    print("FileNotFoundError ist aufgetreten")


# ## Eigene Fehler auslösen
# 
# Über den `raise` - Befehl kannst du eigene Fehler auslösen:

# In[8]:


class InvalidEmailError(Exception):
    pass

def send_mail(email, subject, content):
    if not "@" in email:
        raise InvalidEmailError("email does not contain an @")
try:     
    send_mail("hallo", "Betreff", "Inhalt")
except InvalidEmailError:
    print("Bitte gebe eine gültige E-Mail ein")


# ## Mit `finally` aufräumen
# 
# Wenn du möchtest, dass ein bestimmter Codeblock auf jeden Fall ausgeführt wird, egal, ob ein Fehler auftritt oder nicht, kannst du diesen Code in einen `finally` - Block schreiben. Dieser Code wird auf jeden Fall ausgeführt, selbst wenn ein Fehler vorher aufgetreten ist.
# 
# In dem Fall hier z. B. kannst du dadurch garantieren, dass du eine einmal geöffnete Datei auf jeden Fall über das `.close()` schließt (notwendig, wenn du die Datei nicht über ein `with file = open("existiert.txt", "r")` öffnest).
# 
# Andere Beispiele könnten z. B. sein, dass eine Netzwerkverbindung auf jeden Fall noch getrennt wird, etc. 

# In[9]:


try:
    file = open("existiert.txt", "r")
    print(file)
    print(5 / 0)
except FileNotFoundError:
    print("Datei wurde nicht gefunden")
finally:
    print("FINALLY!!!")
    file.close()


# ### Das `with` - Konstrukt
# 
# In der Praxis bietet sich aber für Dateien primär das `with` - Konstrukt an. Da ist quasi schon seitens Python implementiert, dass die Datei auf jeden Fall geschlossen wird - egal, ob ein Fehler auftritt oder nicht. 
# 
# Unser Code wird also sehr viel übersichtlicher:

# In[6]:


with open("existiert.txt", "r") as file:
    print(file)


# In[ ]:





