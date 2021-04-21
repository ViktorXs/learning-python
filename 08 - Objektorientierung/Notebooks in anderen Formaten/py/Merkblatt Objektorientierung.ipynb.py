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

# # Erste Schritte: Objektorientierung
# 
# Objektorientierung ist ein unglaublich mächtiges Konzept, welches es uns ermöglicht, Code sauber zu organisieren.

# Wir haben schon mit Objekten gearbeitet, z. B. mit dem Listen-Objekt von Python, auf das wir Methoden wie die append()-Methode angewendet haben.

# In[3]:


students = ["Max", "Monika"]
students.append("Erik")

print(students)


# ### Eine Klasse definieren

# Wir wollen eigene Objekte mit eigenen Methoden erzeugen. Dafür brauchen wir Klassen, das sind Baupläne für Objekte. Die entsprechend dieser Anleitungen erzeugten Objekte nennt man Instanzen dieser Klasse:

# In[2]:


# Wir definieren die Klasse Student mit der Methode name(),
# Klassennamen beginnen gemäß Konvention mit Großbuchstaben

class Student():
    
    # self ist ein Schlüsselwort, es fungiert gewissermassen 
    # als Platzhalter für die jeweilige Instanz
    def name(self):
        print(self.firstname + " " + self.lastname)


# ### Eine Instanz erstellen

# Mittels dieser Klasse als Vorlage erstellen wir uns nun eine Student-Instanz und speichern sie in einer Variable:

# In[8]:


erik = Student()


# In[16]:


monika = Student()
monika.firstname = "Monika"
monika.lastname ="Müller"

print(monika.firstname)
print(monika.lastname)


# ### Die Methode eines Objektes benutzen
# Wie gewohnt funktioniert so auch der Zugriff auf die Methode des Objektes:

# In[17]:


erik.name()


# In[19]:


monika.name()


# Insbesondere kann es auch weitere Objekte mit einer Methode desselben Namens geben:

# In[31]:


class Company():
    
    def name(self):
        print(self.legal_name + ": " + self.legal_type)

c = Company()
c.legal_name = "Max Müller"
c.legal_type = "GmbH"

c.name()


# In[32]:


def name_5x(v):
    for i in range(0,5):
         v.name() 
    
name_5x(c)
name_5x(erik)
name_5x(monika)


# In der Funktion name_5x() wird jeweils die zum Objekt gehörige Methode name() ausgeführt. Dafür müssen die Objekte natürlich eine name()-Methode enthalten.

# # Objektorientierung: Constructor, Eigenschaften abändern
# 
# In den nächsten Abschnitten geht es darum, wie du: 
# 
# - mit Hilfe eines Constructors Eigenschaften einer Klasse definieren kannst
# - Eigenschaften einer Instanz abänderst.

# Wir haben die bereits die Klasse Students ein wenig erweitert:

# In[13]:


class Student():
    
    # Das ist unser sogenannter Constructor: hier definieren 
    # wir die Variablen für die Klasse. 
    #
    # self ist obligatorisch und bezieht sich immer auf das 
    # Objekt, das gerade angelegt wird.
    #
    # bei der Erzeugung der Instanz taucht self aber nicht
    # als Parameter auf!
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def name(self):
        print(self.firstname + " " + self.lastname)

erik = Student("Erik", "Mustermann")
erik.name()


# Die Klassendefinition mit Constructor liefert also dieselben Ergebnisse wie die vorherige umständlichere Definition.

# Wir ergänzen eine weitere Methode:

# In[1]:


class Student():
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        # Hier initialisieren wir die neue Variable term (Eigenschaft)
        self.term = 1
        
         # Mit dieser Methode erhöhen wir die Variable term um 1
    def increase_term(self):
        self.term = self.term + 1
    
        # name() gibt nunmehr zusätzlich die Anzahl der Semester aus
    def name(self):
        print(self.firstname + " " + self.lastname + 
              " (Semester: " + str(self.term) + ")")
        


# In[19]:


erik = Student("Erik", "Mustermann")
erik.name()


# In[20]:


erik.increase_term()
erik.name()


# ## Objektorientierung: Private Eigenschaften und Methoden
# 
# Private Eigenschaften erlauben sauberes Kapseln von Eigenschaften und Methoden. Dadurch können wir Variablen und Methoden quasi vor "neugierigen Blicken" von außerhalb "schützen" - sehr wichtig, wenn wir später die Möglichkeit haben möchten, diese Variablen / Methoden noch anzupassen. Das geht nur, wenn unser Kollege von seinem Code aus darauf  nicht zugreift:

# In[16]:


class Student():
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.term = 1
        
    # Bei dieser Methode schränken wir ein, dass man 
    # nicht mehr als 9 Semester erreichen            
    def increase_term(self):
        if self.term >= 9:
            return
        self.term = self.term + 1
        
    def get_term(self):
        return self.term
    
    def name(self):
        print(self.firstname + " " + self.lastname + 
              " (Semester: " + str(self.term) + ")")
        
        
erik = Student("Erik", "Mustermann")
erik.increase_term()
erik.name()


# In[17]:


erik.increase_term()
erik.increase_term()
erik.increase_term()
erik.increase_term()
erik.increase_term()
erik.increase_term()
erik.increase_term()
erik.increase_term()
erik.increase_term()
erik.increase_term()
erik.name()


# Trotzdem können wir von außen noch auf die Eigenschaft zugreifen und sie überschreiben:

# In[19]:


erik.term = 100
erik.name()


# Wenn wir allerings zwei Unterstriche vor die Variable setzen, machen wir sie **privat**.
# 
# In Python gibt es auch die Konvention seitens der Programmierer, private Eigenschaften mit einem Unterstrich zu benennen, auch wenn sie dann technisch noch nicht privat sind. Dafür braucht es wirklich zwei Unterstriche zu Beginn ihres Namens:

# In[3]:


class Student():
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.__term = 1
        
    def increase_term(self):
        if self.__term >= 9:
            return
        self.__term = self.__term + 1
     
    # Die Methode ergänzen wir, um von außerhalb der Klasse 
    # noch die term-Eigenschaft abfragen zu können
    def get_term(self):
        return self.__term
    
    def name(self):
        print(self.firstname + " " + self.lastname + 
              " (Semester: " + str(self.__term) + ")")


# In[5]:


erik = Student("Erik", "Mustermann")
# Punkt in Verbindung mit Unterstrich ist dabei als 
# Warnung zu verstehen - unbedingt vermeiden!

# Zwei Unterschtriche (wie hier) ist aber komplett "privat",
# daher können wir so nicht auf das Attribut zugreifen:

print(erik.__term)


# Auch den Zugriff auf Methoden können wir einschränken:

# In[31]:


class Student():
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.__term = 1
        
    def increase_term(self):
        if self.__term >= 9:
            return
        self.__term = self.__term + 1

    def get_term(self):
        return self.__term
    
    def name(self):
        print(self.firstname + " " + self.lastname + 
              " (Semester: " + str(self.__term) + ")")
        
    # Unserer private Funktion    
    def __do_something(self):
        print("doSomething")


# In[34]:


test = Student("Tim", "Test")
test.name()
test.__do_something()


# ## In Python gibt es ein paar besondere Methoden, die unsere Klasse implementieren kann...
# 
# Damit kannst du dafür sorgen, dass:
# 
# - deine Klasse direkt ausgegeben werden kann
# - du len(variable) berechnen kannst.

# Die str-Funktion

# In[5]:


class PhoneBook():
    def __init__(self):
        self.__entries = {}
        
    def add(self, name, phone_number):
        self.__entries[name] = phone_number
        
    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None
    
    def __str__(self):
        return "PhoneBook(" + str(self.__entries) + ")"
    
book = PhoneBook()
book.add("Mustermann", "+4912345678")
book.add("Müller", "+49123456789")

print(book)


# Die repr-Methode

# In[12]:


class PhoneBook():
    def __init__(self):
        self.__entries = {}
        
    def add(self, name, phone_number):
        self.__entries[name] = phone_number
        
    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None
    
    def __str__(self):
        return "PhoneBook(" + str(self.__entries) + ")"
    
    def __repr__(self):
        return self.__str__()

        
book = PhoneBook()
book.add("Mustermann", "+4912345678")
book.add("Müller", "+49123456789")

print(book)


# Die len-Methode

# In[13]:


class PhoneBook():
    def __init__(self):
        self.__entries = {}
        
    def add(self, name, phone_number):
        self.__entries[name] = phone_number
        
    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None
    
    def __len__(self):
        return len(self.__entries)

        
book = PhoneBook()
book.add("Mustermann", "+4912345678")
book.add("Müller", "+49123456789")

print(len(book))


# # Vererbung
# 
# Vererbung ist ein fundamentales Konzept der Objektorientierung, mit dem du Daten aufteilen und besser modellieren kannst.

# Die Klasse Student kennen wir schon:

# In[4]:


class Student():
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    def name(self):
        return self.firstname + " " + self.surname


# In[7]:


student = Student("Monika", "Mustermann")
print(student.name())


# Wir wollen eine weitere Klasse definieren, die Ähnlichkeiten zu einer bereits bestehenden Klasse aufweist:

# In[29]:


class WorkingStudent():
    
    def __init__(self, firstname, surname, company):
        self.firstname = firstname
        self.surname = surname
        self.company = company
    
    def name(self):
        return self.firstname + " " + self.surname
        


# In[30]:


student = WorkingStudent("Max", "Müller", "ABCDEF GmbH")
print(student.name())


# ### Eine Klasse mit Vererbung definieren
# 
# Wir können uns sparen, gleiche Instanzvariablen und Methoden ein weiteres Mal zu definieren - dank Vererbung. Dazu verweisen wir innerhalb einer Klassendefinition auf eine andere:

# In[44]:


# Als Parameter übergeben wir die Klasse, von der unsere neue Eigenschaften und Methoden vererbt werden soll (Mutterklasse)
class WorkingStudent(Student):
    
    def __init__(self, firstname, surname, company):
        # Die alten Instanzvariablendefinitionen werden unten hinfällig
        # self.firstname = firstname
        # self.surname = surname
        
        # mit super() zeigen wir Python an, dass die init()-Methode der Mutterklasse angewendet werden soll
        super().__init__(firstname, surname)
        self.company = company
    
    def name(self):
        # wieder verweisen wir mit super() auf die Methode der Mutterklasse, die wir für die Klasse WorkingStudent überschreiben
        return super().name() + " (" + self.company + ")"


# In[39]:


student = WorkingStudent("Max", "Müller", "ABCDEF GmbH")
print(student.name())


# In[43]:


students = [
    WorkingStudent("Max", "Müller", "ABCDEF GmbH"),
    Student("Monika", "Mustermann"),
    Student("Erik", "Müller"),
    WorkingStudent("Franziska", "Mustermann", "XYZXYZ GmbH")
]

for student in students:
    print(student.name())


# Hier sehen wir, dass die verschiedenen name()-Methoden verschiedene Ausgaben liefern, obwohl wir mit demselben Namen auf sie zugreifen.

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
# Die Funktion **isinstance()** erhält zwei Parameter: die Variable und die Klasse bezüglich derer auf Zugehörigkeit der Variable geprüft werden soll. isinstance() liefert einen Bool zurück.

# In[19]:


print(isinstance(w_student, WorkingStudent))
print(isinstance(w_student, Student))

print(isinstance(student, WorkingStudent))
print(isinstance(student, Student))


# Da Student die Mutterklasse von  WorkingStudent ist, ist w_student auch bezüglich Student eine Instanz.

# Nützlich wird die Funktion, wenn wir nach Klassen filtern wollen, z. B. nur Instanzen von WorkingStudent ausgeben:

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


# ## Styleguide - Benennung von Klassen und Variablen
# 
# Grundsätzlich ist es in Python egal, wie wir eine Klasse / Variable benennen. Unser Programm wird so oder so funktionieren.
# 
# **Aber:** Für Python gibt es ein paar Style - Guides, wie wir "schönen" Code schreiben können. Da möchte ich in diesem Abschnitt die wichtigsten Punkte von durchgehen (https://www.python.org/dev/peps/pep-0008/).
# 
# Wie können (sollten) wir Variablen / Klassen / Funktionen überhaupt benennen, insbesondere wenn die Namen aus mehreren Wörtern bestehen sollen?
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


# In[ ]:





