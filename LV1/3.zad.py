lst=[]
sum=0

while True:
   element=input()
   if element=="Done" or element.isdigit():
      if element.isdigit():
         lst.append(element)
         sum+=int(element)
      if element == "Done":
         break
   else:
      print("Pogresan unos")

print("Ukupno brojeva: ",len(lst))
print("Srednja vrijednost: ",float(sum/len(lst)))
print("Minimalna vrijednost: ",min(lst))
print("Maksimalna vrijednost: ",max(lst))
print(sorted(lst))

   
