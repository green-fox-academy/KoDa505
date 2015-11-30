class MySuperString:
    def __init__(self, aszo):
        self.aszo = aszo


    def forditas(self):
        forditott = ''
        for i in self.aszo:
            forditott = i + forditott
        return forditott

    def szamolas(self, char):
        res = 0
        for i in self.aszo:
            if char in i:
                res += 1
        return res


    
