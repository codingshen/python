# !user/bin/python3
# try...except...finally...语句

# 异常处理

#实例1
try:
    a = 10
    for i in range(11):
        print(2/a)
        a -= 1           # 非常明显的错误:发现除到最后引发ZeroDivisionError.
except ZeroDivisionError:
    print('除数为0是错误的')
finally:
    print('下次不可以犯这样的错误')

#语法总结:
'''
try: 
    有可能会出现错误的代码(你不确定)
except 错误名称:
    如果说except发现出现了except后面跟的错误，那么就执行except语句(之后执行finally)
    如果没有被捕捉到，那就继续程序。
finally:
    捕捉到错误，结尾。
'''