import math
import matplotlib.pyplot as plt

def plot_vertical_line2(x_value, min_value, min_list):
    plt.axvline(x=x_value, color='r', linestyle='--', ymax = 5.5 * 0.095)
    title = '$M_{Pmin}$'
    plt.text(x_value, 0.05 , title, rotation=45, verticalalignment='top', horizontalalignment='center', transform=plt.gca().transData, color='black')
   # print("%.2f" % min_value)

def Fonksiyon1(a, b):
    value_list = []
    Pgup = []
    M = []
    i = 0.003
    while i <= 0.8:
      r=2*i
      result =- 1/(math.pi * i*i *32) * (1 - (8*a)/(16*r) + (2*b)/(16*r*r))
      if -0.15 < result < 0.1:
            Pgup.append(result)
            M.append(i)
            value_list.append((result, i))
      i = i + 0.001
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.plot(M, Pgup, label=f" \u03B1 = {a} \u03B2 = {b}", color='orange')
    if a == 0.5 and b == 0.01:
        # plot_vertical_line()
        # print(max(value_list)[1])
        plot_vertical_line2(min(value_list)[1], min(value_list)[0], min(value_list))


def Fonksiyon2(a, b):
    value_list = []
    Pgup = []
    M = []
    i = 0.003
    while i <= 0.8:
      r=2*i
      result = - 1/(math.pi * i*i *32) * (1 - (8*a)/(16*r) + (2*b)/(16*r*r))
      if -0.15 < result < 0.1:
            Pgup.append(result)
            M.append(i)
            value_list.append((result, i))
      i = i + 0.001
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.plot(M, Pgup, label=f" \u03B1 = {a} \u03B2 = {b}")
    if a == 0.5 and b == 0.01:
        pass



Fonksiyon2(0, 0)
Fonksiyon2(0.5, 0.01)
Fonksiyon2(0.6, 0.02)
Fonksiyon2(0.7, 0.03)
Fonksiyon2(0.8, 0.05)

plt.xlabel('M')
plt.ylabel('Pgup')
plt.legend()
plt.savefig("fig2.png")
plt.show()

Fonksiyon1(0.5, 0.01)

plt.xlabel('M')
plt.ylabel('Pgup')
plt.legend()
plt.savefig("fig1.png")
plt.show()
