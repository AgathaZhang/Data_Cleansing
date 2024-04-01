# with open("00.DAT", "r") as f:
#     data = f.readline()
#     print(data)

# with open("00.DAT", 'rb') as f:
# with open("00.txt", 'r', encoding='UTF-8') as f:
# #     data = f.readline()
# #     print(data)
#     # datadict = pickle.load(f, encoding='latin1')
#
# # with open("00.txt", 'r') as f:
#     data = f.read()
#     # datadict = pickle.load(f)
#     # X = datadict['data']
#     pass

# with open("00.txt", 'rb') as f:
#     data = f.read()
#
#     print(data)
#     b4 = bytes('Python:,,2323资料', encoding='UTF-8')
#     print("b4: ", b4)
#     pass
#     # datadict = pickle.load(f, encoding='latin1')


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
import numpy as np

    # X = np.loadtxt("exp4/normal.txt", delimiter=",", dtype=np.float32)
    # pca = PCA(n_components=2)
    # newX = pca.fit_transform(X)
    # print(pca.explained_variance_ratio_)
    # xs = newX[:, 0]
    # ys = newX[:, 1]
    # plt.xlabel('component_x')
    # plt.ylabel('component_y')
    # # 沿x轴方向渐变颜色
    # plt.scatter(xs, ys, c=xs)

# 设置坐标轴范围
# plt.xlim((0, 360))
# plt.ylim((0, 240))
# 设置坐标轴名称

# pca = PCA(n_components=2)
# newX = pca.fit_transform(item.z)
# print(pca.explained_variance_ratio_)
# plt.xlabel('component_x')
# plt.ylabel('component_y')
# plt.scatter(item.x, item.y, item.z)

# def number_to_string_and_join(numbers):
#
#
#
# numbers_list = [1, 2, 3, 4, 5]
# result_string = number_to_string_and_join(numbers_list)
# print("连接后的字符串:", result_string)


# def outer_function(static_variable=[0]):
#     static_variable[0] += 1
#     print(static_variable[0])
#
# outer_function()
# outer_function()
# pass

# str_numbers = [str(num) for num in numbers]
# joined_string = ''.join(str_numbers)
# return joined_string


# import matplotlib.pyplot as plt
#
# # 生成数据
# x = [1, 2, 3, 4, 5]
# y = [1, 2, 3, 4, 5]
#
# # 创建画布和子图
# (fig, ax) = plt.subplots()
#
# # 循环绘制每个点
# for i in range(len(x)):
#     if i < len(x) - 1:
#         # 对前四个点设置渐变颜色
#         color = (i / (len(x) - 1), 0, 1 - i / (len(x) - 1))
#         ax.scatter(x[i], y[i], color=color, label=f'Point {i+1}')
#     else:
#         # 最后一个点使用不同的符号标记
#         ax.scatter(x[i], y[i], color='red', marker='x', label=f'Point {i+1}')
#
# # 添加图例
# ax.legend()
#
# # 显示图形
# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.patches import Circle
#
# # 定义三组坐标
# coordinates = [
#     np.array([(1, 2), (2, 3), (3, 4)]),
#     np.array([(4, 5), (5, 6), (6, 7)]),
#     np.array([(7, 8), (8, 9), (9, 10)])
# ]
#
# # 绘制每组坐标点
# for i, group in enumerate(coordinates):
#     x, y = zip(*group)
#     plt.scatter(x, y, label=f'Group {i+1}')
#
# # 计算每组的重心并绘制
# for i, group in enumerate(coordinates):
#     center = np.mean(group, axis=0)
#     plt.scatter(center[0], center[1], color='black', marker='x', label=f'Center of Group {i+1}')
#
# # 绘制每组坐标点的外切圆
# for group in coordinates:
#     center = np.mean(group, axis=0)
#     radius = max(np.linalg.norm(point - center) for point in group)
#     circle = Circle(center, radius, fill=False, color='red', linestyle='--')
#     plt.gca().add_patch(circle)
#
# # 添加图例
# plt.legend()
#
# # 显示图形
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Coordinates and Their Centers')
# plt.gca().set_aspect('equal', adjustable='box')
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.patches import Circle
#
# # 生成三组随机坐标
# num_points = 10
# coordinates = [
#     np.random.rand(num_points, 2),  # 第一组随机坐标
#     np.random.rand(num_points, 2),  # 第二组随机坐标
#     np.random.rand(num_points, 2)   # 第三组随机坐标
# ]
#
# # 绘制每组坐标点，并计算重心并绘制
# for i, group in enumerate(coordinates):
#     x, y = group[:, 0], group[:, 1]
#     plt.scatter(x, y, label=f'Group {i+1}')
#
#     # 计算重心并绘制
#     center = np.mean(group, axis=0)
#     plt.scatter(center[0], center[1], color='black', marker='x', label=f'Center of Group {i+1}')
#
#     # 计算外切圆并绘制
#     radius = max(np.linalg.norm(point - center) for point in group)
#     circle = Circle(center, radius, fill=False, color='red', linestyle='--')
#     plt.gca().add_patch(circle)
#
# # 添加图例
# plt.legend()
#
# # 显示图形
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Random Coordinates and Their Centers')
# plt.gca().set_aspect('equal', adjustable='box')
# plt.grid(True)
# plt.show()
#------------------------------------------------------------------------------------------
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.patches import Circle
#
# # 生成随机坐标
# np.random.seed(0)
# num_points = 10
# coordinates = np.random.rand(num_points, 2) * 10
#
# # 绘制坐标点
# plt.scatter(coordinates[:, 0], coordinates[:, 1], color='blue', label='Coordinates')
#
# # 计算重心并绘制
# center = np.mean(coordinates, axis=0)
# plt.scatter(center[0], center[1], color='red', marker='x', label='Center')
#
# # 计算外切圆并绘制
# radius = max(np.linalg.norm(point - center) for point in coordinates)
# circle = Circle(center, radius, fill=False, color='green', linestyle='--', label='Bounding Circle')
# plt.gca().add_patch(circle)
#
# # 添加图例
# plt.legend()
#
# # 设置图形属性
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Random Coordinates and Their Center with Bounding Circle')
# plt.gca().set_aspect('equal', adjustable='box')
# plt.grid(True)
#
# # 显示图形
# plt.show()
# -----------------------------------------------------------------------------------
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.patches import Circle
#
# # 生成随机坐标
# np.random.seed(0)
# num_points = 10
# coordinates = np.random.rand(num_points, 2) * 10
#
# # 绘制坐标点
# plt.scatter(coordinates[:, 0], coordinates[:, 1], color='blue', label='Coordinates')
#
# # 计算重心并绘制
# center = np.mean(coordinates, axis=0)
# plt.scatter(center[0], center[1], color='red', marker='x', label='Center')
#
# # 计算外切圆并绘制
# radius = max(np.linalg.norm(point - center) for point in coordinates)
# circle = Circle(center, radius, fill=False, color='green', linestyle='--', label=f'Bounding Circle (radius={radius:.2f})')
# plt.gca().add_patch(circle)
#
# # 添加标注
# plt.text(center[0] + radius, center[1], f'radius={radius:.2f}', verticalalignment='center', color='green')
#
# # 添加图例
# plt.legend()
#
# # 设置图形属性
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Random Coordinates and Their Center with Bounding Circle')
# plt.gca().set_aspect('equal', adjustable='box')
# plt.grid(True)
#
# # 显示图形
# plt.show()
# -----------------------------------------------------------------------------------
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.patches import Circle
#
# # 生成两组随机坐标
# np.random.seed(0)
# num_points = 10
# coordinates1 = np.random.rand(num_points, 2) * 10
# coordinates2 = np.random.rand(num_points, 2) * 10
#
# # 绘制第一组坐标点
# plt.scatter(coordinates1[:, 0], coordinates1[:, 1], color='blue', label='Group 1')
#
# # 绘制第二组坐标点
# plt.scatter(coordinates2[:, 0], coordinates2[:, 1], color='red', label='Group 2')
#
# # 计算并绘制第一组重心
# center1 = np.mean(coordinates1, axis=0)
# plt.scatter(center1[0], center1[1], color='blue', marker='x', label='Center of Group 1')
#
# # 计算并绘制第二组重心
# center2 = np.mean(coordinates2, axis=0)
# plt.scatter(center2[0], center2[1], color='red', marker='x', label='Center of Group 2')
#
# # 计算并绘制第一组外切圆
# radius1 = max(np.linalg.norm(point - center1) for point in coordinates1)
# circle1 = Circle(center1, radius1, fill=False, color='blue', linestyle='--', label=f'Bounding Circle (radius={radius1:.2f})')
# plt.gca().add_patch(circle1)
#
# # 添加第一组外切圆半径标注
# plt.text(center1[0] + radius1, center1[1], f'radius={radius1:.2f}', verticalalignment='center', color='blue')
#
# # 计算并绘制第二组外切圆
# radius2 = max(np.linalg.norm(point - center2) for point in coordinates2)
# circle2 = Circle(center2, radius2, fill=False, color='red', linestyle='--', label=f'Bounding Circle (radius={radius2:.2f})')
# plt.gca().add_patch(circle2)
#
# # 添加第二组外切圆半径标注
# plt.text(center2[0] + radius2, center2[1], f'radius={radius2:.2f}', verticalalignment='center', color='red')
#
# # 添加图例
# plt.legend()
#
# # 设置图形属性
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Random Coordinates and Their Centers with Bounding Circles')
# plt.gca().set_aspect('equal', adjustable='box')
# plt.grid(True)
#
# # 显示图形
# plt.show()
# ----------------------------------------------------------------------
# def draw_old(item):
#     x = item.x
#     y = item.y
#     # --------------------------------------------------------------- # 二维网图
#     # 绘制 x-y 点图
#     # plt.figure(figsize=(8, 6))  # 设置图形的大小
#     plt.plot(x, y, 'o', color='blue', label='Points')
#     plt.xlabel('x Axis')
#     plt.ylabel('y Axis')
#
#     # 设置坐标轴刻度
#     # plt.xticks(my_x_ticks)
#     # plt.yticks(my_y_ticks)
#     # surf = ax1.plot_wireframe(X, Y, Z)
#
#     plt.show()
#     global current_completion_flag
#     current_completion_flag = False
#
#     return
#
#         global x_draw
#         global y_draw
#         x_draw.append(0.8)
#         y_draw.append(0.8)
#
#         (fig, ax) = plt.subplots()
#
#         # 循环绘制每个点
#         for i in range(len(x_draw)):
#             if i < len(x_draw) - 1:
#                 # 对前四个点设置渐变颜色
#                 color = (i / (len(x_draw) - 1), 0, 1 - i / (len(x_draw) - 1))
#                 ax.scatter(x_draw[i], y_draw[i], color=color, label=f'P {i + 1}')
#             else:
#                 # 最后一个点使用不同的符号标记
#                 ax.scatter(x_draw[i], y_draw[i], color='red', marker='x', label=f'P {i + 1}')
#
#         # 添加图例
#         ax.legend()
#
#         # 显示图形
#         plt.show()
#         # plt.plot(x_draw, y_draw, 'o', color='blue', label='Points')
#         # plt.xlabel('x Axis')
#         # plt.ylabel('y Axis')
#         # plt.show()
#
#         # TODO 输出文件for 遍历到不同的文件中


# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.patches import Circle
#
# # 生成两组随机坐标和一个随机点
# np.random.seed(0)
# num_points = 10
# coordinates1 = np.random.rand(num_points, 2) * 10
# coordinates2 = np.random.rand(num_points, 2) * 10
# random_point = np.random.rand(1, 2) * 10
#
# # 绘制第一组坐标点
# plt.scatter(coordinates1[:, 0], coordinates1[:, 1], color='blue', label='Group 1')
#
# # 绘制第二组坐标点
# plt.scatter(coordinates2[:, 0], coordinates2[:, 1], color='red', label='Group 2')
#
# # 绘制随机点
# plt.scatter(random_point[:, 0], random_point[:, 1], color='green', label='Random Point')
#
# # 计算并绘制第一组重心
# center1 = np.mean(coordinates1, axis=0)
# plt.scatter(center1[0], center1[1], color='blue', marker='x', label='Center of Group 1')
#
# # 计算并绘制第二组重心
# center2 = np.mean(coordinates2, axis=0)
# plt.scatter(center2[0], center2[1], color='red', marker='x', label='Center of Group 2')
#
# # 计算并绘制第一组外切圆
# radius1 = max(np.linalg.norm(point - center1) for point in coordinates1)
# circle1 = Circle(center1, radius1, fill=False, color='blue', linestyle='--', label=f'Bounding Circle (radius={radius1:.2f})')
# plt.gca().add_patch(circle1)
#
# # 添加第一组外切圆半径标注
# plt.text(center1[0] + radius1, center1[1], f'radius={radius1:.2f}', verticalalignment='center', color='blue')
#
# # 计算并绘制第二组外切圆
# radius2 = max(np.linalg.norm(point - center2) for point in coordinates2)
# circle2 = Circle(center2, radius2, fill=False, color='red', linestyle='--', label=f'Bounding Circle (radius={radius2:.2f})')
# plt.gca().add_patch(circle2)
#
# # 添加第二组外切圆半径标注
# plt.text(center2[0] + radius2, center2[1], f'radius={radius2:.2f}', verticalalignment='center', color='red')
#
# # 绘制连线并标注距离
# plt.plot([center1[0], random_point[0, 0]], [center1[1], random_point[0, 1]], color='blue', linestyle='--')
# distance1 = np.linalg.norm(center1 - random_point)
# plt.text((center1[0] + random_point[0, 0]) / 2, (center1[1] + random_point[0, 1]) / 2, f'distance={distance1:.2f}', color='blue')
#
# plt.plot([center2[0], random_point[0, 0]], [center2[1], random_point[0, 1]], color='red', linestyle='--')
# distance2 = np.linalg.norm(center2 - random_point)
# plt.text((center2[0] + random_point[0, 0]) / 2, (center2[1] + random_point[0, 1]) / 2, f'distance={distance2:.2f}', color='red')
#
# # 添加图例
# plt.legend()
#
# # 设置图形属性
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Random Coordinates, Their Centers and Bounding Circles')
# plt.gca().set_aspect('equal', adjustable='box')
# plt.grid(True)
#
# # 显示图形
# plt.show()
#
# x = [1, 2, 3]
# y = [4, 3, 2]
#
# # 使用列表推导式转换点的形式
# points = [[x[i], y[i]] for i in range(len(x))]
#
# # 打印转换后的点
# for i, point in enumerate(points):
#     print(f'p[{i}] = {point}')
#
#     # 计算并绘制第一组重心
#     # center = np.empty((0, 0))
#     # for i in range(len(band)):
#     #     center[i] = np.mean(band[i][20:40], axis=0)
#     # plt.scatter(center[i][0], center[i][1], color='blue', marker='x', label='Center 1')
#
#     # 计算并绘制第二组重心

# class MyClass:
#     pass
#
# obj = MyClass()
#
# # 获取对象所属的类
# obj_class = type(obj)
# a = obj_class
# print("Object belongs to class:", obj_class)

# class ClassA:
#     def __init__(self, value):
#         self.__private_attr = value
#
#
# # 创建 ClassA 和 ClassB 的实例
# obj_a = ClassA(100)
#
# # 访问 obj_a 的私有属性
# strobj = type(obj_a)
# over = str(strobj)
# a = '_'
# for i in range(17, 23):
#     a += over[i]
# a += "__private_attr"
#
# value_a = getattr(obj_a, a)
# print("ClassA private attribute value:", value_a)

# class MyClass:
#     class_attr = []
#
#     def __init__(self, value):
#         self.instance_attr = value
#
# # 实例化两个对象
# obj1 = MyClass(1)
# obj2 = MyClass(2)
#
# # 修改obj1的实例属性
# obj1.instance_attr = 10
#
# # 修改obj1的类属性
# obj1.class_attr.append(100)
#
# # 打印obj1的属性
# print("obj1 instance_attr:", obj1.instance_attr)
# print("obj1 class_attr:", obj1.class_attr)
#
# # 打印obj2的属性
# print("obj2 instance_attr:", obj2.instance_attr)
# print("obj2 class_attr:", obj2.class_attr)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# # 生成随机三维数据
# np.random.seed(0)
# num_points = 100
# x = np.random.normal(size=num_points)
# y = np.random.normal(size=num_points)
# z = np.random.normal(size=num_points)
#
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
#
# # 添加色标
# fig.colorbar(surf)
#
# # 显示图形
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# # 数据
# x = np.random.rand(100)
# y = np.random.rand(100)
# z = np.random.rand(100)
#
# # 绘图
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x, y, z)
#
# # 设置坐标轴标签
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# # 显示图形，并允许旋转
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.animation import FuncAnimation
#
# # 创建数据
# x = np.random.rand(100)
# y = np.random.rand(100)
# z = np.random.rand(100)
#
# # 创建图形和轴
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# sc = ax.scatter(x, y, z)
#
# # 设置坐标轴标签
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# # 定义动画函数
# def update(frame):
#     ax.view_init(elev=10, azim=frame)
#
# # 创建动画
# ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=50)
#
# # 显示动画
# plt.show()

# def find_surrounding_grid_points(x, y):
#     """
#     找到给定坐标所在的四个网格点。
#
#     参数:
#     x (float): x 坐标。
#     y (float): y 坐标。
#
#     返回值:
#     list: 包含四个网格点坐标的列表。
#     """
#     # 向下取整获得网格点的坐标
#     x1, y1 = int(x), int(y)
#     x2, y2 = x1 + 1, y1 + 1
#
#     # 返回四个网格点的坐标
#     return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
#
# # 示例用法
# x_coord = 2.5
# y_coord = 3.7
# grid_points = find_surrounding_grid_points(x_coord, y_coord)
# print("给定坐标所在的四个网格点：", grid_points)

# def find_closest_grid_points(x, y, grid_points):
#     """
#     找到给定坐标所在的四个网格点。
#
#     参数:
#     x (float): x 坐标。
#     y (float): y 坐标。
#     grid_points (list of tuple): 多边形网格点的坐标列表。
#
#     返回值:
#     list: 包含四个网格点坐标的列表。
#     """
#     closest_points = []
#
#     # 遍历网格点，找到距离给定坐标最近的四个网格点
#     for point in grid_points:
#         if len(closest_points) < 4:
#             closest_points.append(point)
#         else:
#             distances = [((x - px) ** 2 + (y - py) ** 2) for px, py in closest_points]      # 遍历该点到四个点中每个点的距离 存在distance里
#             max_distance_index = distances.index(max(distances))                            # 找出距离最大点的索引
#             distance_to_point = (x - point[0]) ** 2 + (y - point[1]) ** 2                   # 找出第五个点的距离
#             if distance_to_point < distances[max_distance_index]:                           # 从第五个点开始，该点如果小于距离最大点
#                 closest_points[max_distance_index] = point                                  # 该点替换为更近的点
#
#     return closest_points
#
# # 示例用法
# polygon_grid_points = [(0.3, 0), (0, 1), (1, 1), (1, 0)]
# x_coord = 0.5
# y_coord = 0.6
# closest_points = find_closest_grid_points(x_coord, y_coord, polygon_grid_points)
# print("给定坐标所在的四个网格点：", closest_points)
# pass

# my_list = [[1.0, 2], [1.22, 444], [1.22, 444], [1.22, 444]]
#
# # 打开一个文本文件，以写入模式打开（'w'）
# with open('output.txt', 'w') as f:
#     # 将列表中的每个元素写入到文件中
#     for item in my_list:
#         f.write(item + '\n')
#
# print("列表已成功写入到文件 output.txt 中。")

class deal_grid:
    mean_x = 0
    mean_y = 0
    _mean_z = 0
    _calcu_sample = 10
    dropdata = 15
