class Person:
    pass


p = Person()
# 增加对象属性,和当前类并没有关系，自己当前对象新增了一个属性，指向内存某个区域
p.name = "cindy"
p.age = 15

print(p.name, p.age)
print(p.__dict__)
# 修改引用
p.age = 123
print(p.name, p.age)
# 修改引用对象
p.pets = ["小花", "小黑"]
print(p.pets, id(p.pets))

p.pets.append("小三")
print(p.pets, id(p.pets))

# 删除对象
# del p.age  
del p.__dict__
print(p.age)
print(p.__dict__)

