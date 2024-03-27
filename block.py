import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import queue

block_table_queue = []  # 方块池
table_queue = []
def get_scale(input_df):
    linmax = input_df.shape[0]
    colmax = input_df.shape[1]
    return [linmax, colmax]

# def interpolation(x):
#     ampli_x = []
#     for index in range((len(x)-1)):
#         temp = np.linspace(x[index], x[index+1], 10)    # TODO 解决取值重复的问题
#         for index in temp:
#             ampli_x.append(index)
#
#     return ampli_x

class table:
    table_num = 0
    __table_value = []

    def __init__(self, ls):
        self.__table_value = ls
        return

    def load_it(self, p, q, lst):   # p是队列位置，q是遍历的第二个参数，lst是传入的操作table
        if self.table_num == p:
            self.__table_value.append(lst[p][q])

    def pull_out(self):
        return self.__table_value

# class table_queue:
# Queue = table_queue()
for i in range(60):     # 自动长度
    ls = []
    item = table(ls)
    item.table_num = i
    table_queue.append(item)

# 画出block区域、坐标系、基点位置、颜色映射
def draw_block(scale):  # TODO 密化网格 线性插值
    l = scale[0]
    w = scale[1]

    table_o = []
    table_row = []
    table_value = []
    table_col = []
    table_value_col = []
    # take_it = []
    for i in range(l-1):  # 扩增扫描行,方块比点位少1
        line = []
        value = []
        line_segment = []
        value_segment = []
        for temp in block_table_queue:
            if temp.block_ID[0] == i:
                line.append(temp.block_ID[1])
                value.append(temp.weigh)
        for t in range(len(line)-1):
            lable_seg = np.linspace(line[t], line[t + 1], 10, endpoint = False)  # 生成连续数据
            value_seg = np.linspace(value[t], value[t + 1], 10, endpoint = False)  # 生成连续数据
            for p in lable_seg:
                line_segment.append(p)
            for v in value_seg:
                value_segment.append(v)
        # for to_line in line_segment:
        table_row.append(line_segment)
        # for to_value in value_segment:
        table_value.append(value_segment)
        pass


    # table = list((l-1, len(table_value[0])))
    for i in range(l-2):    # TODO 考虑最后一排的问题
        col_segment = []
        # table = np.zeros((10*w), (10*l))
        # table = np.zeros((50, 60))
        value_seg_col = []
        for j in range(len(table_value[0])):
            star_value = table_value[i][j]
            stop_value = table_value[i+1][j]
            value_seg_col.append(np.linspace(star_value, stop_value, 10, endpoint=False))
        # take_it.append(value_seg_col)
        pass
        for n in range(len(value_seg_col)):     # 60
            for m in range(len(value_seg_col[0])):      # 10
                # pass
                # Queue.table[n].table_value.append(value_seg_col[n][m])
                for r in table_queue:
                    r.load_it(n, m, value_seg_col)   # p是队列位置，q是遍历的第二个参数，lst是传入的操作table
                    # if r.table_num == n:
                    #     r.table_value.append(value_seg_col[n][m])
                # A = table_queue[n]
                # if A.table_num == n:
                #     A.table_value.append(value_seg_col[n][m])
        pass
    pass

            # col_seg = np.linspace(star_row, stop_row, 10, endpoint=False)
            # star_row = table_row[i][j]
            # stop_row = table_row[i+1][j]

    x = np.linspace(0, 60, 60)  # 生成连续数据
    y = np.linspace(0, 40, 40)  # 生成连续数据
    # Z = np.zeros((40, 60))    # len(table_queue)
    Z = np.zeros((60, 40))
    for temp in table_queue:
        for i in range(len(temp.pull_out())):
            line_num = temp.table_num
            obj = temp.pull_out()
            Z[line_num][i] = obj[i]
            pass
        pass
    pass



    Y, X = np.meshgrid(y, x)        # 将原始数据变成网格数据形式
    # for i in range(l):      # TODO 这里没考虑z与xy对应关系
    #     for j in range(w):
    #         p = i + j
    #         item = block_table_queue[p]
    #         Z[j][i] = item.weigh
    # table_z_ = np.zeros((j*10, i*10), dtype=int)
    # for i in Z.shape[0]:
    #     for j in (Z.shape[1]-1):
    #         temp = np.linspace(Z[i][j], Z[i][j+1], 10)
    #         line_ampli.append(temp)
    #     line_ampli = 0
    #
    #         pass


# --------------------------------------------------------------- # 等高线图
    #设置打开画布大小,长10，宽6
    plt.figure(figsize=(10, 6))
    #填充颜色，f即filled
    plt.contourf(X, Y, Z)
    plt.contour(X, Y, Z)    # 画等高线
# --------------------------------------------------------------- # 二维网图
#     C = plt.contour(X, Y, Z, [2, 5, 8, 10])
#     plt.clabel(C, inline=True, fontsize=10)
#     fig = plt.figure()
#     fig = plt.figure(figsize=(10, 10))
#     ax1 = plt.axes(projection='3d')
#     ax1.scatter3D(X, Y, Z, cmap='Blues')
    # 设置坐标轴范围
    # plt.xlim((0, 360))
    # plt.ylim((0, 240))
    # 设置坐标轴名称
    plt.xlabel('x Axis')
    plt.ylabel('y Axis')
    # plt.zlabel('rate of expansion')
    # 设置坐标轴刻度
    # my_x_ticks = np.arange(0, 360, 60)
    # my_y_ticks = np.arange(0, 240, 60)
    # plt.xticks(my_x_ticks)
    # plt.yticks(my_y_ticks)
    # surf = ax1.plot_wireframe(X, Y, Z)
    plt.grid(True)
    plt.show()
    return

class block:
    adv_ratio = 0
    block_ID = []
    weigh = 0
    _le_up = [] # 定义block的四个顶点
    _ri_down = []
    _ri_up = []
    _le_down = []


    def __init__(self, adv_ratio, i, j):
        self.block_ID = [i, j]
        self.adv_ratio = adv_ratio
        return

    def get_four_p(self, input_df):
        le_up = input_df.at[self.block_ID[0], self.block_ID[1]]
        ri_down = input_df.at[self.block_ID[0] + 1, self.block_ID[1] + 1]
        ri_up = input_df.at[self.block_ID[0], self.block_ID[1] + 1]
        le_down = input_df.at[self.block_ID[0] + 1, self.block_ID[1]]
        self._le_up = str.split(le_up)
        self._ri_down = str.split(ri_down)
        self._ri_up = str.split(ri_up)
        self._le_down = str.split(le_down)
        return  # _le_up, _ri_down, _ri_up, _le_down

    def norm(self):  # 求对角线二范数和伸缩尺度的权重
        line_1 = abs(float(self._ri_up[1]) - float(self._le_up[1]))
        line_3 = abs(float(self._ri_down[1]) - float(self._le_down[1]))
        line_2 = abs(float(self._ri_down[0]) - float(self._ri_up[0]))
        line_4 = abs(float(self._le_down[0]) - float(self._le_up[0]))
        self.weigh = math.sqrt(np.square(max(line_1, line_2, line_3, line_4)) + np.square(min(line_1, line_2, line_3, line_4)))
        self.weigh /= math.sqrt(2)
        self.weigh /= self.adv_ratio      # 体现相对误差 # TODO 没考虑坐标配准和旋转
        return

    def interpolation(self):
        pass
        return


if __name__ == '__main__':
    def main():

        scale = []  # table的规模
        ls = []

        input_df = pd.read_csv(r"E:\Project_Python\UWB_Spatial_linearity\cell_data.csv", index_col=0)
        input_df.index = range(input_df.shape[0])
        input_df.columns = range(input_df.shape[1])
        scale = get_scale(input_df)  # 获取源表规模
        # 创建block数据结构
        for i in range(scale[0] - 1):
            for j in range(scale[1] - 1):
                itme = block(60, i, j)  # 关键字参数设置方块边长 adv_ratio = 60
                block_table_queue.append(itme)
        # 求每个block涨缩尺度
        for temp in block_table_queue:
            temp.get_four_p(input_df)
            temp.norm()
        # 画每个block
        draw_block(scale)


        pass

    main()