""" step1: filter_ascii
    step2: change_format
    step3: final_wash
"""
from typing import BinaryIO
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import block as bk

# matplotlib.use('TkAgg')
# from mpl_toolkits.mplot3d import Axes3D
# from sklearn.decomposition import PCA

"""初始化一些变量"""
data = bytes()  # 用于存放循环输入测试数据
data_scale = [8, 8]  # 需要数据清洗的规模
current_completion_flag = False  # 标志一次循环是否做完
file_type = ".DAT"  # 批处理的文件后缀名
size_of_each_grid = 0.4  # 每个方格的边长
count = -1  # 用于auto_input循环

path = "./data_of_web/"  # 提供绝对路径的字符串
# path = "./recalibration_anchor/"  # 提供绝对路径的字符串
# path = "./only_reopen_anchor/"  # 提供绝对路径的字符串
# path = "./long_time/"  # 提供绝对路径的字符串

x_draw = []
y_draw = []


def get_SN(data_scale=[8, 8]):
    """获取每个文件编号"""
    sn = []
    for i in range(data_scale[0]):
        for j in range(data_scale[1]):
            sn.append(str(i) + str(j))  # 提供遍历文件的编号
    return sn


def auto_input(sn):
    # count = -1  # 用于文件处理遍历计数
    # global path, file_type, current_completion_flag
    #
    # def inner():  # inner()起局部静态变量的作用
    #     nonlocal count  # 声明 count 变量来自外部函数
    #     count += 1
    #     return count
    # def counter():
    #     # 在闭包内部定义一个函数属性
    #     if not hasattr(counter, "count"):
    #         counter.count = -1
    #
    #     counter.count += 1
    #     return counter.count
    # class counter:
    #     count = -1
    #
    #     @property
    #     def cc(self):
    #        self.count = self.count + 1
    #
    # counter.cc
    # ct = counter.count
    global count
    count = count + 1

    global current_completion_flag
    if current_completion_flag is False:
        path_handle = path + sn[count] + file_type
        current_completion_flag = True
    # with open(path, 'rb') as f:  # 自动close
    f: BinaryIO = open(path_handle, 'rb')
    return f, sn[count]  # TODO 不关闭文件还能第二次遍历吗


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


def draw(group):
    # 生成两组随机坐标和一个随机点
    band = []
    for temp in group:
        x = temp._separate_data__x
        y = temp._separate_data__y
        points = [[x[i], y[i]] for i in range(len(x))]
        array = np.array(points)
        band.append(array)

    # 绘制坐标点
    plt.scatter(band[0][90:110, 0], band[0][90:110, 1], color='blue', label='Group 1')
    plt.scatter(band[1][90:110, 0], band[1][90:110, 1], color='red', label='Group 2')
    plt.scatter(band[2][90:110, 0], band[2][90:110, 1], color='#58ff70', label='Group 3')
    plt.scatter(band[3][90:110, 0], band[3][90:110, 1], color='#ff7f60', label='Group 4')
    plt.scatter(band[4][90:110, 0], band[4][90:110, 1], color='m', label='Group 5')

    # 绘制基站点
    plt.scatter(1.2, 1, color='k', label='real_point')
    if True:
        center0 = np.mean(band[0][90:110], axis=0)
        plt.scatter(center0[0], center0[1], color='blue', marker='x', label='Center 0')

        center1 = np.mean(band[1][90:110], axis=0)
        plt.scatter(center1[0], center1[1], color='red', marker='x', label='Center 1')

        center2 = np.mean(band[2][90:110], axis=0)
        plt.scatter(center2[0], center2[1], color='#58ff70', marker='x', label='Center 2')

        center3 = np.mean(band[3][90:110], axis=0)
        plt.scatter(center3[0], center3[1], color='#ff7f60', marker='x', label='Center 3')

        center4 = np.mean(band[4][90:110], axis=0)
        plt.scatter(center4[0], center4[1], color='m', marker='x', label='Center 4')

    if True:
        # 计算并绘制第一组外切圆
        radius0 = max(np.linalg.norm(point - center0) for point in band[0][90:110])
        circle0 = Circle(center0, radius0, fill=False, color='blue', linestyle='--',
                         label=f'Bounding Circle (radius={radius0:.2f})')
        plt.gca().add_patch(circle0)
        plt.text(center0[0] + radius0, center0[1], f'radius={radius0:.2f}', verticalalignment='center',
                 color='blue')  # 添加第一组外切圆半径标注

        radius1 = max(np.linalg.norm(point - center1) for point in band[1][90:110])
        circle1 = Circle(center1, radius1, fill=False, color='blue', linestyle='--',
                         label=f'Bounding Circle (radius={radius1:.2f})')
        plt.gca().add_patch(circle1)
        plt.text(center1[0] + radius1, center1[1], f'radius={radius1:.2f}', verticalalignment='center',
                 color='blue')  # 添加第一组外切圆半径标注

        radius2 = max(np.linalg.norm(point - center2) for point in band[2][90:110])
        circle2 = Circle(center2, radius2, fill=False, color='blue', linestyle='--',
                         label=f'Bounding Circle (radius={radius2:.2f})')
        plt.gca().add_patch(circle2)
        plt.text(center2[0] + radius2, center2[1], f'radius={radius2:.2f}', verticalalignment='center',
                 color='blue')  # 添加第一组外切圆半径标注

        radius3 = max(np.linalg.norm(point - center3) for point in band[3][90:110])
        circle3 = Circle(center3, radius3, fill=False, color='blue', linestyle='--',
                         label=f'Bounding Circle (radius={radius3:.2f})')
        plt.gca().add_patch(circle3)
        plt.text(center3[0] + radius3, center3[1], f'radius={radius3:.2f}', verticalalignment='center',
                 color='blue')  # 添加第一组外切圆半径标注

        radius4 = max(np.linalg.norm(point - center4) for point in band[4][90:110])
        circle4 = Circle(center4, radius4, fill=False, color='blue', linestyle='--',
                         label=f'Bounding Circle (radius={radius4:.2f})')
        plt.gca().add_patch(circle4)
        plt.text(center4[0] + radius4, center4[1], f'radius={radius4:.2f}', verticalalignment='center',
                 color='blue')  # 添加第一组外切圆半径标注

    # 绘制连线并标注距离

    # 添加图例
    # plt.legend()
    plt.legend(bbox_to_anchor=(-0.5, 1), loc='upper left')

    # 设置图形属性
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Centers and Bounding Circles')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    # 显示图形
    plt.show()


def mean_drop():
    return


class separate_data:
    base_start_num = 0
    __check_num = []
    __check_num2 = []
    __x2 = []
    __y2 = []
    __z2 = []
    __x = []
    __y = []
    __z = []

    def __init__(self, sn):
        self.base_start_num = 0
        self.__check_num = []
        self.__check_num2 = []
        self.__x2 = []
        self.__y2 = []
        self.__z2 = []
        self.__x = []
        self.__y = []
        self.__z = []
        self.__sn = sn

    def make_dimen_right(self):
        if len(self.__x) != len(self.__y) and len(self.__x) != len(self.__z) and len(self.__z) != len(self.__y):
            num = min(len(self.__x), len(self.__y), len(self.__z))
            for i in range(num):
                self.__x2.append(self.__x[i])
                self.__y2.append(self.__y[i])
                self.__z2.append(self.__z[i])
            self.__x = self.__x2
            self.__y = self.__y2
            self.__z = self.__z2

    def load_data(self, lists):
        # strlen = len(lists[0])
        got_m_x_y_z_complete = []
        lenth_total = len(lists)
        for i in range(lenth_total):  # 遍历每一大条
            if len(lists[i]) > 40:  # 串长不足40 说明存在清洗丢失 就不分解此串了
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
                        self.__check_num2.append(result)
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
                        self.__x2.append(result)
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
                        self.__y2.append(result)
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
                        self.__z2.append(result)
                        buff = []
                        i = 2
                if len(buff_mxyz) == 4:
                    self.__check_num.append(buff_mxyz[0])
                    self.__x.append(buff_mxyz[1])
                    self.__y.append(buff_mxyz[2])
                    self.__z.append(buff_mxyz[3])
                else:
                    break
                    #     self.__check_num
        # self.make_dimen_right()
        return


def loop(sn):
    """循环处理每个样本"""
    f, sn = auto_input(sn)
    global current_completion_flag
    data = f.read()

    filtered_bytes = filter_ascii(data)  # 去空格加截断标识符
    bottle = change_format(filtered_bytes)  # 限制位长分隔为bytearray list
    sec_bottle = final_wash(bottle)  # 倒序清洗、加结束符、格式化为字符串

    item = separate_data(sn)
    item.load_data(sec_bottle)  # 截断分离check_num xyz
    # one = point_grid(item, sn='00')
    # diif_x, diff_y, diff_distance = one.abs_diff()
    #
    # global x_draw
    # global y_draw
    # x_draw.append(one._mean_x)
    # y_draw.append(one._mean_y)
    current_completion_flag = False
    return item


if __name__ == '__main__':
    def main():
        group = []  # 用于接收每组清洗好的类
        # with open("./data_of_web/00.DAT", 'rb') as f:     # 单文件处理

        # for i in range(5):                                # 非网格文件清洗
        #     group.append(loop(['00', '01', '02', '03', '04']))
        # draw(group)

        for i in range(data_scale[0]*data_scale[1]):        # 网格点文件遍历清洗
            group.append(loop(get_SN()))
        # draw(group)

    main()
