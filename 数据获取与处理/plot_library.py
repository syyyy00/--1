import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ======================
# 全局绘图设置（论文级质量）
# ======================
plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti SC', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False  # 负号正常显示
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'

# ======================
# 1. 多系列折线图（最常用：负荷曲线、预测对比）
# ======================
def plot_lines(x, y_dict, xlabel='时间', ylabel='值', title='折线图',
               save_path=None, figsize=(10,5), linewidth=2, marker=None):
    plt.figure(figsize=figsize)
    for label, y in y_dict.items():
        plt.plot(x, y, label=label, linewidth=linewidth, marker=marker, markersize=4)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    if save_path:
        plt.savefig(save_path)
    plt.show()

# ======================
# 2. 散点图（相关性、误差分布）
# ======================
def scatter_plot(x, y, xlabel='X', ylabel='Y', title='散点图',
                 alpha=0.6, color='steelblue', save_path=None, figsize=(8,5)):
    plt.figure(figsize=figsize)
    plt.scatter(x, y, alpha=alpha, color=color, edgecolors='w', s=60)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    plt.show()

# ======================
# 3. 热力图（相关系数、时空分布）
# ======================
def heatmap(matrix, x_labels=None, y_labels=None, title='热力图',
            cmap='coolwarm', annot=True, fmt='.2f', save_path=None, figsize=(10,8)):
    plt.figure(figsize=figsize)
    sns.heatmap(matrix, xticklabels=x_labels, yticklabels=y_labels,
                cmap=cmap, annot=annot, fmt=fmt, linewidths=0.5)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    plt.show()

# ======================
# 4. 3D 曲面图（优化曲面、二维分布）
# ======================
def plot_3d_surface(x, y, Z, xlabel='X', ylabel='Y', zlabel='Z', title='3D曲面',
                    view_angle=(30, 45), save_path=None, figsize=(10,7)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    ax.view_init(view_angle[0], view_angle[1])
    fig.colorbar(surf, shrink=0.5, aspect=10)
    if save_path:
        plt.savefig(save_path)
    plt.show()