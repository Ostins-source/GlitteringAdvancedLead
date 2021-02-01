#lists vai saraksts
#[1,2,3,[4,5]]
myList=["teksts", 100, 12.8, "vēl teksts"]
print(myList)
print(len(myList))
mylist=["viens", 'divi', "trīs", "četri"]
print(mylist[0]) #izdrukā pirmo elementu (ar indeksu 0)
print(mylist[1:]) #izdrukā no otrā elementa jeb 1. indeksa uz priekšu

#var konkatinēt (apvienot)
cits_list= ["pieci", "seši"]
print(mylist + 
 cits_list) #izdrukā sarakstu apvienojumu, bet neizmaina pašus sarakstus
jauns_list= mylist+cits_list
print(jauns_list)
jauns_list[0] = 1 #definē pirmo elementu (aiztāj iepriekšējo)
print(jauns_list)

#elementu pievienošana
jauns_list.append("septiņi")
print(jauns_list)
jauns_list.append(8)
print(jauns_list)

#elementu noņemšana
jauns_list.pop() #noņem pēdējo elementu
print(jauns_list)
pop_element = jauns_list.pop()
print(pop_element)
jauns_list.pop(3) #noņem elementu ar norādīto indeksu
print(jauns_list)

#elementu krtošana
new_list = ['b', 'a', 'z', 'e']
print(new_list)
new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)
num_list = [4, 1, 8, 3]
print(num_list)
num_list.reverse()
print(num_list)
num_list.sort()
print(num_list)
s = [1, 2, 3, 100, 3.59]
s.sort()
print(s)

#saraksts sarakstā (nested)
nested_list = [8, 6, [5, 7]]
print(len(nested_list))
print(nested_list[1])
print(nested_list[2][1]) #izdrukā ligzdsaraksta elementu

#piemēri
augli = ["ābols", "banāns", "gurķis"]
print(augli[2])
#aiztāt elementu - gurķis -> apelsīns
augli[2]="apelsīns"
print(augli)
#pievienot beigās "bumbieris"
augli.append("bumbieris")
print(augli)
#iespruast konkrētā vietā jaunu elementu "citrons"
augli.insert(2,"citrons")
print(augli)
#izņemt no saraksata "banāns"
augli.pop(1)
print(augli)
#izdrukāt pilnāteikumā, cik augļi ir sarakstā
print(f"Šajā sarakstā ir {len(augli)} augli")