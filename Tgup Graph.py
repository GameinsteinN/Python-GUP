import math
import matplotlib.pyplot as plt



def plot_vertical_line2(x_value, max_value, min_list):
    plt.axvline(x=x_value, color='r', linestyle='--', ymax = 10 * 0.095)
    title = '$M_{ph}$'
    scnd_title = '$M_{remnant}$'
    plt.text(x_value, -0.01, title, rotation=45, verticalalignment='bottom', horizontalalignment='center', transform=plt.gca().transData, color='black')
    plt.text(min_list[1], -0.01, scnd_title, rotation=45, verticalalignment='bottom', horizontalalignment='center', transform=plt.gca().transData, color='black')
   # print("%.2f" % max_value)
    



def Fonksiyon1(a,b):
  value_list=[]
  Tgup=[]
  M=[]
  i = 0.001
  while i <= 1:
    result = (1 / (16 * math.pi * i)) * (1 - (a / (8 * i)) + (b / (64 * i * i)))
    if  result > 0 and result < 0.1 :
      Tgup.append(result)
      M.append(i)
      value_list.append((result,i))
    i = i + 0.001
  plt.plot(M,Tgup, label= f" \u03B1 = {a} \u03B2 = {b}", color = 'orange' )
  if  a == 0.5 and b == 0.01:
      #plot_vertical_line()
      #print(max(value_list)[1])
      plot_vertical_line2(max(value_list)[1], max(value_list)[0], min(value_list))


def Fonksiyon2(a,b):
  value_list=[]
  Tgup=[]
  M=[]
  i = 0.001
  while i <= 1:
    result = (1 / (16 * math.pi * i)) * (1 - (a / (8 * i)) + (b / (64 * i * i)))
    if  result > 0 and result < 0.1 :
      Tgup.append(result)
      M.append(i)
      value_list.append((result,i))
    i = i + 0.001
  plt.plot(M,Tgup, label= f" \u03B1 = {a} \u03B2 = {b}")
  if  a == 0.5 and b == 0.01:
    pass



i = 0.17

Fonksiyon2(0,0)
Fonksiyon2(0.5,0.01)
Fonksiyon2(0.6,0.02)
Fonksiyon2(0.7,0.03)
Fonksiyon2(0.8,0.05)

plt.xlabel('M')
plt.ylabel('Tgup')
plt.legend()
plt.savefig("fig2.png")
plt.show()


Fonksiyon1(0.5,0.01)

plt.xlabel('M')
plt.ylabel('Tgup')
plt.legend()
plt.savefig("fig1.png")
plt.show()