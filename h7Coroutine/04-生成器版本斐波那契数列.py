

def create_num(all_num):
    # a=0
    # b=0
    a,b = 0,1
    current_num = 0
    while current_num < all_num:
        #print(a)
        yield a  # 如果一个函数中有yield ,那么此时就不是这个函数，而是一个生成器模版
        a, b = b, a+b
        current_num += 1

# 如果是在调用create_num 的时候，发现这个函数中有yield 那么此时，不适调用函数，而是创建一个生成器对象
obj = create_num(10)
# ret = next(obj)
# print(ret)
#
# ret=next(obj)
# print(ret)

a=0
while a<10:
    ret = next(obj)
    print(ret)
    a+=1