import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import numpy as np

data = bytes()  # 用于循环输入测试数据
data_scale = [8, 8]  # 需要数据清洗的规模
Flag_deal_finished = False  # 标志一次循环是否做完

def filter_ascii(data):  # 去空格加截断标识符
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


def change_format(filtered_bytes):  # 限制位长格式化为list
    over = []
    lenz = len(filtered_bytes)
    for num in range(lenz - 80):  # 45 是预留安全尾距 舍弃掉最后一个数据 by the way 怎样去掉num的重复遍历
        temp = bytearray()
        i = 1
        if (filtered_bytes[num] == 38):  # 遇到&
            while filtered_bytes[num + i] != 38 and i < 45:  # 限制一个搜索单次log的上限 设置长了有的时候末尾会有u,处理不干净
                temp.append(filtered_bytes[num + i])
                i += 1
                if filtered_bytes[num + i] == 38:
                    break
            over.append(temp)
            # num += (i - 1)
    return over


def final_wash(bottle):
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

    return lis


def auto_input(num=0):
    # with open("./data_of_web/20.DAT", 'rb') as f:
    return


class separate_data:
    base_satrt_num = 0
    check_num = []
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
        lenth_total = len(lists)
        for i in range(lenth_total):  # 遍历每一条
            dealstr = lists[i]
            if len(lists[i]) < 30:
                pass
            for j in range(len(lists[i]) - 10):  # 遍历每一条中的字符 # 这里减去一个常数是为了保证裕量不会超出 dealster本身
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
                    self.check_num.append(result)
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
                        if flag == True:
                            mi = org_len - 1
                        else:
                            mi = mi = org_len
                        result = result * (10 ** (-mi))
                    if flag == True:
                        result = result * (-1)
                    flag = False
                    flag_point = False
                    self.x.append(result)
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
                        if flag == True:
                            mi = org_len - 1
                        else:
                            mi = mi = org_len
                        result = result * (10 ** (-mi))
                    if flag == True:
                        result = result * (-1)
                    flag = False
                    flag_point = False
                    self.y.append(result)
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
                        if flag == True:
                            mi = org_len - 1
                        else:
                            mi = mi = org_len
                        result = result * (10 ** (-mi))
                    if flag == True:
                        result = result * (-1)
                    flag = False
                    flag_point = False
                    self.z.append(result)
                    buff = []
                    i = 2
                pass
                #     self.check_num
        self.make_dimen_right()
        return


if __name__ == '__main__':
    def main():
        # num  TODO 放文件
        # 字符串链接
        # to str
        # for 遍历文件
        with open("./data_of_web/20.DAT", 'rb') as f:
            data = f.read()
            filtered_bytes = filter_ascii(data)  # 去空格加截断标识符
            bottle = change_format(filtered_bytes)  # 限制位长格式化为list
            answer = final_wash(bottle)
            strgroup = []
            for temp in answer:
                byte_str = str(temp, 'utf-8')
                strgroup.append(byte_str)
            item = separate_data()
            item.load_data(strgroup)
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
            pass
            # TODO 输出文件for 遍历到不同的文件中


    main()
