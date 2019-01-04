from collections import Iterable
from collections import Iterator
# print(isinstance(100,Iterable))
# print(isinstance("abx",Iterable))
#
# # for i in range(10):
# #     print(i)

class Classmate(object):

    def __init__(self):
        self.names=list()
    def add(self,name):
        self.names.append(name)
    def __iter__(self):
        """如果想让一个对象称为一个 可迭代的对象，即可以使用for ，那么必须实现 __iter__方法"""
        return ClassIterator()

class ClassIterator(object):

    def __iter__(self):
        pass
    def __next__(self):
        return 11
classmate = Classmate()
classmate.add('王哥')

print("判断classmate是否是可迭代的对象：",isinstance(classmate,Iterable))
classmate_iterator = iter(classmate)

print("判断classmate是否是迭代器：",isinstance(classmate_iterator,Iterator))

iter(classmate)

for name in classmate:
    print(name)