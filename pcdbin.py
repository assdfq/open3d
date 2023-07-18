import numpy as np
import open3d as o3d
import struct
import os

# 定义一个转换函数，输入是一个pcd文件路径，输出是一个bin文件路径
def pcd2bin(pcd_path, bin_path):
  # 读取pcd文件
    pcd = o3d.io.read_point_cloud(pcd_path)

  # 将点云数据转换为numpy数组，假设每个点有4个属性（x, y, z, intensity）
    points = np.asarray(pcd.points)

  # 打开bin文件，以二进制写入模式
    with open(bin_path, "wb") as f:
    # 遍历每个点，将其属性打包为4个浮点数，写入bin文件
        for x, y, z,intensity in points:
            f.write(struct.pack("ffff", x, y,z,intensity))

# 定义pcd文件和bin文件的目录
pcd_dir = "D:/all/pcd1/mianzhen/"
bin_dir = "D:/all/bin/mianzhen/"


# 如果bin目录不存在，创建一个
if not os.path.exists(bin_dir):
    os.makedirs(bin_dir)

# 遍历pcd目录下的所有文件
for file in os.listdir(pcd_dir):
    # 如果文件是pcd格式，读取并转换
    if file.endswith(".pcd"):
        # 调用转换函数，文件名与pcd文件相同
        pcd2bin(pcd_dir + file, bin_dir + file.replace(".pcd", ".bin"))



