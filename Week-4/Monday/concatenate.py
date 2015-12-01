ag = 'kuty'

def concatenate(text):
    return text + 'a'

ag = concatenate(ag)

print(ag)

ag2 = ['rep', 'macsk', 'cic', 'alm', 'kacs']


for i in range(len(ag2)):
    ag2[i] = concatenate(ag2[i])

print(ag2)


"""
Ez itt azert nem jo, mert nem nyulsz konkretan a taghoz,  nem irod felul.
for i in ag2:
    i = concatenate(i)

print(ag2)

"""

   
