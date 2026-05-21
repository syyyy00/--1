import numpy as np

# ----------------------
# 1. 解线性方程组 Ax = b
# ----------------------
def solve_linear(A, b):
    """
    解线性方程组 A @ x = b
    A：系数矩阵
    b：右侧向量
    返回：解 x
    """
    return np.linalg.solve(A, b)

# ----------------------
# 2. 多项式拟合（非常常用）
# ----------------------
def poly_fit(x, y, degree):
    """
    多项式拟合
    x, y：数据点
    degree：次数（1=直线，2=抛物线）
    返回：多项式系数（高次 → 低次）
    """
    return np.polyfit(x, y, degree)

# ----------------------
# 3. 数值积分（梯形法）
# ----------------------
def numerical_integral(func, a, b, n=1000):
    """
    计算函数从 a 到 b 的积分
    func：函数
    a, b：上下限
    """
    x = np.linspace(a, b, n)
    y = func(x)
    return np.trapz(y, x)

# ----------------------
# 4. 矩阵基本运算（备用）
# ----------------------
def matrix_ops(A):
    """返回转置、逆、特征值"""
    return {
        "T": A.T,
        "inv": np.linalg.inv(A),
        "eig": np.linalg.eigvals(A)
    }