# daysperweek = int(input('一周多少天？'))
# hourperday = int(input('一天多少小时？'))
# MinutesPerHour = int(input('一小时多少分钟？'))
# MinutesPerWeek = daysperweek * hourperday * MinutesPerHour
# print(MinutesPerWeek)

#从网站上获取文件代码
# import urllib
# file = urllib.urlopen('http://helloworldbook.com/data/message.txt')
# message = file.read()
# print(message)


#嵌套循环，决策树
# print('  \t  Dog \tbug \tketchup \tMustard \tOnions')
# count = 1
# for dog in [0,2]:
#     for bun in [0,2]:
#         for ketchup in [0,2]:
#             for mustard in [0,1]:
#                 for onion in [0,2]:
#                     print('#',count,"\t",end="")
#                     print(dog,"\t",bun,"\t   ",ketchup,"\t          ",end="")
#                     print(mustard,"\t        ",onion)
#                     count = count +1

# def printmyaddress():
#     print("I",end="")#end=""在输出时，不换行
#     print("123 m ")
#     print("K2M 2E9")
#
# printmyaddress()
# printmyaddress()

# def calculateTax(price, tax_rate):
#      taxTotal = price + (price * tax_rate)
#      print(my_price)
#      my_price = 1000
#      print('my_price(inside function)=',my_price)
#      return taxTotal
# my_price = float(input('enter a price:'))
# totalprice = calculateTax(my_price,0.06)
# print('price = ',my_price,'\nTotal price = ',totalprice)
# print('my_price(outside function) = ',my_price)

#类的定义和使用
# class Ball:
#     def __init__(self,color,size,direction):
#         self.color = color
#         self.size = size
#         self.direction = direction
#     def __str__(self):
#         msg = "HI,I'M a "+ self.size+" "+ self.color + "ball!"
#
# myBall = Ball('red',"small","down")
# print(myBall)

#
# class Hotdog:
#     def __int__(self):
#         self.cooked_level = 0
#         self.cooked_string = "raw"
#         self.condiments = []
#
#     def __str__(self):
#         msg = "hot dog"
#         if len(self.condiments)>0:
#             msg = msg + "with"
#         for i in self.condiments:
#             msg = msg + i + ","
#         msg = msg.strip(",")
#         msg = self.cooked_string + " "+ msg+"."
#         return msg
#     def cook(self, time):
#         self.cooked_level = self.cooked_level+ time
#         if self.cooked_level > 8:
#             self.cooked_string = "charcoal"
#         elif self.cooked_level >5:
#             self.cooked_string = "well"
#         elif self.cooked_level > 3:
#             self.cooked_string = "medium"
#         else:
#             self.cooked_string ="raw"
#     def addcondiment(self,condiment):
#         self.condiments.append(condiment)
# mydog = Hotdog()
# print(mydog)
# print("cooking hot dog for 4 minutes...")
# mydog.cook(4)
# print("cooking hot dog for 3 more minutes...")
# mydog.cook(3)
# print(mydog)

#引入模块
# import my_module
# celsius = float(input("enter a temperature in celsius:"))
# fahrenheit = my_module.c_to_f(celsius)#模块中的变量
# print("that's ", fahrenheit,"degress fahrenheit")
# #_引入模块中的变量__（ ）_______________________________________________-
# from my_module import c_to_f  #如果导入所有变量：from my_module import *
# celsius = float(input("enter a temperature in celsius:"))
# fahrenheit = c_to_f(celsius)
# print("that's ", fahrenheit,"degress fahrenheit")

#画图
# import pygame,sys
# import math
# pygame.init()
#
# disp = pygame.display.set_mode([640,480])
# disp.fill([255,255,255])
# plotPoints = []
# for x in range(0,640):
#     y = int(math.sin(x/640.0 * 4 * math.pi)* 200 + 240)
#     plotPoints.append([x,y])
# pygame.draw.lines(disp, [0,0,0],True,dots,2)# 颜色另一种表示pygame.color.THECOLORS["red"]
# pygame.display.flip()
#
# while True:
#     for display in pygame.event.get():
#         if display.type ==pygame.QUIT:
#             sys.exit()

# import pickle
# my_list = ['fred',73,'hello',99]
# pickle_file = open('F:/notepad/my_pickle_list.pkl','w')
# pickle.dump(my_list,pickle_file)
# pickle_file.close()
# pickle_file = open('F:/notepad/my_pickle_list.pkl','r')
# recover_list = pickle.load(pickle_file)
# pickle_file.close()
# print(recover_list)


# my_file.write("eat supper\n")
# my_file.write("play soccer\n")
# my_file.close()
# my_file = open('F:/notepad/notes1.txt','w')
# my_file.write("supper\n")
# my_file.write("soccer\n")
# my_file = open('F:/notepad/notes1.txt','r')
# file = my_file.readlines()
# print(file)


#文件的附加和读
# filename = 'F:/notepad/pi_digits.txt'
# with open(filename,'a') as file_object:
#     file_object.write("i .\n")
#     file_object.write("creating.\n")
# with open(filename)as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))

#异常处理
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#       answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#          print("youcan't divide by zero") #或者pass ，什么也不输出，直接跳过该错误。
#     else:
#       print(answer)

#存储和读取数据
# import json
# filename = 'username.json'
# try:
#     with open(filename)as f_obj:
#         username = json.load(f_obj)  #读取数据
# except FileNotFoundError:
#     username = input("what is your name ?")
#     with open(filename,'w') as f_obj:
#         json.dump(username,f_obj)   #写数据
#         print("we'll rember you when you come back," +username+"!")
# else:
#     print("welcome back," + username+"!")

# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k, v in d.items():
# print(k, '=', v)

#画图示例
# import numpy as np
# import matplotlib.pyplot as plt
# from pylab import *
#
# x = np.linspace(-np.pi,np.pi,256,endpoint = True)
# C,S = np.cos(x),np.sin(x)
# plot(x,C)    #plt.plot()
# plot(x,S)
# show()       #plt.show()
##画图示例2
#import numpy as np
# import matplotlib.pyplot as plt
#
# t = np.arange(-1, 2, .01)
# s = np.sin(2 * np.pi *t)
#
# plt.plot((1,2,3),(4,3,-1))
# plt.show()
#
# plt.figure(figsize=(16,8),dpi=98)   #指定画图大小和精度
# plt.plot(t , s)
# l = plt.axhline(linewidth = 4, color = 'r')
# plt.axis([-1,2, -1,2])
# plt.show()
# plt.close()
#
# plt.plot(t,s)
# l = plt.axvline(x= 0 ,ymin=0, linewidth = 4,color ='b')
# plt.axis([-1,2,-1,2])
# plt.show()
# plt.close()
#
# plt.plot(t,s)
# l = plt.axhline(y=.5, xmin=0.25, xmax=0.75)
# plt.axis([-1, 2, -1, 2])
# plt.show()
# plt.close()
#
# plt.plot(t,s)
# p = plt.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
# p = plt.axvspan(1.25, 1.55, facecolor='g', alpha=0.5)
# plt.axis([-1, 2, -1, 2])
# plt.show()

# a_i_x = sum(c*c for c in data_acc_x) #求平方和
# a_i_y = sum(c*c for c in a_i_y)
# a_i_z = sum(c*c for c in a_i_z)
#
#
# s = 25    #求平方根
# a_i = np.sqrt(s)
# print(a_i)

#opencv 读图片
# import cv2
# import numpy as np
# img = cv2.imread("C:1.jpg")
# cv2.imshow("lena",img)
# cv2.waitKey(100000)
#
# import numpy as np
# group = [(1,2),(2,3),(3,4)]
# print(type(group),group)
# ar = np.array(group)
# print(type(ar))
# print(ar[:,1])    #ar = [x[0]for x in group]# ar.ndim 显示维度数

# ################################################################################################
# import  numpy as np
# from pylab import *
#
# file = open('F:/Python/acc.txt')
# data = file.readlines()
# data_acc_x = []
# data_acc_y = []
# data_acc_z = []
# for i in range(len(data)):
#     data_acc_x.append(float(data[i].split(',')[0].split('(')[1]))  #读.添加data中所有行的第一列 以逗号分隔取第0位置的字符，在以（分隔取位置1的字符，再转化为float型
#     #len_x = len(data_acc_x)
#     data_acc_y.append(float(data[i].split(',')[1]))
#     #len_y = len(data_acc_y)
#     data_acc_z.append(float(data[i].split(',')[2].split(')')[0]))
#     #len_z = len(data_acc_z)
# figure(figsize=(16,8),dpi=100)
# rcParams['font.sans-serif']=['SimHei'] #显示中文字符
# rcParams['axes.unicode_minus'] = False
# title("加速度x轴数据")
# plot(data_acc_x) #画出acc_x点曲线
# show()
#
# a_i_x=[]
# a_i_y = []
# a_i_z = []
# i = 0
# for i in range(len(data_acc_x)):
#     a_i_x.append (data_acc_x[i] ** 2)
#     a_i_y.append(data_acc_y[i]**2)
#     a_i_z.append(data_acc_z[i]**2)
#     i = i + 1
# #print(a_i_x) #验证列表中每项的平方
# #print(a_i_y)
# #print(a_i_z)
#
# a_i = []
# i = 0
# for i in range(len(a_i_x)):
#     a_i.append(np.sqrt(a_i_x[i]+a_i_y[i]+a_i_z[i]))
#     i += 1
# print("加速度ai数据值列表",a_i)
# figure(figsize=(16,8),dpi=100)
# plot(a_i)
# show()
#
# gam_a_i=[]
# a_j = []
# a_j_mean = []
# i = 0
# for i in range(len(a_i)):
#     if i >= 14:
#         a_j.append(a_i[(i+1)-15])
#         a_j_mean.append((1/31)*(sum(a_i[(i+1)-15:(i+1)+15])))  #求出aj平均数
#     i = i+ 1
# print("aj数据值列表：",a_j)
# print("均值aj数据值列表",a_j_mean)
# j = 0
# for j in range(len(a_j)):
#     gam_a_i.append ((1 / 31) * (sum ((a_j[j] - a_j_mean[j])) ** 2))
#     j = j+1
# print("gama数据值列表：",gam_a_i)
# plot(gam_a_i)
# title("ACC variance grape")
# show()
#
# T1 = 2
# T2 = 1
# B1i = []
# i = 0
# for i in range (len(gam_a_i)):
#     if T1 < gam_a_i[i]:
#         B1i.append(T1)
#     else:
#         B1i.append(0)
#     i = i+ 1
# print(B1i)
# figure(figsize=(16,8),dpi=100)
# plot(B1i)
# show()
# # 步数统计
# i = 1
# j = 0
# for i in range(len(B1i)):
#     if B1i[i -1] != B1i[i]:
#         j = j + 1
#     else:
#         j = j
#     i = i + 1
# step = j / 2
# print(step)
############################################################
import numpy as np
from pylab import *
file = open('F:/Python/步频数据/acc-2-1.txt','r')
data = []
for line in file:
    if line != "\n":    #去除数据表中所有空行，
        data.append(line)   #如果该行不为空，将该行添加到data新列表里
   # print(data)
    #print(len(data))
#print(data[9])
data_lacc_x = []
data_lacc_y = []
data_lacc_z = []
for i in range(len(data)):
    data_lacc_x.append(float(data[i].split(',')[3]))
    data_lacc_y.append(float(data[i].split(',')[5]))
    data_lacc_z.append(float(data[i].split(',')[7]))
# print(data_lacc_x)
# print(len(data_lacc_x))
# figure(figsize=(16,8),dpi=200)
# rcParams['font.sans-serif']=['SimHei'] #显示中文字符
# rcParams['axes.unicode_minus'] = False
# title("线加速度x轴数据")
# plt.plot(data_lacc_x,'r',label = "lacc_x" ) #画出acc_x点曲线
# plt.plot(data_lacc_y)
# plt.legend()    # 显示图中标签
# plt.show()

la_i_x=[]
la_i_y = []
la_i_z = []
i = 0
for i in range(len(data_lacc_x)):
    la_i_x.append(data_lacc_x[i] ** 2)
    la_i_y.append(data_lacc_y[i]**2)
    la_i_z.append(data_lacc_z[i]**2)
    i = i + 1
#print(a_i_x) #验证列表中每项的平方
#print(a_i_y)
#print(a_i_z)
la_i = []
i = 0
for i in range(len(la_i_x)):
    la_i.append(np.sqrt(la_i_x[i]+la_i_y[i]+la_i_z[i]))
    i += 1
print("线性加速度lai数据值列表",la_i)
# figure(figsize=(16,8),dpi=100)
# plot(la_i)
# show()

gam2_la_i=[]
gam_la_i = []
la_j = []
la_j_mean = []
i = 0
w = 10
for i in range(len(la_i)):
    if i >= 14:
        la_j.append(la_i[(i+1)-w])
        la_j_mean.append((1/(2*w+1))*(sum(la_i[(i+1)-w:(i+1)+w])))  #求出aj平均数
    i = i+ 1
print("laj数据值列表：",la_j)
print("均值laj数据值列表",la_j_mean)
          # j = 0
          # for j in range(len(la_j)):
          #      gam2_la_i.append ((1 / 31) * (sum ((la_j[j] - la_j_mean[j])) ** 2))
          #      gam_la_i.append(np.sqrt((1 / 31) * (sum ((la_j[j] - la_j_mean[j])) ** 2)))
          #      j = j+1
          # print("gama2_la数据值列表：",gam2_la_i)
          # print("gama_la数据值列表：",gam_la_i)
          # plot(gam2_la_i)
          # title("ACC variance grape")
          # show()
            ####阈值判断
            # T1 = 2
            # T2 = 1
            # B1i_la = []
            # B2i_la = []
            # i = 0
            # for i in range (len(gam_la_i)):
            #     if T1 < gam_la_i[i]:
            #         B1i_la.append(T1)
            #     else:
            #         B1i_la.append(0)
            #     i = i+ 1
            # for i in range(len(gam_la_i)):
            #     if T2 > gam_la_i[i]:
            #         B2i_la.append(T2)
            #     else:
            #         B2i_la.append(0)
            #     i = i + 1
            # print(B1i_la)
            # print(B2i_la)
            # figure(figsize=(16,8),dpi=100)
            # plot(B1i_la)
            # show()
                    #     # 步数统计
                    #     i = 1
                    #     step = 0
                    #     for i in range(len(B1i_la)):
                    #         if B1i_la[i-1]< B1i_la[i] and max(B2i_la[i-1:i+14]) == T2:
                    #             step = step + 1
                    #         else:
                    #             step = step
                    #         i = i+1
                    #     step = step/2
                    #     print(step)
#阈值判断
T1 = 10.2   #T1 = 12
T2 = 1
B1i_la = []
B2i_la = []
i = 0
for i in range (len(la_j_mean)):
    if T1 < la_j_mean[i]:
        B1i_la.append(T1)
    else:
        B1i_la.append(0)
    i = i+1
print(B1i_la)
#统计步数
i = 1
j = 0
for i in range(len(B1i_la)):
    if B1i_la[i -1] != B1i_la[i]:
        j = j + 1
    else:
        j = j
    i = i + 1
step = j / 2
print(step)
figure(figsize=(20,8),dpi=100)
rcParams['font.sans-serif']=['SimHei'] #显示中文字符
rcParams['axes.unicode_minus'] = False

config = {
    "font.family":'Time New',  # 设置字体类型
    #"font.size": ,
#     "mathtext.fontset":'stix',
}
rcParams.update(config)

###改变XY轴的刻度字体大小
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (24, 15),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
#params = {'axes.labelsize': 16,
#          'axes.titlesize': 16}
plt.rcParams.update(params)



plt.xlabel('Time steps(1/40s)',size = 20)#横坐标命名
plt.ylabel('Data value',size = 20)
x=np.arange(0,7)
plt.axis([0,2000,-0.5,59])

plot(la_i,'k',label ='Synthetic acceleration data',markersize=10)#线性加速度ai
plot(la_j_mean,'lime',label = 'Local variance',markersize=10)
#plot(gam_la_i,'g',label = 'gam_la_i')#加速变化方差图
plot(B1i_la,'b',label = 'Steps detection',markersize=10)

# plot(B2i_la,'m',label = 'B2i_la')
plt.legend(loc='upper left',fontsize=16)#标签显示位置和大小
plt.subplots_adjust(top=0.986, bottom=0.08, right=0.982, left=0.045, hspace=0, wspace=0)
plt.savefig("Irregular step detection.eps", dpi = 200)
#plt.legend()
plt.show()
# show()
# plot(gam_la_i) #
# title("ACC variance grape")
# show()





