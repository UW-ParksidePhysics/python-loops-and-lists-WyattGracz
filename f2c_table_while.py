F = 0                        # start value for C
dF = 10                         # increment of C in loop
print("Farenheit vs Celsius")     # table heading

while F <= 100:                 # loop heading with condition
    C = (F-32)/1.8        
    print(F, C)                 
    F = F + dF    