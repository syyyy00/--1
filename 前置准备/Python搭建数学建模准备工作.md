## 第一步：搭建统一开发环境

**目的**：避免库版本冲突，保证代码在任何机器上都能跑。  
**动作**：
1. 安装 Anaconda（推荐）或 Miniconda。装好后打开 **Anaconda Prompt**（或终端）。
2. 新建一个专用环境，并安装所有必备库：
   创建环境：
   conda create -n mathmodel python=3.10 -y
   激活环境：
   conda activate mathmodel
   安装所有必备库：
   pip install numpy pandas scipy sympy matplotlib seaborn plotly openpyxl xlrd jupyter

3. 验证安装：
在 (mathmodel) 环境下输入：
   python
   import numpy as np
   import pandas as pd
   import scipy, sympy, matplotlib, seaborn, plotly
   print("All OK")
退出 Python：
   exit()
**产出**：一个名为 `mathmodel` 的稳定 Python 环境。以后所有练习和比赛都在这个环境下进行。

如何使用（在 Anaconda Prompt 里输）
方法 A：用 Jupyter
1.进入你的文件夹
H:
cd H:\2411607018翁佳琦\电工杯\电工杯数学建模竞赛
2.启动 jupyter
jupyter notebook

方法 B：用 VS Code
1.conda activate mathmodel
2.code
3.选择解释器
按 Ctrl + Shift + P
输入plaintext
Python: Select Interpreter选择Python 3.10 (mathmodel)

常规操作：
conda activate mathmodel
H:
cd H:\2411607018翁佳琦\电工杯\电工杯数学建模竞赛
jupyter notebook
## 第二步：数据读写技能——打造你自己的数据 I/O 助手

**目的**：快速读取题目给的数据文件（CSV、Excel），处理完又能保存为指定格式，不再被编码和路径问题纠缠。  

**需要掌握的技能点**：

### 2.1 用 Pandas 读取 CSV / Excel
- **中文路径、编码问题**：读取时指定 `encoding='gbk'` 或 `utf-8`。
- **跳过表头说明行**：用 `skiprows` 参数。
- **读取多个sheet**：`pd.read_excel` 加上 `sheet_name=None` 返回字典。

**可复用代码模板**：创建一个 `data_io.py` 文件
```python
import pandas as pd

def read_data(file_path, **kwargs):
    """
    自动判断 CSV 或 Excel，读取数据。
    支持额外参数如 encoding='gbk', skiprows=1 等。
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path, **kwargs)
    elif file_path.endswith(('.xls', '.xlsx')):
        return pd.read_excel(file_path, **kwargs)
    else:
        raise ValueError("Unsupported file format")

def save_data(df, file_path, index=False, **kwargs):
    """保存数据框，自动识别格式"""
    if file_path.endswith('.csv'):
        df.to_csv(file_path, index=index, **kwargs)
    elif file_path.endswith(('.xls', '.xlsx')):
        df.to_excel(file_path, index=index, **kwargs)
    else:
        raise ValueError("Unsupported file format")
```

**练习**：找一份电工杯真题的数据（比如负荷数据），用 `read_data` 读进来，打印前5行和列名。确认中文不乱码。


## 第三步：数值计算核心——NumPy + SciPy

**目的**：比赛中涉及的任何矩阵运算、线性方程组求解、数值积分、优化、拟合，都能用一行代码搞定。

### 3.1 NumPy 矩阵与向量运算（必须肌肉记忆）
```python
import numpy as np

# 创建矩阵
A = np.array([[1,2],[3,4]])
b = np.array([5,6])

# 矩阵乘法、转置、求逆
x = np.linalg.solve(A, b)          # 解 Ax=b
eigenvalues = np.linalg.eigvals(A) # 特征值
```

**可复用函数**：添加到 `numeric_utils.py`
```python
def solve_linear(A, b):
    """解线性方程组 Ax = b，返回解向量"""
    return np.linalg.solve(A, b)

def poly_fit(x, y, degree):
    """多项式拟合，返回多项式系数（高次到低次）"""
    return np.polyfit(x, y, degree)

def numerical_integral(func, a, b, n=1000):
    """复化梯形求积"""
    x = np.linspace(a, b, n)
    y = func(x)
    return np.trapz(y, x)
```

### 3.2 SciPy 高级工具箱（优化、微分方程、插值）
```python
from scipy.optimize import minimize, curve_fit
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d, griddata

# 例子：求解常微分方程 y'= -2y, y(0)=1
def dydt(t, y):
    return -2 * y
sol = solve_ivp(dydt, [0, 5], [1], t_eval=np.linspace(0,5,100))
```

**可复用代码模板**：把这些常用调用封装成你熟悉的参数结构，但不必过度封装，因为每个问题差异大。建议你直接收集常用示例到 `sci_cheatsheet.py` 中，比赛时直接复制修改。


## 第四步：符号计算（SymPy）——为公式推导留后路

**目的**：当需要对模型进行理论推导（求导、解符号方程、化简矩阵）时，不用手算，SymPy 自动给出解析表达式，可直接粘贴进论文。

**必须掌握的四个操作**：
1. 定义符号 `x, y = sp.symbols('x y')`
2. 表达式化简 `sp.simplify(expr)`
3. 求导/积分 `sp.diff(expr, x)`，`sp.integrate(expr, x)`
4. 求解方程 `sp.solve(expr, x)`
5. 输出 LaTeX 代码 `sp.latex(expr)` 直接放到论文公式里！

**可复用脚本 `symbolic_utils.py`**：
```python
import sympy as sp

def symbolic_derivative(expr_str, var_str='x'):
    """输入字符串表达式，返回求导后的简化表达式和LaTeX"""
    x = sp.symbols(var_str)
    expr = sp.simplify(expr_str)
    deriv = sp.diff(expr, x)
    return deriv, sp.latex(deriv)

# 示例：deriv, latex_str = symbolic_derivative('x**3 * sin(x)')
# 打印 latex_str 可得到：'x^{3} \cos{\left(x \right)} + 3 x^{2} \sin{\left(x \right)}'
```

**练习**：用 SymPy 推导一个简单的优化问题（比如求目标函数梯度），并导出 LaTeX 公式，感受“一键出公式”的快乐。


## 第五步：搭建高质量绘图代码库（核心产出）

**目标**：建立一个 `plot_library.py`，包含所有常见图表的绘制函数，你只需要传入数据和标题就能生成接近出版质量的图。这样比赛中就不必反复调参数。

### 5.1 全局图片风格设定（中文字体、尺寸、分辨率）
在 `plot_library.py` 开头写入：
```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 设置中文字体（Windows用SimHei，macOS用Heiti SC）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti SC', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False  # 负号显示
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'
```

### 5.2 常用图表封装函数（只需修改数据就能复用）

#### ① 多系列折线图（用于负荷曲线、收敛过程等）
```python
def plot_lines(x, y_dict, xlabel='时间', ylabel='值', title='折线图',
               save_path=None, figsize=(10,5), linewidth=2, marker=None):
    """
    y_dict: {'系列1': y1_array, '系列2': y2_array}
    """
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
```

#### ② 散点图（用于数据分布、相关关系）
```python
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
```

#### ③ 热力图（用于相关系数矩阵、网格数据值分布）
```python
def heatmap(matrix, x_labels=None, y_labels=None, title='热力图',
            cmap='coolwarm', annot=True, fmt='.2f', save_path=None, figsize=(10,8)):
    plt.figure(figsize=figsize)
    sns.heatmap(matrix, xticklabels=x_labels, yticklabels=y_labels,
                cmap=cmap, annot=annot, fmt=fmt, linewidths=0.5)
    plt.title(title)
    if save_path:
        plt.savefig(save_path)
    plt.show()
```

#### ④ 三维曲面图（用于二变量函数、势能面、优化地形图）
```python
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
```

#### ⑤ 多子图对比图（一行多列或一列多行）
```python
def multi_plot(plot_func_list, plot_args_list, nrows=1, ncols=2,
               figsize=(14,5), save_path=None):
    """
    plot_func_list: 每个子图所用的绘图函数，要求函数接受 ax 参数
    plot_args_list: 传给对应函数的参数字典，如 {'ax': ax, 'data': ...}
    使用者需自己编写一个 helper 函数调用，这里演示一种简单实现。
    推荐更灵活的做法：自行利用 matplotlib.subplots 手动布局。
    """
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)
    axes = axes.flatten()
    for i, (func, args) in enumerate(zip(plot_func_list, plot_args_list)):
        args['ax'] = axes[i]
        func(**args)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()
```

**重要建议**：上面最后一种多子图函数通用性较差，比赛中可以**直接使用 `plt.subplots` 手写布局**，因为通常每一问组合不同。但前四种单图函数足够覆盖 80% 的需求，务必熟练调用。

### 5.3 练习：用电工杯真题数据“跑通”整个绘图库
找一道往届电工杯题目（如“负荷预测”或“光伏出力预测”），完成：
1. 读取数据（CSV 或 Excel）。
2. 用 `plot_lines` 画一天96点的负荷曲线，对比真实值和预测值。
3. 用 `heatmap` 画出各个节点电压的时空分布矩阵。
4. 用 `scatter_plot` 分析预测误差分布。
5. 用 `plot_3d_surface` 展示某个二元函数的形状（比如光伏出力随时间和辐照度的变化）。

每画一张图，调用 `save_path` 保存为 `.png`，分辨率 300dpi，这样的图直接插入论文无需再修改。


## 第六步：将所有代码组织成一个“竞赛工具包”

建议你在电脑上建立一个文件夹 `MathModel_Toolkit`，结构如下：

```
MathModel_Toolkit/
├── data_io.py            # 数据读写函数
├── numeric_utils.py      # 数值计算（线性方程组、拟合、积分）
├── symbolic_utils.py     # 符号计算快捷函数
├── plot_library.py       # 全部绘图模板
├── examples/             # 每个技能点的 Jupyter Notebook 练习
│   ├── 01_read_data.ipynb
│   ├── 02_numpy_scipy.ipynb
│   ├── 03_sympy_demo.ipynb
│   └── 04_plot_gallery.ipynb
└── competition_template.ipynb  # 比赛时直接拷贝的起手式，已导入所有模块
```
在vscode安装Jupyter插件。
**比赛起手式 `competition_template.ipynb`** 内容：
```python
# 导入全部工具箱
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import seaborn as sns
import sympy as sp

# 自建模块（放在同一目录下）
from data_io import read_data, save_data
from numeric_utils import solve_linear, poly_fit
from plot_library import *

# 设置全局风格
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")
```

这样，比赛开始后你只需要**拷贝这个模板**，然后全神贯注在建模和算法上，数据处理和绘图只是简单的函数调用。


## 第七步：限时模拟训练（关键）

**目的**：真正比赛时压力下才能熟练调用。  
**动作**：找一道电工杯小题（比如只做第一问的数据处理+可视化），设定 **2 小时**，用你的工具包完成读取、计算、绘图、保存全部流程。  
通过模拟发现工具包的不足（例如缺少某种图、读取某个 Excel 表失败），及时补充到对应的 `.py` 文件中。

---
