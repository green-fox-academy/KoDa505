def greet(name):
    return "hello, " + name

result = greet("Tomi")
print(result)

g = []
def add(a, b):
    res = a + b
    g.append(res)
    return res

print(add(1, 2))
print(add(7, 2))
print(g)


def add2(a, b, res = None):
    if res is None:
        res = []
    r = a + b
    res.append(r)
    print(res)
    return r
        
