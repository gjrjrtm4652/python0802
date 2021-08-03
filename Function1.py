# Function1.py
#리턴을 하지 않는 함수
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수:",x)

#호출
result = setValue(5)
print(result)

def swap(x,y):
    return y,x

result = swap(3,4)
print (result)

def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print (intersect('HAM',"SPAM"))

a=1.2
print(id(a))
a=2.3
print(id(a))

print("====가변형식====")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

#객체는 참조를 통해 입출력이 된다.

wordlist = ["J","A","M"]

def change(x):

    x1 = x[:]
    x1[0] = "H"
    print("함수내부:" ,x1)
    #x[0] = "H"

    
change(wordlist)
print("함수 호출후:",wordlist)