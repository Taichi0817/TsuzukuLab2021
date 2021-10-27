import pandas as pd
import matplotlib.pyplot as plt
from fractions import Fraction
import requests
import numpy as np
import random
import statsmodels.graphics.api as smg
from statsmodels.graphics.tsaplots import plot_acf

from assets import create_ideal_jjy
from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic',
                               'Noto Sans CJK JP']
noc  = 2
create = create_ideal_jjy.CreateIdealJJY()
ideal_signal = create.create_signal()
count = 0
cC = np.zeros(60)  # 相関演算の結果
tmp = 0
Error = 0  # 相関演算した時の誤り数



for j in range(60):
    for k in range(60):
        for l in range(8):
            for co in range(noc - 1, -1, -1):
                cC[k] += ideal_signal[j+co][l] * ideal_signal[k+co][l]

    fig = plt.figure()
    plt.xlabel('分', fontsize=14)
    plt.ylabel('相関係数', fontsize=14)
    plt.grid(which="both")
    plt.title('minute={}の場合の自己相関関数'.format(j))
    plt.plot(cC)
    plt.show()
    name_of_image = '{}分連続、minute={}の場合の自己相関関数'.format(noc, j)
    fig.savefig("images/{}分連続/{}".format(noc, name_of_image))
    cC = np.zeros(60)

BER = Error / 60
Error = 0

