import pandas as pd

def read_data(file_path, **kwargs):
    """
    自动读取 CSV / Excel 文件
    使用方法：
    df = read_data("数据.xlsx", encoding="gbk", skiprows=1)
    """
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path, **kwargs)

    elif file_path.endswith((".xls", ".xlsx")):
        return pd.read_excel(file_path, **kwargs)

    else:
        raise ValueError("只支持 CSV、xls、xlsx 格式")


def save_data(df, file_path, index=False, **kwargs):
    """
    自动保存 DataFrame 到 CSV / Excel
    """
    if file_path.endswith(".csv"):
        df.to_csv(file_path, index=index, **kwargs)

    elif file_path.endswith((".xls", ".xlsx")):
        df.to_excel(file_path, index=index, **kwargs)

    else:
        raise ValueError("只支持保存为 CSV、xls、xlsx 格式")