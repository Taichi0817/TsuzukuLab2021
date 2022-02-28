import numpy as np
import matplotlib.pyplot as plt
from simulation_correlation_minutes.assets import create_ideal_jjy

n = 120
noc = 2
a = np.zeros(60)
cc = np.zeros(60)
create = create_ideal_jjy.CreateIdealJJY(n)
ideal_signal = create.create_signal()
noise_signal = np.load(r"C:\Users\ofdm\Documents\TaichiMorioka\TsuzukuLab2021\actualization\np_save.npy")
error = 0
for i in range(60):
    for j in range(60):
        for k in range(60):
            for l in range(8):
                for co in range(i, -1, -1):
                    cc[k] += ideal_signal[j + co][l] * noise_signal[k + co][l]
        if cc[j] != np.amax(cc):
            error += 1
        cc = np.zeros(60)
    a[i] = error
    error = 0
plt.ylabel('エラー回数', fontname="MS Gothic", fontsize=14)
plt.xlabel('連続する分の長さ[分]',fontname="MS Gothic", fontsize=14)
plt.grid(which="both")
plt.plot(a)
plt.show()
print(a)