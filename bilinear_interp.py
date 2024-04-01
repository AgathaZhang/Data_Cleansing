import Predeal_data as wash
import pickle
import math
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D

def find_closest_grid_points(grid_points, x, y):
    """
    找到给定坐标所在的四个网格点。

    参数:
    x (float): x 坐标。
    y (float): y 坐标。
    grid_points (list of tuple): 多边形网格点的坐标列表。

    返回值:
    list: 包含四个网格点坐标的列表。
    """
    closest_points = []

    # 遍历网格点，找到距离给定坐标最近的四个网格点
    for point in grid_points:
        if len(closest_points) < 4:
            closest_points.append(point)
        else:
            distances = [((x - px) ** 2 + (y - py) ** 2) for px, py in closest_points]      # 遍历该点到四个点中每个点的距离 存在distance里
            max_distance_index = distances.index(max(distances))                            # 找出距离最大点的索引
            distance_to_point = (x - point[0]) ** 2 + (y - point[1]) ** 2                   # 找出第五个点的距离
            if distance_to_point < distances[max_distance_index]:                           # 从第五个点开始，该点如果小于距离最大点
                closest_points[max_distance_index] = point                                  # 该点替换为更近的点

    return closest_points


def bilinear_interp(table, x, y):


    # 先处理真值比上计算值
    # if 判断 x y 在哪个方格内 判断大致位置 这里的x y 直接就是取的计算坐标值
    # 双线性插值本体
    # return real_x real_y 这里的 real_x real_y 直接就是得到的真实坐标值


    back_set = []
    grid_points = []
    for set in table:
        grid_points.append(set[0])
    which = find_closest_grid_points(grid_points, x, y)
    which.append([x, y])
    A = which
    x_coords = [point[0] for point in A]
    y_coords = [point[1] for point in A]

    # 绘制点
    plt.scatter(x_coords, y_coords, color='red')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot of Points')
    plt.grid(True)
    plt.show()
    pass

def gridTotabel(grid):

    table = []
    for item in grid:
        one = []
        set = []
        weight = []
        x = item.mean_x
        y = item.mean_y
        set.append(x)
        set.append(y)
        weight_x = item.weight_x
        weight_y = item.weight_y
        weight.append(weight_x)
        weight.append(weight_y)
        one.append(set)
        one.append(weight)
        table.append(one)

    return table



def draw_grid():
    # TODO 1,散点漂移半径和相对位置坐标的关系 看看是否每个点都画圆表示
    # TODO 2,Abs_deff 各个点位绝对差 标出最大值
    # TODO 3,膨胀收缩图
    x = []
    y = []
    z = []
    mean_x = []
    mean_y = []
    mean_z = []
    for item in grid:
        z.append(item.diff_distance)
        # x.append(item.posi_real_x)
        # y.append(item.posi_real_y)
        x.append(item.posi_real_x)
        y.append(item.posi_real_y)
        mean_x.append(item.mean_x)
        mean_y.append(item.mean_y)
        mean_z.append(1)
    # # 创建三维图形对象
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    #
    # # 绘制三维散点图
    # ax.scatter(x, y, z, c='b', marker='o')
    #
    # # 设置图形属性
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')
    # ax.set_title('3D Scatter Plot')
    # # ax.view_init(elev=30, azim=45)
    # ax.view_init(elev=30, azim=220)
    # # 显示图形
    # plt.show()
    # # ----------------------------------------------- abs_diif 均值和各个点的绝对差
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    xi, yi = np.meshgrid(xi, yi)

    # 插值
    zi = griddata((x, y), z, (xi, yi), method='cubic')

    # 绘制散点图
    plt.scatter(x, y, c=z, cmap='viridis')
    # plt.scatter(mean_x, mean_y, c=mean_z, alpha=0.07, cmap='inferno')
    plt.colorbar()

    # 显示
    plt.show()
    # -------------------------------------------------
    # # 生成网格点
    # xi = np.linspace(min(x), max(x), 100)
    # yi = np.linspace(min(y), max(y), 100)
    # xi, yi = np.meshgrid(xi, yi)
    #
    # # 进行插值
    # zi = griddata((x, y), z, (xi, yi), method='cubic')
    #
    # # 创建三维图形对象
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    #
    # # 绘制曲面
    # surf = ax.plot_surface(xi, yi, zi, cmap='viridis')
    #
    # # 设置图形属性
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')
    # ax.set_title('3D Surface Plot')
    # ax.view_init(elev=30, azim=220)
    #
    #
    # # 添加色标
    # fig.colorbar(surf)
    #
    # # 显示图形
    # plt.show()
    pass

    return


class deal_grid:
    global size_of_each_grid
    # index_x = ''
    # index_y = ''
    # index_z = ''
    # x = []
    # y = []
    # z = []
    # check_num = []
    # total = 0
    # mean_x = 0
    # mean_y = 0
    # mean_z = 0
    _calcu_sample = 10
    dropdata = 15   # 丢弃的前n个样本
    # __posi_ID = []
    # posi_real = []
    # posi_calcu_real = []

    def __init__(self, point):
        # strinit = "_"
        # strcome = str(type(point))
        # strinit += strcome[21:-2]     # 如果更改了外部类名，也可以读类名访问私有变量
        # self.index_x = strinit + "__x"
        # self.x = getattr(point, self.index_x)
        self.x = point._separate_data__x
        self.y = point._separate_data__y
        self.z = point._separate_data__z
        self.check_num = point._separate_data__check_num
        self.total = len(self.check_num)
        self.mean_each()
        self.posi_ID_x = int(point._separate_data__sn[0])  # sn只是用来计算推算真值坐标
        self.posi_ID_y = int(point._separate_data__sn[1])
        self.posi_real_x = self.posi_ID_x * wash.size_of_each_grid
        self.posi_real_y = self.posi_ID_y * wash.size_of_each_grid
        if self.posi_real_x == 0.0:  self.weight_x = 1.0
        else:
            self.weight_x = self.posi_real_x/self.mean_x       # 权重 = 真值 / 测量值
            self.weight_x = round(self.weight_x, 5)
        if self.posi_real_y == 0.0:  self.weight_y = 1.0
        else:
            self.weight_y = self.posi_real_y/self.mean_y
            self.weight_y = round(self.weight_y, 5)
        # self.posi_real_define = [1.2, 1.2]  # 分析单个点时手动设置的该点坐标
        self.abs_diff()

    def mean(self, lst):
        sum = 0
        for i in range(self._calcu_sample):
            sum = sum + lst[i + self.dropdata]
        return sum / self._calcu_sample

        # total = sum(lst)
        # length = len(lst)
        # if length == 0:
        #     return 0  # 避免除以零的情况
        # return total / length

    def mean_each(self):
        self.mean_x = self.mean(self.x)
        self.mean_x = round(self.mean_x, 5)
        self.mean_y = self.mean(self.y)
        self.mean_y = round(self.mean_y, 5)
        self.mean_z = self.mean(self.z)
        self.mean_z = round(self.mean_z, 5)

    def calcu_posi_mean(self):
        return

    def calcu_posi_real(self):
        return

    def abs_diff(self):
        diif_x = self.mean_x - self.posi_real_x
        diff_y = self.mean_y - self.posi_real_y
        self.diff_distance = math.sqrt(diif_x ** 2 + diff_y ** 2)
        # return diif_x, diff_y, diff_distance

    def error_range(self):
        return

    def long_time_diff(self):
        return

    def api_contour(self):
        """误差随位置变化的等高线图"""

        return  # posit_ID abs_diff

    def abs_diff_define(self):
        diif_x = self.mean_x - self.posi_real_x
        diff_y = self.mean_y - self.posi_real_y
        diff_distance = math.sqrt(diif_x ** 2 + diff_y ** 2)
        return diif_x, diff_y, diff_distance

    def to_dict(self):
        # 初始化空字典
        result = {}
        result['posi_ID_x'] = self.posi_ID_x
        result['posi_ID_y'] = self.posi_ID_y
        result['mean_x'] = self.mean_x
        result['mean_y'] = self.mean_y
        result['weight_x'] = self.weight_x
        result['weight_y'] = self.weight_y



        # # 获取类的所有属性和对应的值
        # attributes = vars(self)
        # # 将属性和值添加到字典中
        # for attr, value in attributes.items():
        #     result[attr] = value
        return result


class mash:
    scale = [0, 0]

grid = []
dicts = []
if __name__ == '__main__':
    def main():
        # group = []  # 用于接收每组清洗好的类
  # 用于接收待处理的格点
        # for i in range(wash.data_scale[0] * wash.data_scale[1]):  # 网格点文件遍历清洗
        #     group.append(wash.loop(wash.get_SN()))
        # with open('saved_group.pkl', 'wb') as f:
        #     pickle.dump(group, f)
        global grid
        global dicts
        with open('saved_group.pkl', 'rb') as f:
            group = pickle.load(f)
        for item in group:
            grid.append(deal_grid(item))
        # for item in grid:
        #     dicts.append(item.to_dict())

        with open('interp_table.txt', 'w') as f:
            for detail in grid:
                # 将对象的属性按照指定格式写入到文件中
                f.write(f"posi_ID_x:{detail.posi_ID_x}posi_ID_y:{detail.posi_ID_y}mean_x:{detail.mean_x}mean_y:{detail.mean_y}weight_x:{detail.weight_x}weight_y:{detail.weight_y}\n")
                # json.dump(detail, f)

        # draw_grid()
        # x = 0.47        # 例子
        # y = 2.05
        # table = gridTotabel(grid)
        # with open('output.txt', 'w') as f:
        #     # 遍历列表中的每个子列表
        #     for sublist in table:
        #         # 将子列表中的每个元素转换为字符串，并使用逗号分隔
        #         line = ','.join(map(str, sublist))
        #         # 将转换后的字符串写入文件，并添加换行符
        #         f.write(line + '\n')
        # # bilinear_interp(table, x, y)
        pass

    main()
