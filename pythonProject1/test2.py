#第二部分，判断语句与循环语句
"""
与 and 或 or 非 not
"""
a=10
if a>5 and a<15:
    print("T")
else:
    print("F")


"""
要求：从键盘输入身高，如果身高没有超过150cm，则进动物园不用买票，否则需要买票。

提示：input获取的数据不是整数类型，需要用int()转换，例如int("100")结果就是整数100
"""
tall1 = int(input("请输入身高"))
if tall1<=150 :
    print("不用买票")
else :
    print("买票！")


"""
90以上为优秀，80以上为好，70以上为良，其余不及格
"""
score=89
if score>90 :
    print("优秀")
elif score>80:
    print("好")
elif score>70:
    print("良")
else :
    print("不及格")


"""
要求：使用while循环编写代码试如下效果
1--->1
2--->4
3--->9
"""
i=1
while i<4:
    print(f"{i}--->{i**2}")
    i+=1


"""
（九九乘法表）
"""
i=1
j=1
while i<10:
    j=1
    while j<=i:
        print(f"{j}*{i}={i*j}\t",end="")
        j+=1
    print()
    i+=1


"""
while  else的用法
当while循环体中没有使用break，则执行else的内容
"""
i=1
while i<5:
    if i ==6 :
        print("有break")
        break
    i+=1
else :
    print("没有break")

"""
for循环以及range(x,y),范围是前闭后开
"""
for i in range(30,35):
    print(i)




"""
for循环与else 
"""
for i in range(30,35):
    if i==35:
        print("有break")
        break
    i+=1
else :
    print("没有break")
