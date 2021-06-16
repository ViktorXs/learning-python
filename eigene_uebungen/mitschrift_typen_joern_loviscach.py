# Typen in Python von Jörn Loviscach
from __future__ import annotations
import math
import typing

def solve(p: float, q: float) -> typing.Set[float]:
    u = - 0.5 * p
    d = u ** 2 - q
    if d < 0.0:
        return set()
    elif d < 1e-10:
        return { u }
    else:
        s = math.sqrt(d)
        return { u + s, u - s }

a = solve("ABC", True)
b = solve(13.0, 42.0)
c = b + 1
d = len(b)
e = b.pop()
f: float
f = b
f = b.pop()

g: bool
h: int
i: float
i = 13.0 + 23.0j
j: complex
j = 13.0 + 23.0j
k: str

def output(x: str) -> None:
    print(x)

class Point:
    _x: float
    _y: float

    @typing.overload
    def __init__(self, x: float, y: float) -> None:
        ...

    @typing.overload
    def __init__(self, p: Point) -> None:
        ...

    def __init__(self, *args: typing.Any) -> None:
        if len(args) == 2:
            self._x = args[0]
            self._y = args[1]
        else: 
            self._x = args[0]._x
            self._x = args[0]._y
    
    def shift(self, delta_x: float, delta_y: float) -> None:
        self._x += delta_x
        self._y += delta_y

p: Point
p = 23.0
p = Point(3.0, 23.0)
p = Point(p)

q: typing.List[Point]
q = [p, p, p]

r: typing.Tule[int, Point, str]
r = [13, p, "ABC"]
r = (13, p, "ABC")

s: typing.Dict[str, int] = {}
s[13] = "ABC"
s["ABC"] = 13

t: typing.Any
t = 13
t = p
t = s

def root(x: float) -> typing.Optional[float]:
    if x > 0.0:
        return math.sqrt(x)
    else:
        return None

u = root(23.0)
if u is not None:
    v = u + 1