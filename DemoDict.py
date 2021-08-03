# DemoDict.py

d=dict(a=1,b=2,c=3)
print(type(d))
print(d)

color = {"apple":"red","kiwi":"green"}
print(len(color))
print(color["apple"])

color["cherry"]="red"
print(color)

del color["apple"]
print(color)

color.clear()
print(color)

device = {"아이폰":10,"아이패드":15,"윈도우":20}
print(len(device))
print(type(device))
#디버깅할 때 중단점(Break Point)
for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)    

device["맥프레"] = 30
print(device)

del device["아이폰"]
print(device)

device["맥프레"] = 15
print(device)

# print(device)
