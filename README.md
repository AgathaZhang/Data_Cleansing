# Data cleansing of co-ordinate data
For reference

This is a data processor of cleaning and refining raw data to improve its quality and accuracy.
    
The raw data is a set of log text containing three dimensional coordinate points.

This contains the original log data that needs to be cleaned, and I hope that some of the processing methods of the algorithm can be shared with you.

![test_scene 图标](https://github.com/AgathaZhang/Data_Cleansing/blob/master/docs/test_scene.jpg)

偏移位置的分析数据
多次定位同一点的一致性评估

![result_0 图标](https://github.com/AgathaZhang/Data_Cleansing/blob/master/docs/一致性.png)

平均定位点与真值点的网格分布图

![result_1 图标](https://github.com/AgathaZhang/Data_Cleansing/blob/master/docs/20组点平均计算坐标和真值格点对照0327.png)

UWB膨胀收缩势图（定位计算点与真值点距离差）

![result_2 图标](https://github.com/AgathaZhang/Data_Cleansing/blob/master/docs/20组点平均计算坐标和真值格点对照03272.png)

定位点跳变分散性在全局坐标系位置中的关系
结论：可以看到四个基站所围起来的全局坐标系下 靠近坐标系中心的位置，基准稳定度非常好，靠近坐标系边界时出现跳变误差，并且初步看来，这种误差存在一定的方向性：
1，误差可能是在边界上TAG与基站的极限拓扑构型（共线或共点导致）
2，误差在右上角边界的跳变更大，是否意味着现有天线波束指向性影响了计算距离，导致多径返回的距离参与到了计算中

![result_3 图标](https://github.com/AgathaZhang/Data_Cleansing/blob/master/docs/分散性分析2.png)

