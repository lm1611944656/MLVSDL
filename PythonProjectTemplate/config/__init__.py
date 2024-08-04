import yaml
import os


def load_config():
    # 打开yaml文件
    config_file_data = os.path.join(os.path.dirname(__file__), 'configdata.yaml')
    with open(config_file_data, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config

config2 = load_config()
