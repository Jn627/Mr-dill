monday =float(input('temperature for monday'))
tuesday =float(input('gimmie temperature for tuesday'))
wednesday =float(input('gimmie temp for wednesday'))
thursday =float(input('gimmie temp for thursday'))
friday =float(input('gimmie temp for friday'))
saturday =float(input('gimmie temp for saturday'))
sunday =float(input('gimmie temp for sunday'))
average_temp =monday+tuesday+wednesday+thursday+friday+saturday+sunday/7
print(average_temp)
x = float(input('gimmie a value for x'))
y = float(input('gimmie a value for y'))
z = float(input('gimmie a value for z'))
PIE = 3.14
ans = 4*x**4+3*y**3+9*z+PIE
print(ans)

time = int(input('enter a hour 1-12'))
ahead = int(input('how many hours ahead would you like to know'))
ans = time+ahead%12
print(ans)

forwards = int(input('enter three numbers'))
b = forwards//10
a = b%10
bob = b//10
car = bob%10
floor = car//10
fom = floor%10
print(a,car,fom,sep='')