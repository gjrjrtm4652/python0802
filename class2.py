# class2.py

class Person:
    num_person = 0
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
    def print(self):
        print ("My name is {0}".format(self.name))

p1 = Person()
p2 = Person()
p3 = Person()
print("인스턴스 갯수:{0}".format(Person.num_person))  

#동적으로 확장이 된다
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

#인스턴스에 추가
p1.age = 30
print(p1.age)
# print(p2.age)
