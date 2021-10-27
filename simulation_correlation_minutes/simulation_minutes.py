import requests
import time
import datetime

import math
import matplotlib.pyplot as plt
import numpy as np
import pprint

from assets import create_ideal_jjy
from assets import make_noise
from assets import calculate_correlation
from assets import line_notify


start = time.time()
n = 120
noc =  2 #number_of_consecutive何分連続するか
roc = 12     # range_of_cnr   CNの範囲設定
create = create_ideal_jjy.CreateIdealJJY(n)
ideal_signal = create.create_signal()
number_of_simulations = 10000
cc = np.zeros(60)
error = 0
ber = np.zeros((roc, number_of_simulations//60))
for i in range(number_of_simulations//60):
    for cnr in range(roc):
        std_dev = make_noise.out_standard_deviation(cnr)
        noise_signal = make_noise.make_noise(std_dev, ideal_signal, n)
        for j in range(60):
            for k in range(60):
                for l in range(8):
                    for co in range(noc-1, -1, -1):
                        cc[k] += ideal_signal[j+co][l] * noise_signal[k+co][l]
            if cc[j] != np.amax(cc):
                error += 1
            cc = np.zeros(60)
        ber[cnr, i] = error
        error = 0
# print(ber)
# print(np.mean(ber, axis=1))
b = np.sum(ber, axis=1)
c = b / number_of_simulations
dt_now = datetime.datetime.now()
elapsed_time = time.time() - start
elapsed_time = round(elapsed_time)
td = datetime.timedelta(seconds=elapsed_time)
fig = plt.figure()
ax = plt.gca()
ax.set_yscale('log')
plt.grid(which="both")
plt.title('{0}分連続、{1}回、実行時間{2}'.format(\
    noc, number_of_simulations, td),\
    fontname="MS Gothic", fontsize=18)
plt.ylabel('SER', fontsize=14)
plt.xlabel('C/N[dB]', fontsize=14)
plt.plot(c)

plt.show()

name = dt_now.strftime('%Y,%m,%d,_%H,%M')
name_of_image = "img_{0}分連続_{1}回_{2}.png".format(noc, number_of_simulations, name)
fig.savefig("images/{}".format(name_of_image))
line_notify.main_gazo(name_of_image)

print ("elapsed_time:{}".format(td))
print(c)