# %%
import requests
import time
import datetime

import math
import matplotlib.pyplot as plt
import numpy as np

from assets import calculate_correlation
from assets import create_ideal_jjy
from assets import line_notify
from assets import make_noise


create = create_ideal_jjy.CreateIdealJJY()
ideal_signal = create.create_signal()
number_of_simulations = 600
cc = np.zeros(60) # 相関演算の結果
error = 0
ber = np.zeros((15, number_of_simulations//60))
for i in range(number_of_simulations//60):
    for cnr in range(5):
        std_dev = make_noise.out_standard_deviation(cnr)
        noise_signal = make_noise.make_noise(std_dev, ideal_signal)
        for k in range(60):
            for l in range(60): #   相関を計算
                for m in range(8): #    相関を計算
                    cc[l] += noise_signal[k][m] * ideal_signal[l][m]
            if cc[k] != np.amax(cc):
                error += 1
            # dfResult = np.inserdfdfResult, i, cC, axis=1)
            cc = np.zeros(60)
        ber[cnr, i] = error
        error = 0
print(ber)
print(np.mean(ber, axis=1))
b = np.sum(ber, axis=1)
c = b/number_of_simulations
fig = plt.figure()
ax = plt.gca()
ax.set_yscale('log')
plt.grid(which="both")
plt.plot(c)

plt.show()
dt_now = datetime.datetime.now()
name = dt_now.strftime('%Y年%m月%d日')
fig.savefig("image/img_{}.png".format(name))
line_notify.main()
