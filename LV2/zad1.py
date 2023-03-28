import numpy as np
import matplotlib.pyplot as mp

x=np.array([1,2,3,3,1])
y=np.array([1,2,2,1,1])

mp.plot(x,y, marker=".",markersize=10)
mp.axis([0,4,0,4])
mp.title("Primjer")
mp.xlabel("x os")
mp.ylabel("y os")
mp.show()
