import matplotlib.pyplot as plt
import pandas as pd


mtcars = pd.read_csv('mtcars.csv')

plt.subplot(2,2,1)
c=['pink','hotpink','pink']
mpg_by_cyl = mtcars.groupby('cyl')['mpg'].mean()
plt.bar(mpg_by_cyl.index, mpg_by_cyl.values, color=c)
plt.xlabel('Broj cilindara')
plt.ylabel('Potrošnja goriva (mpg)')



plt.subplot(2,2,2)
wt_by_cyl=mtcars.groupby('cyl')['wt']
#wt_by_cyl = [mtcars[mtcars['cyl']==cyl]['wt'] for cyl in [4, 6, 8]]
plt.boxplot(wt_by_cyl, labels=[4, 6, 8])
plt.xlabel('Broj cilindara')
plt.ylabel('Težina (t)')

plt.show()
