# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 20:25:48 2016

@author: volvic
"""

import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import time

"""
横軸に犯罪のカテゴリー, 縦軸に犯罪数をヒストグラムでプロット。
縦軸にPdDistrictの内訳を表示
45分ほどかかる。
"""

df = pd.read_csv('.../data/train.csv', header = 0)
print "Start..."
## 不要列の削除
train_off_list = ["Dates", "Resolution", "X", "Y",
                  "Descript", "Address", "DayOfWeek"]
df = df.drop(train_off_list, axis = 1)

## カテゴリーに番号付け
catego = {}
cnt = 0
for i in np.unique(df.Category.values):
    catego[i] = cnt
    cnt += 1
dict = {"Category" : catego}
df = df.replace(dict)

## PdDistrictに番号付け
pddist = {}
cnt = 0
for i in np.unique(df.PdDistrict.values):
    pddist[i] = cnt
    cnt += 1
dict = {"PdDistrict" : pddist}
df = df.replace(dict)


## グラフ作成用のDataFrameを作成
## 39列, 10行の new_df を作成. 値は0

new_df = DataFrame(0,
                   columns = ["BAYVIEW", "CENTRAL", "INGLESIDE", "MISSION",
                              "NORTHERN", "PARK", "RICHMOND", "SOUTHERN",
                              "TARAVAL", "TENDERLOIN", "Total"],
                    index = ['ARSON', 'ASSAULT', 'BAD CHECKS', 'BRIBERY',
                             'BURGLARY', 'DISORDERLY CONDUCT', 'DRIVING UNDER THE INFLUENCE',
                             'DRUG/NARCOTIC', 'DRUNKENNESS', 'EMBEZZLEMENT',
                             'EXTORTION', 'FAMILY OFFENSES', 'FORGERY/COUNTERFEITING',
                             'FRAUD', 'GAMBLING', 'KIDNAPPING', 'LARCENY/THEFT',
                             'LIQUOR LAWS', 'LOITERING', 'MISSING PERSON',
                             'NON-CRIMINAL', 'OTHER OFFENSES', 'PORNOGRAPHY/OBSCENE MAT',
                             'PROSTITUTION', 'TRESPASS', 'ROBBERY',
                             'RUNAWAY', 'SECONDARY CODES', 'SEX OFFENSES FORCIBLE',
                             'SEX OFFENSES NON FORCIBLE', 'STOLEN PROPERTY',
                             'SUICIDE', 'SUSPICIOUS OCC', 'TREA',
                             'TRESPASS', 'VANDALISM', 'VEHICLE THEFT',
                             'WARRANTS', 'WEAPON LAWS'])

##条件があったときは, new_df の該当行列に 1 を追加する

#leng = df["PdDistrict"].count()
## テスト用
leng = 200
t1 = time.time()
for i in range(leng):
    if i == int(leng*0.2):
            t2 = time.time()
            print "20% Done.", ("Time:{0}".format(t2-t1)) + "[sec]"
    elif i == int(leng*0.4):
        t2 = time.time()
        print "40% Done.", ("Time:{0}".format(t2-t1)) + "[sec]"
    elif i == int(leng*0.5):
        t2 = time.time()
        print "50% Done.", ("Time:{0}".format(t2-t1)) + "[sec]"
    elif i == int(leng*0.7):
        t2 = time.time()
        print "70% Done.", ("Time:{0}".format(t2-t1)) + "[sec]"
    elif i == int(leng*0.9):
        t2 = time.time()
        print "90% Done.", ("Time:{0}".format(t2-t1)) + "[sec]"
    for j in range(0, 39):
        for k in range(0, 10):
            if df["Category"][i] == j  and df["PdDistrict"][i] == k:
                new_df.ix[j, k] = new_df.ix[j ,k] + 1.0

## 規準化する場合は True
if False:
    for i in range(0, 39):
        for j in range(0, 10):
            new_df.ix[i, 10] = new_df.ix[i, 10] + new_df.ix[i, j]

    for i in range(0, 39):
        for j in range(0, 10):
            new_df.ix[i, j] = new_df.ix[i, j] / new_df.ix[i, 10]

# Totalの行を削除
new_df = new_df.drop("Total", axis = 1)

## グラフの作成
## colorの設定 1ずつ, 10個の色を作成
colors = plt.cm.GnBu(np.linspace(0, 1, 10))
ax = new_df.plot(figsize = (12,8), title = "All Category - PdDistrict", kind = "bar", stacked = True, color = colors, fontsize = 10)
ax.set_ylabel("Number Of Crime")
ax.legend(loc = "center right", bbox_to_anchor = (1.23, 0.5))
if False:
    #規準化の場合はTrue
    ax.set_ylim(0, 1)
plt.show()
