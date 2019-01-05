def add_qx(func):
	print("---开始进行装饰权限1的功能---")
	def call_func(*args, **kwargs):
		print("---这是权限验证1----")
		return func(*args, **kwargs)
	return call_func


def add_xx(func):
	print("---开始进行装饰xxx的功能---")
	def call_func(*args, **kwargs):
		print("---这是xxx的功能----")
		return func(*args, **kwargs)
	return call_func


@add_qx
@add_xx
def test1():
	print("------test1------")


test1()


# 1.多个装饰器，上面的先装饰，但是后执行
# 2.按照代码的顺序进行执行


"""
C:\Python372\python.exe D:/human/h18decorator/12-多个装饰器对同一个函数进行装饰.py
---开始进行装饰xxx的功能---
---开始进行装饰权限1的功能---
---这是权限验证1----
---这是xxx的功能----
------test1------

Process finished with exit code 0

"""