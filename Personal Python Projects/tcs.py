def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

m1,n1 = input().split()
m = int(m1)
n = int(n1)
num1 = 0
num2 = 0
counter = 0
for i in range(m,n+1):
    if(isPrime(i)):
        num1 = i
        for j in range(i+1,n+1):
            if(isPrime(j)):
                num2 = j
                if((num2-num1)==6):
                    counter = counter+1
print(counter)