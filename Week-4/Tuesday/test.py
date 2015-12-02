from reverse import reversing  # ez a fajl neve es benne maganak a funkcionak a neve

from functions.bars import starbar #ezt abban az esetben kell alkalmazni, amikor a fajl egy masik mappaban van es a functiont onnan hozom at

print(reversing([3, 4, 5, 9,]))

starbar(5)

"""
import os #operating system

print(os.getpid())
print(os.getcwdb)
print(os.getcwd)
"""

alma_file = open('alma.txt') #ez csak olvasasi jog
print(alma_file.read())
print(type(alma_file.read()))
#print(len(alma_file.read()))


alma_file = open('alma.txt', 'w') # itt mar meg tudok adni egy irasi jogosultsagot. De akkor nem tudom kiolvasni a fajlt
alma_file.write('Maugli egyel meg \n ket banant')

alma_file.close()  # celszeru bezarni, mert 1. mas nem tudja addig bizgetni, 2. egy ido utan mar nem tud tobbet megnyitni

alma_file = open('alma.txt')
print(alma_file.readline())
print(alma_file.read())
alma_file.close()
