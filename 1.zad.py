radni_sati=int(input("Radni sati: "))
eura_h=float(input("eura/h: "))
ukupno=radni_sati*eura_h
print("Ukupno:",ukupno, "eura")

def total_euro(radni_sati,eura_h):
    return radni_sati*eura_h

ukupno=total_euro(radni_sati,eura_h)
print("Ukupno:",ukupno, "eura")