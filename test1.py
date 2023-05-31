#第一部分 基础知识

#第一个Python程序
print("hello, world!")
#我是注释
"""我也是注释哈哈哈哈
hhhhhh
"""
#数据类型
a=666
b=66.6
c="hhhhhhhh"

#格式化输出
print(type(a),type(b),type(c))
print("a为%d,b为%f,c为%s"%(a,b,c))
print(f"a为{a},b为{b},c为{c}")
print(f"a为{a}\nb为{b}\nc为{c}")
print(f"a为{a}\tb为{b}\tc为{c}")
#\n表示换行，\t表示一个tab键的间距

#输入
password=input("请输入")
print(f"您输入的密码为{password}")

#运算符
a1=10
a2=2
a3=3
print(a1**a3)#取a1的a3次幂
print(a1%a3)#取余
print(a1//a3)#取整