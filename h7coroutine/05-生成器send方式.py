def create_num(all_num):
    a,b = 0,1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print('<<<<ret<<<<',ret)
        a,b = b,a+b

        current_num += 1

obj = create_num(10)
# obj.send(None)  # send 一般不会放在第一次启动生成器，如果是一定要，那么传递None
ret = next(obj)
print(ret)

# send 里面的数据会传递给下一次第六行，单做yield a 的结果，然后ret 保存这个结果
# send 的结果是下一次调用yield时，yield 后面的值

ret = obj.send("哈哈")
print(ret)

ret = obj.send("哈哈")
print(ret)
ret = obj.send("哈哈")
print(ret)
ret = obj.send("哈哈")
print(ret)
ret = obj.send(8)
print(ret)
ret = obj.send(8)
print(ret)