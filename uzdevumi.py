
#1. uzdevums
x = input("Ievadi jebkādu tekstu: ")
print(len(x))

#2. uzdevums
c = input("Ieavadi vārdu: ")
print(c[0])

#3. uzdevums
z = "Sveika, Pasaule!"
print(z[10:15])

#4. uzdevums
v = input("Ievadi jebkādu teikumu ar mazajiem burtiem: ")
print(v.upper())

#5. uzdevums
b = input("Ievadi jebkādu teikumu ar lielajiem burtiem: ")
print(b.lower())

#6. uzdevums
n = "samērcēt"

l = n.replace("s", "p")

print(l)

#7. uzdevums
m = "  Sveika, Pasaule!  "
print(m[2:18])

#8. uzdevums
#Aprēķina no naudas summas iztērēto un uz cik +naudas ir saņēmis
y=3.19
balance= float(input("Kāda ir naudas summa? "))
print(f"Tavs profits ir {balance-y}. ")
x2=balance-y
print(f"Atņemot naudu no operacijas tavs īstais profits ir {x2-12.75}. ")

#9. uzdevums
a = input("Ievadi savu vārdu: ")
input(a[::-1] + ". Pamatīgs juceklis, vai ne, ?")
print(f">:)")