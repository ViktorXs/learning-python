example = "There is something wrong over here. I can feel it!"

# .upper() & .lower()
print(example)
print(example.lower())
print(example.upper())


# .startswith() & .endswith()
def check_if():
    if example.startswith("There") and example.endswith("it!"):
        print("The string is correct")
    else:
        print("Wrong string")


check_if()


# .strip(), .lstrip() & .rstrip()
print(example.strip("ehirtT!"))
print(example.lstrip(" ehrT"))
print(example.rstrip(" acint!"))


# .find()
print(example.find("is"))
print(example.find("were"))

# .replace()
print(example.replace("wrong", "right"))


# Übung
print(example.lower().replace(" ", "_").replace(".", ";").replace("!", ";"))


## Strings formatieren ##

# format()