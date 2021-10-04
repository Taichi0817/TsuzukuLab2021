import pprint

import numpy as np


class CreateIdealJJY(object):
    """理想的なJJYの0~59分の分の情報を生成するクラス

    理想的なJJYの0~59分の分の情報を生成するクラス
    ただし、マーカーは排除した。
    Attributes:
        ideal_signal[:, 0]: 40分を示す
        ideal_signal[:, 1]: 20分を示す
        ideal_signal[:, 2]: 10分を示す
        ideal_signal[:, 3]: 8分を示す
        ideal_signal[:, 4]: 4分を示す
        ideal_signal[:, 5]: 2分を示す
        ideal_signal[:, 6]: 1分を示す
        ideal_signal[:, 7]:パリティ

    """
    def __init__(self):
        self.ideal_signal = np.zeros((60, 8))
        self.tmp2 = [0] * 60
        self.tmp3 = np.zeros((60, 8))

    def create_signal(self):
        for i in range(60):
            tmp1 = i
            if tmp1 >= 50:
                self.ideal_signal[i, 0] = 1
                self.ideal_signal[i, 2] = 1
                tmp1 -= 50
            elif tmp1 >= 40:
                self.ideal_signal[i, 0] = 1
                tmp1 -= 40
            elif tmp1 >= 30:
                self.ideal_signal[i, 1] = 1
                self.ideal_signal[i, 2] = 1
                tmp1 -= 30
            elif tmp1 >= 20:
                self.ideal_signal[i, 1] = 1
                tmp1 -= 20
            elif tmp1 >= 10:
                self.ideal_signal[i, 2] = 1
                tmp1 -= 10
            self.tmp2[i] = bin(tmp1)[2:]
            if len(self.tmp2[i]) == 1:
                self.ideal_signal[i, 3] = 0
                self.ideal_signal[i, 4] = 0
                self.ideal_signal[i, 5] = 0
                self.ideal_signal[i, 6] = self.tmp2[i]
            elif len(self.tmp2[i]) == 2:
                self.ideal_signal[i, 3] = 0
                self.ideal_signal[i, 4] = 0
                self.ideal_signal[i, 5] = self.tmp2[i][0]
                self.ideal_signal[i, 6] = self.tmp2[i][1]
            elif len(self.tmp2[i]) == 3:
                self.ideal_signal[i, 3] = 0
                self.ideal_signal[i, 4] = self.tmp2[i][0]
                self.ideal_signal[i, 5] = self.tmp2[i][1]
                self.ideal_signal[i, 6] = self.tmp2[i][2]
            elif len(self.tmp2[i]) == 4:
                self.ideal_signal[i, 3] = self.tmp2[i][0]
                self.ideal_signal[i, 4] = self.tmp2[i][1]
                self.ideal_signal[i, 5] = self.tmp2[i][2]
                self.ideal_signal[i, 6] = self.tmp2[i][3]
            if np.count_nonzero(self.ideal_signal[i] == 1) % 2 == 1:
                self.ideal_signal[i, 7] = 1
        self.ideal_signal = np.where(self.ideal_signal == 0, -1, self.ideal_signal)
        self.ideal_signal = dict(enumerate(self.ideal_signal))
        # pprint.pprint(self.ideal_signal)
        return self.ideal_signal