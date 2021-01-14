"""Var rakstīt komentārus
vairākās
rindās"""
print("DAROVA!")
print(2*2)
print(2*2,2*3,2*4,2*5, "es")
print(f"Ja saskaitīsim 5 ar 7, tad iegūsim {5+7}.")#kombinētā izdruka - teksts un aprēķins
print ("dar"+"ova")
print( "Ostins Deņisenoks " *5 )
print(365 * 24 * 60 * 60, "sekundes")
print(0.1 + 0.2 - 0.3)
print( )

#Mainīgie
a = 5
print(a)
print(a + a)
a = a + a # Zīme = nozīmē piešķiršanu
print(a)
print(type(a))
a = 30.1
print(type(a))

mani_ienākumi=430
nodoklis=0.25 # 10%
maniNodkoli = mani_ienākumi * nodoklis
print(maniNodkoli)

#help
help("keywords")

#Datu ievade - input
#Pirmā versija
print("Ievadi vārdu: ")
x = input()
print("Tavs ievadītais vārds ir " + x)

#Otrā versija
x = input("Ievadi vārdu: ")
print("Tavs ievadītais vārds ir " + x)

#Skaitļu ievade
sk = int(input("Ievadi veselu skaitli: ")) #pārveido ievadīto datu tipu pat int
print(f"Tavs ievadītais skaitlis ir {sk}.")