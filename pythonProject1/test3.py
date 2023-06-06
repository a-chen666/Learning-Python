# 字符串切片知识点
# 即print(name[第一位:最后一位:步长])
name="abcdef"
print(name[1:3])
print(name[1:-1])
print(name[-1:1:-1])

# 字符串常用操作
my_str="hello! my friend!!!"
"""find返回字符串所在位置，rfind表示从右往左数
my_str.find(str, start=0, end=len(mystr))"""
print(my_str.find("my"))
print(my_str.rfind("my"))


# count返回字符串出现次数
# my_str.count(str, start=0, end=len(mystr))
print(my_str.count("my"))
print(my_str.count("my",0,len(my_str)))


# replace替换字符串内容 my_str.replace(str1, str2,  mystr.count(str1))
print(my_str.replace("hello","good",my_str.count("hello")))
print(my_str)

# split 以 str 为分隔符切片 my_str，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
# my_str.split(str=" ", maxsplit)
print(my_str.split( ))

# startswith 检查字符串是否是以 hello 开头, 是则返回 True，否则返回 False
# my_str.startswith(hello)
print(my_str.startswith("hello"))

"""等等等等"""

#region 列表内容

# 列表
# 可以存储不同类型的数字，读取时，可按照字符串的切片操作
my_ins=['阿琛',23,"chenchen"]
stu_names=["yihao","erhao","sanhao"]
print(stu_names[0])
print(stu_names[0:2])
# 用for循环遍历
for name in stu_names:
    print(name)

# 用while遍历
print("while 遍历")
i=0
while i<len(stu_names):
    print(stu_names[i])
    i+=1

# 列表的常用方法
#region 增

# 通过append可以向列表添加元素
# 列表.append(新元素数据)
stu_names.append("sihao")
print(stu_names[3])

# 通过extend可以将另一个列表中的元素逐一添加到列表中
# 列表.extend(另外一个列表)
print("extend展示------------")
add_list=[1,2,3]
stu_names.extend(add_list)
for name in stu_names:
    print(name)

# insert(index, object) 在指定位置index（索引，理解为下标即可）前插入元素object
stu_names.insert(1,add_list)
for name in stu_names:
    print(name)
#endregion


#region 删
# del根据下标删除
del stu_names[1]
for name in stu_names:
    print(name)

# pop删除最后一个元素
stu_names.pop()
for name in stu_names:
    print(name)

# remove删除指定值的数据
stu_names.remove(2)
for name in stu_names:
    print(name)
#endregion


#region 改
stu_names[0]="Yihao"
for name in stu_names:
    print(name)
#endregion

#region 查
"""in（存在）,如果存在那么结果为true，否则为false
not in（不存在），如果不存在那么结果为true，否则false
数据 in 列表
数据 not in 列表"""
print(1 in stu_names)

print(stu_names.count(1))
#endregion

#endregion

#region 元组内容
# 元组的元素不能修改
# 元组使用小括号()，列表使用方括号[]
print("元组-----------")
nums=(1,2,3,4)
print(nums[0])
for a in nums:
    print(a)
#endregion

#region 集合内容
"""集合中数据不能重复
列表可以存储多个数据，支持增删改查
元组可以存储多个数据，不能修改
集合依然可以存储多个数据，数据不能重复"""
# 定义集合
print("集合---------")
nums1={1,2,3,4}
nums2={1,2,2,3,4}
for a in nums1:
    print(a)
print("nums2为--------------")
for a in nums2:
    print(a)
#endregion

#region 列表、元组、集合相互转换
# 转换为列表用 list()
# 元组为 tuple()
# 集合为 set()
num1=(1,2,2,3)
num1_set=set(num1)
print(num1_set)

#endregion

#region 字典
# 字典格式{key: value, key2: value ...}
person_ins={"name":"张三", "age" :23, "height":167}
# 访问value
print(person_ins["name"])

#region 遍历字典
# 遍历key
for key in person_ins.keys():
    print(key)

#region 遍历value
for value in person_ins.values():
    print(value)
#endregion

#region 遍历元素
for temp in person_ins.items():
    print(temp)
#endregion


#endregion

#region 字典常用操作

#region 增
person_ins["money"]=666
#endregion

#region 删
del person_ins["money"]
#endregion

#region 改
person_ins["name"]="李四"
#endregion

#region 查
print(person_ins["name"])
# get可以查有无这个key,并返回值或布尔值
print(person_ins.get("weight","无"))
#endregion

#endregion

#endregion

#region 推导式
#region 列表推导式
# [变量 for 变量 in 可迭代对象]
list1=[x for x in range(1,21) if x%2==0]
print(list1)
list2=[(x,y,z) for x in range(1,4) for y in range(1,4) for z in range(1,4)]
print(list2)
#endregion

#region 集合推导式
set1={x for x in range(1,20) if x%2==0}
print(set1)
#endregion

#region 字典推导式
# 快速生成一个1~10内key可以1时value为2，key为2时value3....依次类推的字典
a={x:(x+1) for x in range(1,5)}
print(a)

#endregion

#endregion

