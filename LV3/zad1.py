import numpy as np
import pandas as pd

mtcars=pd.read_csv('mtcars.csv')


petnajvecih=mtcars.sort_values(by=['mpg'])
print(petnajvecih.tail(5))

osamcil=mtcars[mtcars.cyl==8]
osamcil=mtcars.sort_values(by=['mpg'])
print(osamcil.head(3))

sestcil=mtcars[mtcars.cyl==6]
print(sestcil['mpg'].mean())


cetiricil=mtcars[(mtcars.cyl==4) & (mtcars.wt>=2)&(mtcars.wt<=2.2)]
print(cetiricil['mpg'].mean())

amjenjac=mtcars[mtcars.am==0]
rmjenjac=mtcars[mtcars.am==1]
print(len(amjenjac))
print(len(rmjenjac))

print(len(mtcars[(mtcars.am==0)&(mtcars.hp>100)]))

mtcars['kg']=mtcars.wt*0.45*1000

print(mtcars)
