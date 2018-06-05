#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt

labels = '0.30~0.62',"0.1~0.30",'0~0.09','0'

labels = "0~0.09","0.1~0.30","0.30~0.62","0"

sizes = [1489,630,135,9531]

colors = ['dimgray','grey','gainsboro','silver']

explode = (0,0,0,0.1)

fig1,ax1 = plt.subplots()

ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=False,labeldistance=1.1,startangle=90)


ax1.axis('equal')


plt.xlabel('Pie graph of Activity sequence distance')

plt.show()


