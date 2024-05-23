import math
import matplotlib.pyplot as plt
def plot_vertical_line2(x_value, max_value, min_list):
    title = '$Phase Transition$'
    plt.text(0.1, -29.01, title, rotation=90, verticalalignment='bottom', horizontalalignment='center',
             transform=plt.gca().transData, color='black')
   # print("%.2f" % max_value)

def Fonksiyon1(a, b):
    value_list = []
    Cgup = []
    M = []
    i = 0.001
    while i <= 1:
        result = -(((16 * math.pi * i**3) * (b / (64 * i**3) - (a / (8 * i)) + 1) * (8 * a + ((3 * a * b) / (16 * i*i)) - (b / i) + 64 * i)) / (3 * b + 64 * i*i - 16 * i * a))
        if -50 < result < 20:
            Cgup.append(result)
            M.append(i)
            value_list.append((result, i))
        i = i + 0.001
    plt.plot(M, Cgup, label=f" \u03B1 = {a} \u03B2 = {b}", color='orange')
    if a == 0.5 and b == 0.01:
        # plot_vertical_line()
        # print(max(value_list)[1])
        plot_vertical_line2(max(value_list)[1], max(value_list)[0], min(value_list))


def Fonksiyon2(a, b):
    value_list = []
    Cgup = []
    M = []
    i = 0.001
    while i <= 1:
        result = -(((16 * math.pi * i**3) * (b / (64 * i**3) - (a / (8 * i)) + 1) * (8 * a + ((3 * a * b) / (16 * i*i)) - (b / i) + 64 * i)) / (3 * b + 64 * i*i - 16 * i * a))
        if -50 < result < 20:
            Cgup.append(result)
            M.append(i)
            value_list.append((result, i))
        i = i + 0.001
    plt.plot(M, Cgup, label=f" \u03B1 = {a} \u03B2 = {b}")
    if a == 0.5 and b == 0.01:
        pass


Fonksiyon2(0, 0)
Fonksiyon2(0.5, 0.01)
Fonksiyon2(0.6, 0.02)
Fonksiyon2(0.7, 0.03)
Fonksiyon2(0.8, 0.05)

plt.xlabel('M')
plt.ylabel('Cgup')
plt.legend()
plt.savefig("fig2.png")
plt.show()

Fonksiyon1(0.5, 0.01)

plt.xlabel('M')
plt.ylabel('Cgup')
plt.legend()
plt.savefig("fig1.png")
plt.show()
