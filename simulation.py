import requests

import math

import matplotlib.pyplot as plt
import numpy as np

import assets.create_ideal_jjy
from assets import create_ideal_jjy
from assets import line_notify




create = create_ideal_jjy.CreateIdealJJY()
create.create_signal()
print(create.ideal_signal)






if __name__ == '__main__':
    line_notify()
