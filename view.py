import numpy as np
import open3d as o3d

# 读取.bin文件，假设每个点有4个属性（x, y, z, intensity）
points = np.fromfile("D:/all/bin/pcddianyun/1687253540.805808536.bin", dtype=np.float32).reshape(-1, 4)

# 将numpy数组转换为open3d的点云对象
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points[:, :3])

# 可视化点云
o3d.visualization.draw_geometries([pcd])
