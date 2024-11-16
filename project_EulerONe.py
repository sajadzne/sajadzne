def Zarib3or5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else:
        return False
    

count = 0

for i in range(1,1000):
    if Zarib3or5(i):
        count = count + i

print(count)
