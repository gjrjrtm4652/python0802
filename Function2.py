# Function2.py

#지역변수와 전역변수

x= 2
def func1(a):
    return x+a
    
print(func1(1))
def func2(a):
    x = 5
    return x+a

print (func2(1))        

#불변형식 함수 내부에서 읽기+쓰기
g=1
def testScope(a):
    # global g
    g=2
    return g+a
#호출
print(testScope(1))
print("전역변수 g:" ,g)    

def times(a=10,b=20):
    return a*b

print (times())
print(times(a=5))
print(times(3,4))

#키워드 인자 (파라메터명을 명시)
def connectURI(server,port):
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURI("bitCamp","80"))
print(connectURI(port="80",server="bitCamp"))

#가변인자(다양한 갯수를 소화)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print (union ("HAM","EGG"))
print (union ("HAM","EGG","SPAM"))            