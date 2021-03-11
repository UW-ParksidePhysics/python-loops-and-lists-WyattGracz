import math
g = 9.81
v0 = 10
t_final = int(((2*v0)/g)+1)
t = 5

for t in range (0, t_final):
  y = (v0*t)-(.5*g*t*t)
  print(y)


while t < (t_final):
  y = (v0*t)-(.5*g*t**2)
  print(y)
  t += 1
