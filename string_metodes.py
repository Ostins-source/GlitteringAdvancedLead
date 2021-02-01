"""
#string metodes
vards="Man" #ko darīt, lai nomainītu uz "Gan"?
ped_burti=vards[1:]
print(ped_burti)
print('G'+ped_burti) #string konkatinācija
"""
x="Darova, Lamar! "
x= x+ 'Kā klājas?'
print(x)

print(5+6)
print("5"+"6")#nedrīkst saskaitīt string ar skaitļiem

print(x.upper()) #uzraksta ar lielajiem burtiem
print(x.lower()) #uzraksta ar mazajiem burtiem
x2= x.upper()
print(x2)

print(x.split())#sadala visu pa daļām, izmantojot atstarpi
print(x.split("a")) #sadala visu pa daļām, izmantojot burtu "a"
print(x2.split())
