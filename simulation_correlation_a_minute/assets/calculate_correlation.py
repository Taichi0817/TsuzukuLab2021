import numpy as np


from assets import make_noise


cc = np.zeros(60) # 相関演算の結果
error = 0
ber = np.zeros((15, 100))
def calculate_correlation(noise_signal, ideal_signal):
    for i in range(100):
        for cnr in range(15):
            std_dev = make_noise.out_standard_deviation(cnr)
            noise_signal = make_noise.make_noise(std_dev, ideal_signal)
            for k in range(60):
                for l in range(60):  # 相関を計算
                    for m in range(8):  # 相関を計算
                        temp = noise_signal[k][m] * ideal_signal[l][m]
                        cc[l] += temp
                if cc[k] != np.amax(cc):
                    error += 1
                # dfResult = np.inserdfdfResult, i, cC, axis=1)
                cc = np.zeros(60)
            ber[cnr, i] = error
            error = 0
    return ber, noise_signal