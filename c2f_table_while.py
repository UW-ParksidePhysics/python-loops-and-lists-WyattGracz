F = 0                        # start value for C
dF = 10                         # increment of C in loop
print("Farenheit vs Celsius")     # table heading

while F <= 100:                 # loop heading with condition
    C = (F-32)/1.8         # 1st statement inside loop
    print(F, C)                 # 2nd statement inside loop
    F = F + dF                 # 3rd statement inside loop
