import numpy as np

# 读取bin文件，假设每个点有4个属性（x, y, z, intensity）
points = np.fromfile("D:/all/bin/mianzhen/7592.699519800.bin", dtype=np.float32).reshape(-1, 4)

# 保存为npy文件，文件名与bin文件相同
np.save("D:/all/npy", points)
