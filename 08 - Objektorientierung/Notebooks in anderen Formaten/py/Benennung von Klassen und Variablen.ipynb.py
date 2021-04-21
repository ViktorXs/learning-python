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

# ## Styleguide - Benennung von Klassen und Variablen
# 
# Grundsätzlich ist es in Python egal, wie wir eine Klasse / Variable benennen. Unser Programm wird so oder so funktionieren.
# 
# **Aber:** Für Python gibt es ein paar Style - Guides, wie wir "schönen" Code schreiben können. Da möchte ich in dieser Lektion die wichtigsten Punkte von durchgehen (https://www.python.org/dev/peps/pep-0008/).
# 
# Wie können (sollten) wir Variablen / Klassen / Funktionen überhaupt benennen, insbesondere, wenn die Namen aus mehreren Wörtern bestehen sollen?
# 
# In Python verwendet man dazu nach Konvention:
# 
# - PascalCase (`IchBesteheAusMehrerenWoertern`)
# - sneak_case (`ich_bestehe_aus_mehreren_woertern`)
# 
# Anders als in anderen Programmiersprachen benutzt man nicht:
# 
# - camelCase (`ichBesteheAusMehrerenWoertern`)

# In[3]:


# Klassennamen in PascalCase
# Das Beispiel ist aber zu lange ;-)
class IchBesteheAusMehrerenWoertern():
    def __init__(self):
        print("TEST")
    
    # Funktionsname in sneak_case
    def ich_bin_eine_funktion(self):
        print("asdf")

# Variablennamen auch in sneak_case; aber höchstens drei Wörter ;-)
ich_bestehe_aus_mehreren_woertern = IchBesteheAusMehrerenWoertern()

print(ich_bestehe_aus_mehreren_woertern)


