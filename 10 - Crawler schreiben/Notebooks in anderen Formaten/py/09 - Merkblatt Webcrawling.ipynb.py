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

# ## Merkblatt: Webcrawling
# 
# Crawlen beschreibt den Prozess, bei dem du Daten aus einer Webseite extrahierst. Das können beispielsweise die aktuellen Artikel einer Nachrichtenwebseite sein oder auch einfach nur der aktuelle Börsenkurs. 
# 
# Beim Crawlen ist das Vorgehen wie folgt:
# 
# 1. Zuerst muss die Seite als HTML-Code heruntergeladen werden.
# 2. Anschließend wird der HTML-Code eingelesen und das entsprechende Element gesucht.
# 3. Aus den gefundenen Element(en) werden dann die Informationen extrahiert.
# 4. Wir machen irgendetwas mit diesen Informationen. Beispielsweise können wir sie als .csv-Datei speichern oder direkt verrechnen.
# 
# Ggf. müssen wir den Crawling-Prozess dann noch etwas anpassen, z. B. wenn die Daten über mehrere Seiten verteilt sind. Dann kann man dem Crawler z. B. sagen, dass auch die nächste Seite noch betrachtet werden soll.
# 
# 
# ### 1.: HTML-Code herunterladen
# 
# Das Herunterladen des HTML-Codes ist normalerweise in Python recht aufwendig. Glücklicherweise gibt's dafür aber das `requests` - Paket, welches uns seitens Python bereitgestellt wird. Damit können wir eine URL ziemlich einfach herunterladen:

# In[7]:


import requests

response = requests.get("http://python.beispiel.programmierenlernen.io")


# Die Anfrage wurde jetzt an den Server gestellt. Wenn wir überprüfen möchten, ob das ganze soweit geklappt hat, können wir den Statuscode der Antwort genauer untersuchen. 
# 
# Wichtige HTTP Status-Codes sind:
# 
# - 500: Internal Server Error
# - 404: Seite nicht gefunden
# - 200: Alles Okay

# In[15]:


print(response.status_code)


# Hier hat wohl alles geklappt, die Seite wurde korrekt abgerufen. Wenn wir jetzt auf den Seiteninhalt zugerifen möchten, so können wir das über `response.text` tun. Es wird dann der gesamte Text ausgegeben. Da das hier im Merkblatt zu lang wäre, kürzen wir das auf die ersten 15 Zeilen:

# In[22]:


print("\n".join(response.text.split("\n")[:15]))


# ### 2.: HTML-Elemente mit unseren Daten finden
# 
# Jetzt haben wir den gesamten HTML-Code heruntergeladen und möchten daraus die passenden Element extrahieren. Dazu bieten sich CSS-Selektoren an, mit denen wir sehr komfortabel auf Elemente zugreifen können. 
# 
# Beispiel:
# 
# - `<div class="test">Hallo</div>`: Dieses Element können wir mit Hilfe von `.test` finden, der Punkt steht hierbei dafür, dass wir nach einer Klasse suchen
# 
# - `<div class="id">Hallo</div>`: Dieses Element können wir mit Hilfe von `#test` finden, die Raute steht hierbei dafür, dass wir ein Element nach dem ID-Attribut suchen
# 

# In[ ]:





