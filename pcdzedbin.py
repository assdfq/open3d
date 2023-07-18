import open3d as o3d
import numpy as np
import os

# 定义pcd文件和bin文件的目录
pcd_dir = "D:/all/pcd1/pcddianyun/"
bin_dir = "D:/all/bin/pcddianyun/"

# 如果bin目录不存在，创建一个
if not os.path.exists(bin_dir):
    os.makedirs(bin_dir)

# 遍历pcd目录下的所有文件
for file in os.listdir(pcd_dir):
    # 如果文件是pcd格式，读取并转换
    if file.endswith(".pcd"):
        # 读取pcd文件
        pcd = o3d.io.read_point_cloud(pcd_dir + file)

        # 将点云数据转换为numpy数组，只保留xyz坐标
        points = np.asarray(pcd.points)[:, :3]
        points.tofile(bin_dir + file.replace(".pcd", ".bin"))