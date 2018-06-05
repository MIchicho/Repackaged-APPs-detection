#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt



labels = "some differences","subtle differences","same",

sizes = [10,147,13101]

colors = ['dimgray','grey','gainsboro']

explode = (0.1,0.2,0.2)

fig1,ax1 = plt.subplots()

ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True,labeldistance=1.01,startangle=210)


ax1.axis('equal')


plt.xlabel('Pie graph of Event Handler sequence distance')

plt.show()


