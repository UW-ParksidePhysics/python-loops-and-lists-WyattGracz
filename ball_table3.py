n = 5
g = 9.81
v0 = 10
t_final = int(((2*v0)/g)+1)
dt = t_final/n
#for t in range (0, t_final):
  #y = (v0*t)-(.5*g*t*t)
  #print(y)

t = [i*dt for i in range(0,n)]

y = [v0*t[i]-(.5*g*t[i]**2) for i in range(0,n)]

ty1 = 
