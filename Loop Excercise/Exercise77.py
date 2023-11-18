n=int(input())
b=1
sum=0
while n!=0: 
    l = n % 10; 
    n = int(n/ 10);         
    sum += l * b; 
    b = b * 2
print(sum)