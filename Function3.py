# Function3.py
#정의되지 않은 인자 처리(사전식)
def userURIBuilder(server,port,**user):
    strURL = "http://" + server +":"+port +"/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

print(userURIBuilder("Bit camp","80", id="kim",passwd="1234"))    
print(userURIBuilder("Bit camp","80", id="kim",passwd="1234",name="mike",age="30"))    

g=lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())

#제너레이터(값을 생성해서 추출하고 마지막에 리턴)
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]
#호출        
for char in reverse("gold"):
    print(char)

#단순한 예제
def abc():
    s = "abc"
    for char in s:
        #값을 생성하고 추출하고 마지막에 반환
        yield char
#호출
for char in abc():
    print(char)

print(help(abc))