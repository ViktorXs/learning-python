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

# # Typen von Variablen prüfen - die type() und isinstance() Funktionen

# Wir benutzen für die Beispiele wieder die bekannten Student und WorkingStudent-Klassen:

# In[3]:


class Student():
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    def name(self):
        return self.firstname + " " + self.surname
        
class WorkingStudent(Student):
    def __init__(self, firstname, surname, company):
        super().__init__(firstname, surname)
        self.company = company
        
    def name(self):
        return super().name() + " (" + self.company + ")"


# In[4]:


w_student = WorkingStudent("Max", "Müller", "ABCDEF GmbH")
student = Student("Monika", "Mustermann")


# ### Den Typ überprüfen mit type()
# Mit der **type()**-Funktion können wir den Typ eines Objektes feststellen: 

# In[13]:


print(type(w_student))
print(type(student))


# In[16]:


if type(w_student) == Student:
    print("Diese Zeile wird nur für einen Student ausgegeben")

if type(student) == Student:
    print("Hier hingegen steht ein richtiger Student")


# ### Checken, ob es sich um eine Instanz handelt mit isinstance()
# 
# Die Funktion **isinstance()** erhält zwei Parameter: die Variable und die Klasse bezüglich derer auf Zugehörigkeit der Variable geprüft werden soll. isinstance() liefert einen Bool zurück:

# In[19]:


print(isinstance(w_student, WorkingStudent))
print(isinstance(w_student, Student))

print(isinstance(student, WorkingStudent))
print(isinstance(student, Student))


# Da Student die Mutterklasse von  WorkingStudent ist, ist w_student auch bezüglich Student eine Instanz.

# Nützlich wird die Funktion wenn wir nach Klassen filtern wollen, z. B. nur Instanzen von WorkingStudent ausgeben:

# In[24]:


students = [
    WorkingStudent("Max", "Müller", "ABCDEF GmbH"),
    Student("Monika", "Mustermann"),
    Student("Erik", "Müller"),
    WorkingStudent("Franziska", "Mustermann", "XYZXYZ GmbH")
]

for student in students:
    ## alternativ: 
    ## if isinstance(student, WorkingStudent):
    if type(student) == WorkingStudent:
        print(student.name())


