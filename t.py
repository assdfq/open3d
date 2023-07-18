import numpy as np

# 读取.npy文件，假设是一个N*4的数组，每个点有4个属性（x, y, z, intensity）
array = np.load("D:/all/npy.npy")

# 保存为txt文件，使用空格分隔每个元素，换行分隔每一行
np.savetxt("D:/all/npy.txt", array, delimiter=" ")