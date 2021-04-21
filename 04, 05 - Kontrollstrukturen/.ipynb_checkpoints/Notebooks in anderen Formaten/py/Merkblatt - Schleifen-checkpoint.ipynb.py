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

# # Merkblatt: Schleifen
# 
# Schleifen erlauben es dir, dafür zu sorgen, dass bestimmte Teile vom Programm mehrfach ausgeführt werden. Das ist praktisch, wenn du z.B. eine Liste von Studierenden hast und dafür sorgen möchtest, dass z. B. ein print() - Befehl einmal für jeden Studierenden ausgeführt wird. 
# 
# Eine Schleife erlaubt dir, sowas in recht wenig Code auszudrücken!

# ## Die for-Schleife
# Neben der while-Schleife, die wir schon kennen gelernt haben, gibt es noch die **for-Schleife**. Hier durchläuft eine Schleifenvariable nacheinander die Werte in einer ebenfalls anzugebenden Sequenz.
# 
# Bei dieser Sequenz kann es sich z. B. um eine Liste handeln:

# In[3]:


liste = [5, 8, 10]
for i in liste:
    print(i)


# In[5]:


liste = ["Max", "Moritz", "Monika"]
for i in liste:
    print(i)


# Wir sehen, dass unsere Schleifenvariable i nacheinander und automatisch die Werte aus der Liste annimmt. 

# ### Das range-Objekt
# Als Sequenz für eine for-Schleife braucht man nicht zwangsläufig eine Liste. Häufig greift man stattdessen auf ein **range**-Objekt zurück:

# In[1]:


print(range(0,10))


# In[2]:


for i in range(0, 10):
    print(i)


# In[8]:


# Hier summieren wir alle Zahlen von 1 bis 10 mithilfe einer for-Schleife und eines range-Objektes auf
sum = 0
for i in range(1, 11):
    sum += i
print(sum)


# ## Die while-Schleife
# Ein Code-Block innerhalb einer if-elif-else-Struktur wird jeweils nur einmal ausgeführt. Bei Schleifen wie der **while-Schleife** wird ein Code-Block so lange mehrmals hintereinander ausgeführt, bis eine Abbruchbedingung erfüllt ist:

# In[1]:


counter = 0

while counter < 10:
    print(counter)
    counter = counter + 1
    
print("Hallo Welt")


# Innerhalb einer Schleife **muss** sich **unbedingt** ein Zustand in jedem Schritt verändern, damit die Schleifenbedingung nicht dauerhaft erfüllt ist, und das Programm die Schleife auch wieder verlassen kann.

# In[3]:


students = ["Moritz", "Klara", "Monika", "Max"]
i = 0
while i < len(students):
    print(students[i])
    i = i + 1


# # Continue & Break
# 
# Wir können während eines Schleifendurchlaufs den aktuellen Durchlauf vorzeitig abbrechen und unmittelbar mit dem nächsten Schleifendurchlauf fortfahren (**continue**) oder auch die gesamte Schleife abbrechen (**break**).
# 

# ### Continue
# Wir brauchen einfach das Wort **continue** in eine Schleife zu schreiben, wenn an einer bestimmten Stelle zum neuen Schleifendurchlauf gesprungen werden soll:

# In[5]:


for i in range(0, 10):
    if i == 3:
        continue
    print(i)


# In dem obigen Beispiel wird für den Wert 3 der print()-Befehl übersprungen.

# In[3]:


for i in range(1, 10):
    print(i)


# ### Break
# Auch **break** schreiben wir einfach in eine Zeile, und schon wird die ganze Schleife abgebrochen, wenn das Programm diese Stelle erreicht:
# 

# In[4]:


for i in range(0, 10):
    if i == 3:
        break
    print(i)


# In[6]:


liste = [4, 6, 7, 2, 4, 6, 7]

s = 0

for element in liste:
    s = s + element
    if s > 10:
        break
    
print(s)


