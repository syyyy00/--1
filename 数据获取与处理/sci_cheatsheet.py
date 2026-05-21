
# ======================
# SciPy 常用工具速查手册
# 数学建模比赛直接复制用
# ======================

import numpy as np

# ----------------------
# 1. 最小化优化（找最小值）
# ----------------------
def demo_optimize():
    from scipy.optimize import minimize
    def f(x):
        return x**2 + 3*x + 5  # 要最小化的函数
    res = minimize(f, x0=0)
    return res.x

# ----------------------
# 2. 常微分方程求解（高频）
# ----------------------
def demo_ode():
    from scipy.integrate import solve_ivp
    def dydt(t, y):
        return -2 * y  # y’ = -2y
    sol = solve_ivp(dydt, [0,5], [1], t_eval=np.linspace(0,5,50))
    return sol.t, sol.y[0]

# ----------------------
# 3. 1D 插值（补数据点）
# ----------------------
def demo_interp(x, y, x_new):
    from scipy.interpolate import interp1d
    f = interp1d(x, y, kind='linear')
    return f(x_new)

# ----------------------
# 4. 曲线拟合
# ----------------------
def demo_curve_fit(x, y, func):
    from scipy.optimize import curve_fit
    popt, _ = curve_fit(func, x, y)
    return popt