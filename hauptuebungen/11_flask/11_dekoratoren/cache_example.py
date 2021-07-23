def was(func):
    cached = {}

    def das(x):
        for x in cached:
            return cached[x]
        result = func(x)
        cached[x] = result
        return result
    return das

@was
def calculate(x):
    print("calculate " + str(x))  # Code z.B. aufwendige Berechnungen
    return x * x


print(calculate(12))
