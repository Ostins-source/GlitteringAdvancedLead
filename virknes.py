"""
vards = input("Kā tevi sauc? ")
print(f"Tavs vārds ir {vards}.")

gadi = int(input("Cik tev gadu? "))
print(f"Tev ir {gadi} gadi.")
dzimsGads=2021-gadi
print(f"Tavs dzimšanas gads ir {dzimsGads}.")
"""


#Uzraksti programmu, kas lietotājam lūdz ievadīt temperatūru pēc Celsija un izdrukā šo temperatūru pēc Ferenheita skalas. (T(*F) = T(*C) x 9/5 + 32)



celsijs = int(input("Kāda ir temperatūra pēc celsija? "))
ferenheiti = celsijs * 9 / 5 + 32
print(f"Temperatūra {celsijs} pēc Celsija skalas ir {ferenheiti} grādi pēc farenheita skalas.")



#Uzraksti programmu, kas uzdod 3 jautājumus par telpas izmēriem - platumu, garumu, augstumu. Aprēķini un izdrukā telpas tilpumu.

platums = float(input("Kāds ir platums? "))
garums = float(input("Kāds ir garums? "))
augstums = float(input("Kāds ir augstums?  "))
print(f"Tilpums ir {platums*garums*augstums}.")


#Strings (rakstzīmju virknes)
print("čau")
print('čau')
print("I'm going on a run")
print('Arī šis ir "risinājums"')
print("Darova, \nLamar!") #izdrukā divās rindās
print("Darova, \tAlbert!")#izdrukā ar "TAB" atkāpi

#String garums - len()
print(len("čau"))#izdrukā burtu skaitu
print(len("Digitālā datubāze “Zinātnes valoda” – labs palīgs skolēniem"))

# [sākums:beigas:solis]
myString="Darova, Lamar!"
print(myString)
print(myString[0]) #izdrukā 1. rakstzīmi
print(myString[8]) #izdrukā 9. rakstzīmi
print(myString[12]) #izdrukā 13. rakstzīmi
print(myString[-3]) #izdrukā 12. rakstzīmi
print(myString[-1]) #izdrukā 14. rakstzīmi (pēdējo)

myString= "abcdefghjklmnoprstuvz"
print(myString)
print(myString[2]) #izdrukā c
print(myString[2:]) #izdrukā no c burta uz priekšu
print(myString[:3]) #izdrukā līdz 2. indeksam (neietver galapunktu)
print(myString[3:6]) #izdrukā no d līdz f
print(myString[::]) #izdrukā no sākuma līdz beigām
print(myString[::2]) #izdrukā katru otro burtu
print(myString[2:7:2]) #izdrukā no 3. rakstzīmes līdz 7. rakstzīmei katru otro
print(myString[::-1]) #izdrukā visu pretējāvirzienā