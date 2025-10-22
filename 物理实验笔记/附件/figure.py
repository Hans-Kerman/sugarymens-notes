import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 设置Matplotlib支持中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
def linear_function(x, w, b):
    return w * x + b

# 此处填入你的数据，x轴为滑块位置的平方，y轴为转动惯量
x_data = np.array([25, 100, 225, 400,625])
y_data = np.array([1.31795, 4.875, 10.821, 19.149, 29.88])

# 使用curve_fit进行线性拟合
params, covariance = curve_fit(linear_function, x_data, y_data)

w_fit, b_fit = params

y_fit = linear_function(x_data, w_fit, b_fit)

# 计算R^2值
ss_res = np.sum((y_data - y_fit) ** 2)
ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)
r_squared = 1 - (ss_res / ss_tot)


plt.scatter(x_data, y_data,  facecolors='none', edgecolors='black')
x_fit = np.linspace(0, 700, 100)
y_fit = linear_function(x_fit, w_fit, b_fit)


plt.plot(x_fit, y_fit, color='black')
plt.xlabel(r'$X^2/ \times 10^{-4} m^2$')
plt.ylabel(r'$I_x/ \times 10^{-3} kg \cdot m^2$')

plt.figtext(0.4, 0.6, fr'$I_x = {w_fit:.4f}x^2 + {b_fit:.4f}$', 
            ha='center', fontsize=8)
plt.figtext(0.4, 0.55, fr'$R^2 = {r_squared:.4f}$', 
            ha='center', fontsize=8)
plt.figtext(0.5, 0,r'验证平行轴定理$I_x \sim x^2$ 图线', ha='center', fontsize=14)

plt.grid(False)
plt.show()