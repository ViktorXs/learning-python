# Einführung 1/2

def inner1():
    return "Hallo Welt!"


def outer1():
    return inner1  # Es wird nicht die Funktion ausgeführt, sondern als Funktion ausgegeben!


x = outer1()

print("Test1")
print(x)  # Funktion ausgeben -> x
print("Test2")
print(x())  # Funktion ausführen -> x()


# Einführung 2/2: Funktion in Funktion
def outer2():
    def inner2():
        return "Hallo Welt!"

    return inner2


x1 = outer2
print("Test3")
print(x1)
print("Test4")
print(x1())

# Decorator
def outer(func):
    def inner():
        print("inner() wurde ausgeführt")
    func()
    return inner


@outer  # Decorator gibt an, dass die darunterliegende Funktion do_something() vollkommen ignoriert wird und ...
# ... durch die outer3 Funktion ersetzt werden soll.
def do_something():
    print("do_something() wurde ausgeführt")

# Die do_something() Funktion wird als Parameter in outer3(func) eingefügt
do_something()


# Der decorator macht folgendes:
# do_something = outer(do_something)

# Wir bauen uns einen Cache
def cache(func):
    cached = {}

    def fill_cache(a):
        if a in cached:
            return cached[a]
        result = func(a)
        cached[a] = result
        return result
    return fill_cache


@cache
def calculations(a):
    print("calculations done(" + str(a) + ")")
    return a * a


print(calculations(6))

# Auf diesem Konzept beruhen Flasks routes zu den views: @app.route("/directory"), dass die Funktion in der View...
# ... ,nachdem die View-Dinge geladen sind, ausgeführt wird.

# Es geht aber noch weiter: Es lassen sich noch zusätzliche Parameter über den Decorator übergeben.
def outer_func(n):
    def decorator(func):
        def inner_func():
            for i in range(0, n):
                func()

        return inner_func
    return decorator

@outer_func(5)  # Mit Klammern --> () <-- dadurch kann ein zusätzlicher Parameter definiert werden.
def do_decor():
    print("do_decor() wurde ausgeführt")


do_decor()
