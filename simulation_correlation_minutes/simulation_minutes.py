import requests
import time
import datetime

import math
import matplotlib.pyplot as plt
import numpy as np
import pprint

from assets import create_ideal_jjy
from assets import make_noise

n = 120
create = create_ideal_jjy.CreateIdealJJY(n)
ideal_signal = create.create_signal()
pprint.pprint(ideal_signal)
number_of_simulations = int(600)
cc = np.zeros(60)
error = 0
ber = np.zeros((15, int(number_of_simulations/60)))
for i in range(int(number_of_simulations/60)):
    for cnr in range(15):
        std_dev = make_noise.out_standard_deviation(cnr)
        noise_signal = make_noise.make_noise(std_dev, ideal_signal, n)