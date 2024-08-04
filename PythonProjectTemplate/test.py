from core.basecase import BaseCase      # 从模块中导入类名


if __name__ == '__main__':
    base_case_instance = BaseCase()  # 创建 BaseCase 类的实例

    username = base_case_instance.get_user_ID()  # 获取 username
    print(f"Username from config: {username}")

    host_info = base_case_instance.get_host_url()  # 获取主机信息
    print(f"Host info from config: {host_info}")
