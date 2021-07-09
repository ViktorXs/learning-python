print("BMI-Calculator")

weight = float(input("Please enter first your weight in kilograms: ").replace(",", "."))
height = float(input("And now your height in meters: ").replace(",", "."))

bmi_index = weight / height ** 2

print("Your BMI is: " + str(round(bmi_index, 2)))  # "round()"-Funktion aus Musterlösung eingefügt.
input("Thank you.")
