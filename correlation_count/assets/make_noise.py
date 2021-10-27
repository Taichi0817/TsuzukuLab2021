import math


import numpy as np



def out_standard_deviation(cnr):
    """
    CNRを入力すると、標準偏差を出力するプログラム
    cnr:int
    """
    return math.sqrt(1/pow(10, cnr/10))


def make_noise(std_div, ideal_signal):
    """
    正規分布に基づいたノイズを作り出すプログラム
    std_div:float 標準偏差
    """
    e = np.zeros((60, 8))
    noise_signal = np.zeros((60, 8))
    for i in range(60):
        e[i] = np.random.normal(loc=0, scale=std_div, size=8)
        noise_signal[i] = ideal_signal[i] + e[i]
    return noise_signal




