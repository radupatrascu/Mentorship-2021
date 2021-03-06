#Hello


#Ex.1 Printeaza Alexandru



#ex.2 Calculeaza 1 + 3
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility*
'''
np.random.seed(19680801)


N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2  # 0 to 10 point radii
c = np.sqrt(area)
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
# Show the boundary between the regions:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))

plt.show()
'''

#Bun de tot!!



#Se dau 3 sonde 1, 2, 3

# adancimi

AdSonde = [1000, 2000, 3000] # m
DensitateFluide = [1200, 800, 450] #kg/m3



# Presiunea hidrostatica = densitate * adancimea * accelartia -> Pa

def Hidrostatica(adSonda, densitate):
    """
    Calculeaza densitatea fluidului din sonda
    """
    accelartiaGrav = 9.8 #m/s2
    dens = adSonda * densitate * accelartiaGrav

    return dens


for (adancime, densitate) in zip(AdSonde,DensitateFluide):
    i=1
    press = Hidrostatica(adancime,densitate)/100000
    print("Pentru sonda 1, presiunea este de {press}")



## To do
'''
1. Printezi raspunsul astfel:

"Pentru sonda 1, presiunea este de 133 bar. "
'''