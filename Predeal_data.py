""" step1: filter_ascii
    step2: change_format
    step3: final_wash
"""
from typing import BinaryIO
import matplotlib
import math

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import numpy as np

data = bytes()  # 用于存放循环输入测试数据
data_scale = [8, 8]  # 需要数据清洗的规模
current_completion_flag = False  # 标志一次循环是否做完
path = "./data_of_web/"  # 提供绝对路径的字符串
file_type = ".DAT"  # 批处理的文件后缀名
size_of_each_grid = 0.4  # 每个方格的边长


def filter_ascii(data):
    """去空格加截断标识符"""
    ascii_part = bytearray()
    for num in range(len(data)):
        # for byte in data:
        if (data[num] < 123 and data[num] > 47 or data[num] == 45 or data[num] == 46):  # 在字母数字范围内 并且包含小数点和负号
            if (data[num] == 99 and data[num + 1] == 104):  # 发现以ch开头
                ascii_part.append(38)  # 加 & 标识符
                ascii_part.append(data[num])
            else:
                ascii_part.append(data[num])
    return ascii_part


def change_format(filtered_bytes):
    """限制位长格式化为list"""
    over = []
    lenz = len(filtered_bytes)
    for num in range(lenz - 80):  # 45 是预留安全尾距 舍弃掉最后一个数据 by the way 怎样去掉num的重复遍历
        temp = bytearray()
        i = 1
        if (filtered_bytes[num] == 38):  # 遇到&
            while filtered_bytes[num + i] != 38 and i < 46:  # 限制一个搜索单次log的上限 设置长了有的时候末尾会有u,处理不干净
                temp.append(filtered_bytes[num + i])
                i += 1
                if filtered_bytes[num + i] == 38:
                    break
            over.append(temp)
            # num += (i - 1)
    return over


def final_wash(bottle):
    """最后一次清洗"""
    bottle2 = bytearray()
    lis = []
    # number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in bottle:
        for j in range(len(i) - 1, 40, -1):
            if i[j] != 48 and i[j] != 49 and i[j] != 50 and i[j] != 51 and i[j] != 52 and i[j] != 53 and i[j] != 54 and \
                    i[j] != 55 and i[j] != 56 and i[j] != 57:
                i = i[:-1]
            else:
                i.append(37)
                break
        bottle2.extend(i)
        lis.append(bottle2)
        bottle2 = bytearray()
    strgroup = []
    for temp in lis:  # 取每条出来
        byte_str = str(temp, 'utf-8')
        strgroup.append(byte_str)

    return strgroup


def get_SN(data_scale=[8, 8]):
    """获取每个文件编号"""
    sn = []
    for i in range(data_scale[0]):
        for j in range(data_scale[1]):
            sn.append(str(i) + str(j))  # 提供遍历文件的编号
    return sn


def auto_input(sn):
    count = -1  # 用于文件处理遍历计数
    global path, file_type, current_completion_flag

    def inner():  # inner()起局部静态变量的作用
        nonlocal count  # 声明 count 变量来自外部函数
        count += 1
        return count

    inner()
    if current_completion_flag is False:
        path = path + sn[count] + file_type
        current_completion_flag = True
    # with open(path, 'rb') as f:  # 自动close
    f: BinaryIO = open(path, 'rb')
    return f, sn[count]     # TODO 不关闭文件还能第二次遍历吗


def draw(item):
    x = item.x
    y = item.y
    # --------------------------------------------------------------- # 二维网图
    # 绘制 x-y 点图
    # plt.figure(figsize=(8, 6))  # 设置图形的大小
    plt.plot(x, y, 'o', color='blue', label='Points')
    plt.xlabel('x Axis')
    plt.ylabel('y Axis')

    # 设置坐标轴刻度
    # plt.xticks(my_x_ticks)
    # plt.yticks(my_y_ticks)
    # surf = ax1.plot_wireframe(X, Y, Z)

    plt.show()
    global current_completion_flag
    current_completion_flag = False

    return


def loop():
    """循环处理每个样本"""
    f, sn = auto_input(get_SN())
    global current_completion_flag
    data = f.read()
    filtered_bytes = filter_ascii(data)  # 去空格加截断标识符
    bottle = change_format(filtered_bytes)  # 限制位长分隔为bytearray list
    sec_bottle = final_wash(bottle)  # 倒序清洗、加结束符、格式化为字符串

    item = separate_data()
    item.load_data(sec_bottle)
    one = point_grid(item, sn='00')
    diif_x, diff_y, diff_distance = one.abs_diff()
    draw(item)
    current_completion_flag = False
    pass
    return


class separate_data:
    base_start_num = 0
    check_num = []
    check_num2 = []
    x2 = []
    y2 = []
    z2 = []
    x = []
    y = []
    z = []

    def make_dimen_right(self):
        if len(self.x) != len(self.y) and len(self.x) != len(self.z) and len(self.z) != len(self.y):
            num = min(len(self.x), len(self.y), len(self.z))
            for i in range(num):
                self.x2.append(self.x[i])
                self.y2.append(self.y[i])
                self.z2.append(self.z[i])
            self.x = self.x2
            self.y = self.y2
            self.z = self.z2

    def load_data(self, lists):
        # strlen = len(lists[0])
        got_m_x_y_z_complete = []
        lenth_total = len(lists)
        for i in range(lenth_total):  # 遍历每一大条
         if len(lists[i]) > 40:       # 串长不足40 说明存在清洗丢失 就不分解此串了
            buff_mxyz = []
            dealstr = lists[i]
            # if len(lists[i]) < 30:
            #     pass
            for j in range(len(lists[i]) - 3):  # 遍历每一条中的每一个字符 # 这里减去一个常数是为了保证裕量不会超出 dealstr本身
                if dealstr[j] == 'm':
                    buff = []
                    i = 1
                    while i < 10:  # TODO 清洗的时候要注意推演的位数 这里用字符匹配机制比较保险
                        if dealstr[j + i] == "x":
                            break
                        else:
                            buff.append(int(dealstr[j + i]))
                            i = i + 1
                    num_str = ''.join(str(num) for num in buff)
                    result = int(num_str)
                    buff_mxyz.append(result)
                    self.check_num2.append(result)
                    buff = []
                    i = 1
                elif dealstr[j] == 'x':
                    small_point = 0  # 小数点在第几位
                    flag_point = False  # 是否小数
                    flag = False  # 负数标志
                    buff = []
                    i = 2
                    while i < 10:  # 字符匹配机制判断第三位是否为负
                        if dealstr[j + i] == "-":
                            flag = True
                            i = i + 1
                            continue
                        if dealstr[j + i] == ".":
                            flag_point = True
                            small_point = i
                            i = i + 1
                        elif dealstr[j + i] == "y":
                            break
                        else:
                            buff.append(int(dealstr[j + i]))
                            i = i + 1
                    org_len = len(buff)
                    num_str = ''.join(str(num) for num in buff)
                    result = int(num_str)
                    if flag_point == True:
                        # if flag == True:
                        #     mi = org_len - 1
                        # else:
                        #     mi = org_len
                        mi = org_len - 1
                        result = result * (10 ** (-mi))
                    if flag == True:
                        result = result * (-1)
                    flag = False
                    flag_point = False
                    buff_mxyz.append(result)
                    self.x2.append(result)
                    buff = []
                    i = 2
                elif dealstr[j] == 'y':
                    small_point = 0  # 小数点在第几位
                    flag_point = False  # 是否小数
                    flag = False  # 负数标志
                    buff = []
                    i = 2
                    while i < 10:  # 字符匹配机制判断第三位是否为负
                        if dealstr[j + i] == "-":
                            flag = True
                            i = i + 1
                            continue
                        if dealstr[j + i] == ".":
                            flag_point = True
                            small_point = i
                            i = i + 1
                            continue
                        elif dealstr[j + i] == "z":
                            break
                        else:
                            buff.append(int(dealstr[j + i]))
                            i = i + 1
                    org_len = len(buff)
                    num_str = ''.join(str(num) for num in buff)
                    result = int(num_str)
                    if flag_point == True:
                        # if flag == True:
                        #     mi = org_len - 1
                        # else:
                        #     mi = org_len
                        mi = org_len - 1
                        result = result * (10 ** (-mi))
                    if flag == True:
                        result = result * (-1)
                    flag = False
                    flag_point = False
                    buff_mxyz.append(result)
                    self.y2.append(result)
                    buff = []
                    i = 2
                elif dealstr[j] == 'z':
                    small_point = 0  # 小数点在第几位
                    flag_point = False  # 是否小数
                    flag = False  # 负数标志
                    buff = []
                    i = 2
                    while i < 10:  # 字符匹配机制判断第三位是否为负
                        if dealstr[j + i] == "-":
                            flag = True
                            i = i + 1
                            continue
                        if dealstr[j + i] == ".":
                            flag_point = True
                            small_point = i
                            i = i + 1
                            continue
                        elif dealstr[j + i] == "%":
                            break
                        elif dealstr[j + i] != "%" and dealstr[j + i] != "." and dealstr[j + i] != "-" and dealstr[
                            j + i] != "0" \
                                and dealstr[j + i] != "1" and dealstr[j + i] != "2" and dealstr[j + i] != "3" and \
                                dealstr[j + i] != "4" \
                                and dealstr[j + i] != "5" and dealstr[j + i] != "6" and dealstr[j + i] != "7" and \
                                dealstr[j + i] != "8" \
                                and dealstr[j + i] != "9" and dealstr[j + i] != "_":
                            pass
                        else:
                            buff.append(int(dealstr[j + i]))
                            i = i + 1
                    org_len = len(buff)
                    num_str = ''.join(str(num) for num in buff)
                    result = int(num_str)
                    if flag_point == True:
                        # if flag == True:
                        #     mi = org_len - 1
                        # else:
                        #     mi = org_len - 1
                        mi = org_len - 1
                        result = result * (10 ** (-mi))
                    if flag == True:
                        result = result * (-1)
                    flag = False
                    flag_point = False
                    buff_mxyz.append(result)
                    self.z2.append(result)
                    buff = []
                    i = 2
            if len(buff_mxyz) == 4:
                self.check_num.append(buff_mxyz[0])
                self.x.append(buff_mxyz[1])
                self.y.append(buff_mxyz[2])
                self.z.append(buff_mxyz[3])
            else:
                break
                #     self.check_num
        # self.make_dimen_right()
        return


class point_grid:
    global size_of_each_grid
    size_of_each_grid
    _x = []
    _y = []
    _z = []
    _check_num = []
    _total = 0
    _mean_x = 0
    _mean_y = 0
    _mean_z = 0
    _calcu_sample = 3


    posi_ID = []
    posi_real = []
    posi_calcu_real = []

    def __init__(self, group, sn):
        self._x = group.x
        self._y = group.y
        self._z = group.z
        self._check_num = group.check_num
        self._total = len(self._check_num)
        self.mean_each()
        self.posi_ID.append(int(sn[0]))
        self.posi_ID.append(int(sn[1]))
        self.posi_real.append(self.posi_ID[0] * size_of_each_grid)
        self.posi_real.append(self.posi_ID[1] * size_of_each_grid)


    def mean(self, lst):
        sum = 0
        for i in range(self._calcu_sample):
            sum = sum + lst[i+20]
        return sum / self._calcu_sample

        # total = sum(lst)
        # length = len(lst)
        # if length == 0:
        #     return 0  # 避免除以零的情况
        # return total / length

    def mean_each(self):
        self._mean_x = self.mean(self._x)
        self._mean_y = self.mean(self._y)
        self._mean_z = self.mean(self._z)

    def calcu_posi_mean(self):

        return

    def calcu_posi_real(self):

        return

    def abs_diff(self):
        diif_x = self._mean_x - self.posi_real[0]
        diff_y = self._mean_y - self.posi_real[1]
        diff_distance = math.sqrt(diif_x ** 2 + diff_y ** 2)
        return diif_x, diff_y, diff_distance

    def error_range(self):

        return

    def long_time_diff(self):

        return

    def api_contour(self):
        """误差随位置变化的等高线图"""

        return  # posit_ID abs_diff



if __name__ == '__main__':
    def main():
        # with open("./data_of_web/00.DAT", 'rb') as f:  # 单文件处理
        for i in range(data_scale[0]*data_scale[1]):
            loop()

            # TODO 输出文件for 遍历到不同的文件中(


    # for i in range(data_scale[0]*data_scale[1]):

    main()
