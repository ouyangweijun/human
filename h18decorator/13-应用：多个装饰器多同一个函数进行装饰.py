def set_func_1(func):
	def call_func():
		# "<h1>haha</h1>"
		return "<h1>" + func() + "</h1>"
	return call_func

def set_func_2(func):
	def call_func():
		return "<td>" + func() + "</td>"
	return call_func


@set_func_1
@set_func_2
def get_str():
	return "haha"

print(get_str())

"""
C:\Python372\python.exe D:/human/h18decorator/13-应用：多个装饰器多同一个函数进行装饰.py
<h1><td>haha</td></h1>

Process finished with exit code 0

"""