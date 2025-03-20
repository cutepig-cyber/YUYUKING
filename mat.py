import numpy as np
import matplotlib.pyplot as plt

# 设置全局字体和图像分辨率
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
plt.rcParams['figure.dpi'] = 100              # 图像分辨率

# 生成连续信号：余弦波
t = np.arange(-2, 2, 0.01)                   # 连续时间点
continuous_signal = np.cos(2 * np.pi * t)    # 2Hz连续余弦信号

# 生成离散信号：单位阶跃序列
n = np.arange(-5, 6)                         # 离散时间点（整数）
discrete_signal = np.where(n >= 0, 1, 0)     # 单位阶跃信号

# 创建画布
plt.figure(figsize=(10, 4))

# 绘制连续信号
plt.subplot(1, 2, 1)
plt.plot(t, continuous_signal)
plt.title('连续余弦信号')
plt.xlabel('时间 (秒)')
plt.ylabel('幅度')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# 绘制离散信号
plt.subplot(1, 2, 2)
markerline, stemlines, baseline = plt.stem(n, discrete_signal)
plt.setp(markerline, markersize=8, color='red', marker='o')
plt.setp(stemlines, color='blue', linewidth=2)
plt.title('离散单位阶跃序列')
plt.xlabel('样本序号')
plt.ylabel('幅度')
plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(n)  # 明确显示所有离散点

# 调整布局并显示
plt.tight_layout()
plt.show()