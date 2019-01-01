class Feibonaqie(object):
    def __init__(self,all_num):
        self.all_num=all_num
        self.current_num=0
        self.a=0
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a

            self.a,self.b=self.b,self.a+self.b
            self.current_num +=1
            return ret
        else:
            raise StopIteration

feibo = Feibonaqie(10)

for num in feibo:
    print(num)

# 运行结果
#
# C:\Python372\python.exe D:/human/h7Coroutine/03-斐波那契数列.py
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
#
# Process finished with exit code 0

#
# 并不是只有for循环能接收可迭代对象
# 除了for循环能接收可迭代对象，list、tuple等也能接收。

li = list(Feibonaqie(15))
print(li)
tp = tuple(Feibonaqie(6))
print(tp)