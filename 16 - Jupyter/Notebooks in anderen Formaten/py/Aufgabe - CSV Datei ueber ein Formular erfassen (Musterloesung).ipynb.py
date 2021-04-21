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

# ## Musterlösung: CSV-Datei über ein Formular erfassen
# 
# Stell dir vor, du möchtest die Anwesenheit von Studierenden überprüfen. Dazu möchtest du zu jedem Studierenden folgende Daten erfassen: Vorname, Nachname, Studienfach.
# 
# Es gibt 5 verschiedene Studienfächer:
# 
# - Mathe
# - Informatik
# - Philosophie
# - Kulturwissenschaften
# - Psychologie
# 
# Aufgabe: Erstelle ein komfortables Formular, mit dem du die Studierenden erfassen kannst! Sorge dafür, dass nach jedem Schritt alle bisher erfassten Daten in einer .csv-Datei (students.csv) abgespeichert werden. In der .csv-Datei sollen 3 Spalten existieren: Vorname, Nachname und Studienfach.
# 
# Verwende für den Vor- bzw. Nachnamen ein Textfeld und für das Studienfach ein Auswahlmenü, mit dem das Studienfach ausgewählt werden kann. Erstelle dann einen Button, mit dem der aktuelle Studierende in die .csv-Datei geschrieben wird und über das Formular anschließend der nächste Studierende erfasst werden kann.

# In[10]:


import csv
import ipywidgets as widgets
from IPython.display import display

firstname = widgets.Text(description="Vorname:", value="")
display(firstname)

lastname = widgets.Text(description="Nachname:", value="")
display(lastname)

subject_options = [
    "---",
    "Mathe", 
    "Informatik", 
    "Philosophie", 
    "Kulturwissenschaften", 
    "Psychologie"
]

subject = widgets.Dropdown(description="Fach:", options=subject_options)
display(subject)

button = widgets.Button(description="Speichern!")
display(button)

def button_click(event):
    firstname_value = firstname.value
    lastname_value = lastname.value
    subject_value = subject.value
    
    if firstname_value != "" and lastname_value != "" and subject_value != "---":
        with open("./students.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow([firstname_value, lastname_value, subject_value])
        firstname.value = ""
        lastname.value = ""
        subject.value = "---"
        
    else:
        print("Bitte das Formular korrekt ausfüllen")
    
button.on_click(button_click)


# In[ ]:





