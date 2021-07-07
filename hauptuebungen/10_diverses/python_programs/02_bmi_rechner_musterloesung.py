print("BMI-Rechner")

weight_str = input("Bitte gebe dein Gewicht (in kg) ein: ")
height_str = input("Bitte gebe deine Körpergröße (in cm) ein: ")

weight = float(weight_str.replace(",", "."))
height = float(height_str.replace(",", "."))

bmi_index = weight / height ** 2

print("Der BMI ist: " + str(round(bmi_index, 1)))
input("Beliebige Taste zum Beenden des Programms drücken.")
