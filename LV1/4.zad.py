sum=0
counter=0
datoteka_ime=input("Unesite ime datoteke ")
path="C:\\Users\\Lea\Desktop\\PSU_LV1\\" + datoteka_ime
dat=open(path, 'r')

for line in dat:
    line=line.rsplit()
    if "X-DSPAM-Confidence:" in line:
        counter+=1
        sum+=float(line[1])

print("Average X-DSPAM-Confidence: ", sum/counter)
dat.close()
