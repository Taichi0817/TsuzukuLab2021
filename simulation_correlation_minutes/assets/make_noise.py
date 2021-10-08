import math


import numpy as np

def make_noise(std_div, ideal_signal, n):
    """
    正規分布に基づいたノイズを作り出すプログラム
    std_div:float 標準偏差
    """
    e = np.zeros((n, 8))
    noise_signal = np.zeros((n, 8))
    for i in range(n):
        e[i] = np.random.normal(loc=0, scale=std_div, size=8)
        noise_signal[i] = ideal_signal[i] + e[i]
    return noise_signal

def out_standard_deviation(cnr):
    """
    CNRを入力すると、標準偏差を出力するプログラム
    cnr:int
    """
    return math.sqrt(1/pow(10, cnr/10))