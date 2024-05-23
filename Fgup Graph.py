import math
import matplotlib.pyplot as plt
def plot_vertical_line2(x_value, min_value, min_list):
    plt.axvline(x=x_value, color='r', linestyle='--', ymax = 0.5 * 0.095)
    title = '$M_{f_{min}}$'
    plt.text(x_value, 0.043, title, rotation=45, verticalalignment='bottom', horizontalalignment='center', transform=plt.gca().transData, color='black')
   # print("%.2f" % min_value)

def Fonksiyon1(a, b):
    value_list = []
    Fgup = []
    M = []
    i = 0.04
    while i <= 0.30:
      result = i/2 + (1/(64*i) * ((4*a*i - b/2 - (b/(64*i*i) -a/(8*i) +1) * (-b/2 - (3*a*b)/(16*i) + 8*a*i - b * math.log10(16*i)) )) )
      if 0 < result < 0.15:
            Fgup.append(result)
            M.append(i)
            value_list.append((result, i))
      i = i + 0.001
    plt.plot(M, Fgup, label=f" \u03B1 = {a} \u03B2 = {b}", color='orange')
    if a == 0.5 and b == 0.01:
        # plot_vertical_line()
        # print(max(value_list)[1])
        plot_vertical_line2(min(value_list)[1], min(value_list)[0], min(value_list))


def Fonksiyon2(a, b):
    value_list = []
    Fgup = []
    M = []
    i = 0.07
    while i <= 0.30:
      result = i/2 + (1/(64*i) * ((4*a*i - b/2 - (b/(64*i*i) -a/(8*i) +1) * (-b/2 - (3*a*b)/(16*i) + 8*a*i - b * math.log10(16*i)) )) )
      if 0 < result < 0.15:
            Fgup.append(result)
            M.append(i)
            value_list.append((result, i))
      i = i + 0.001
    plt.plot(M, Fgup, label=f" \u03B1 = {a} \u03B2 = {b}")
    if a == 0.5 and b == 0.01:
        pass



Fonksiyon2(0, 0)
Fonksiyon2(0.5, 0.01)
Fonksiyon2(0.6, 0.02)
Fonksiyon2(0.7, 0.03)
Fonksiyon2(0.8, 0.05)

plt.xlabel('M')
plt.ylabel('Fgup')
plt.legend()
plt.savefig("fig2.png")
plt.show()

Fonksiyon1(0.5, 0.01)

plt.xlabel('M')
plt.ylabel('Fgup')
plt.legend()
plt.savefig("fig1.png")
plt.show()
