def greet(name, lange = None):
    if lange is None:
        lange = "Hello"
    print(lange + ', ' + name)

greet('Mark', 'Ciao')
greet('Bela', 'Tschus')
greet('Gabi')
