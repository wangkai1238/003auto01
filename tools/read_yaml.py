import os
import yaml
from config import BASE_PATH


def read_yaml(filename):
    filepath = BASE_PATH + os.sep + "data" + os.sep + filename
    # 定义空列表 存储读取到的数据
    arr = []
    # 读取yaml文件数据
    with open(filepath, "r", encoding="utf-8") as f:
        # 遍历
        for datas in yaml.safe_load(f).values():
            # 序列化为元祖 添加到列表中
            arr.append(tuple(datas.values()))
    # 返回数据列表
    return arr


if __name__ == '__main__':
    # *.yaml文件里一定要注意 格式，:冒号后要有空格
    print(read_yaml("lp_login.yaml"))
