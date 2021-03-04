a = 2
b = 4
n = 8

h = (b-a)/n
List=[]
for i in range (n+1):
  List.append(a+i*h)
print(List)
compList = [a + i*h for i in range (n+1)]
print(compList)