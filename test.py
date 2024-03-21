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

    X = np.loadtxt("exp4/normal.txt", delimiter=",", dtype=np.float32)
    pca = PCA(n_components=2)
    newX = pca.fit_transform(X)
    print(pca.explained_variance_ratio_)
    xs = newX[:, 0]
    ys = newX[:, 1]
    plt.xlabel('component_x')
    plt.ylabel('component_y')
    # 沿x轴方向渐变颜色
    plt.scatter(xs, ys, c=xs)

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

