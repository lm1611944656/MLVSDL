from config import config2      # 从config模块导入config2变量
from config import load_config  # 从config模块导入函数

class BaseCase:
    def __init__(self):

        # 使用其他模块的函数
        self.config = load_config()
        print("用户配置信息：", self.config)

        # 使用config2变量，打印配置文件中的 "password" 键对应的值
        print(config2["weixin"]["password"])

    def get_user_ID(self):
        # 返回配置文件中的 "username" 键对应的值
        return config2["weixin"]["ID"]

    def get_host_url(self):
        # 返回配置文件中的 "host" 和 "port" 信息
        return config2["weixin"]["setting"]["url"]
