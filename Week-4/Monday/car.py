#lehet egy fuggvenyt irni, hogy barmikor tudja egy ujabb kocsit letrehozni
def initCar(color, type, km):
    car = {'color': '', 'type': '', 'km': 0}
    car['color'] = color
    car['type'] = type
    car['km'] = km
    return car

#ezzel a rovid sorral lehet egy uj kocsit megcsinalni
lada = initCar('red', 'Lada 1200', 40000)

def ride(car, km):
    car['km'] += km

""" es akkor erre mar nincsen szukseg
lada = {
    'color': 'red',
    'type': 'Lada 1200',
    'km': 40000
}"""

tesla = {
    'color': 'pink',
    'type': 'Tesla S',
    'km': 1200
}

ifa = initCar('brown', 'Ifa', 300000)

ride(tesla, 220)
ride(ifa, 2500)
print(tesla)
print(ifa)
