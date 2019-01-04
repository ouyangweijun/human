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
        self.current_num=0
    def add(self,name):
        self.names.append(name)
    def __iter__(self):
        """如果想让一个对象称为一个 可迭代的对象，即可以使用for ，那么必须实现 __iter__方法"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret=self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration

classmate = Classmate()
classmate.add('王哥0')
classmate.add('王哥1')
classmate.add('王哥2')

# print("判断classmate是否是可迭代的对象：",isinstance(classmate,Iterable))
# classmate_iterator = iter(classmate)
#
# print("判断classmate是否是迭代器：",isinstance(classmate_iterator,Iterator))
#
# iter(classmate)

for name in classmate:
    print(name)