import sympy as sp

# ======================
# SymPy 符号计算工具箱
# 电工杯/数学建模专用
# ======================

def get_sym(var_str='x'):
    """快速获取符号变量"""
    return sp.symbols(var_str)

def simplify_expr(expr):
    """化简表达式"""
    return sp.simplify(expr)

def derivative(expr, var='x'):
    """求导：返回 表达式 + LaTeX"""
    x = sp.symbols(var)
    res = sp.diff(expr, x)
    return res, sp.latex(res)

def integral(expr, var='x'):
    """不定积分：返回 表达式 + LaTeX"""
    x = sp.symbols(var)
    res = sp.integrate(expr, x)
    return res, sp.latex(res)

def solve_eq(expr, var='x'):
    """解方程 f(x)=0"""
    x = sp.symbols(var)
    return sp.solve(expr, x)

def to_latex(expr):
    """转论文LaTeX公式"""
    return sp.latex(expr)