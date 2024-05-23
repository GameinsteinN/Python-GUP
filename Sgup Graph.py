import math
import matplotlib.pyplot as plt
 
def Fonksiyon2(a, b):
    value_list = []
    Sgup = []
    M = []
    i = 0.001
    while i <= 0.20:
        r = 2 * i
        result = (1/4 * math.pi) * (8*r*r -b/2 - (3*a*b)/(8*r) + 4*a*r + b * math.log(8*r))
        if 0 < result < 2:  #grafiğin y ekseni sınırlarını belirliyoruz
            Sgup.append(result)
            M.append(i)
            value_list.append((result, i))
        i = i + 0.001
    plt.plot(M, Sgup, label=f" \u03B1 = {a} \u03B2 = {b}")
    

Fonksiyon2(0, 0)
Fonksiyon2(0.5, 0.01)
Fonksiyon2(0.6, 0.02)
Fonksiyon2(0.7, 0.03)
Fonksiyon2(0.8, 0.05)

plt.xlabel('M')
plt.ylabel('Sgup')
plt.legend()
plt.savefig("fig2.png")
plt.show()
