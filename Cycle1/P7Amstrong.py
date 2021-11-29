print("Armstrong Numbers:")
for n in range(1,1000):
  temp=n
  sum=0
  while temp>0:
      a=temp%10
      sum=sum+a**3
      temp=temp//10
  if sum==n:
           print (n)





