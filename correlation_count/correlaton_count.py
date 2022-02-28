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
temp = [1]

for a in temp:
    print('{}分連続'.format(a))
    for j in range(60):
        for k in range(60):
            for l in range(8):
                for co in range(a - 1, -1, -1):
                    cC[k] += ideal_signal[j+co][l] * ideal_signal[k+co][l]
        count += np.count_nonzero(cC == a * 4)
        print(count)
        cC = np.zeros(60)
    print('{:.2}'.format(count/60))
    count = 0
BER = Error / 60
Error = 0

