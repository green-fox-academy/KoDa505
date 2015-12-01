class Car:
    def __init__(self, color, cartype, km):
        if type(color) != str:    #hibat dob, ha nem stringet adok be neki mint szin
            raise Exception('Color is not a string')
        self.color = color  # propertyk
        self.cartype = cartype
        self.km = km

    def ride(self, km):
        self.km += km

    def getMiles(self):
        return self.km * 0.6213

# object, objektum, instance

tesla = Car('pink', 'Tesla S', 1200)  #ha meghivom a fuggvenyt csak azzal a teslaval, akkor az egy ures objektum lesz
tesla.ride(210)

tesla.has_eyebrows = True   #mindig lehet egyes objektumoknak plusz tulajdonsagokat beadni

print(tesla.km)
