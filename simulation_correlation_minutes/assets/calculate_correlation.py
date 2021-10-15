import numpy as np


def calculate_correlation(noise_signal, ideal_signal, number_of_simulations, cnr):
    cc = np.zeros(60)
    error = 0
    ber = np.zeros((15, number_of_simulations // 60))
    for i in range(60):
        for j in range(60):
            for k in range(8):
                temp = noise_signal[i][k] * ideal_signal[j][k]
                cc[j] += temp
        if cc[k] != np.amax(cc):
            error += 1
        cc = np.zeros(60)
    ber[cnr, i] = error
    error = 0
    return ber