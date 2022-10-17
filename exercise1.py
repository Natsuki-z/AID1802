# 开发时间： 2022/8/14 18:02
a = 'A'
b = 'B'
a = b
print(a)

a, b = input('输入第一个变量'), input('输入第二个变量')
# 所有语言通用
# i=a
# a=b
# b=i
# 适合python的
a, b = b, a
print(a, b)
