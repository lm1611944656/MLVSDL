创建一个包文件夹config，编辑器会一并创建一个如下的文件：
```angular2html
config
    __init__.py			# 用于解析yaml文件(在此处的作用)
    configdata.yaml		# 存储用户的配置信息
core
	__init__.py			# 不要任何作用
	basecase.py			# 使用用户的配置信息

test.
```
当工程师在basecase.py使用配置信息时，直接导入config文件夹，在导入文件夹时，系统就会自动加载config下的\__init__.py	

