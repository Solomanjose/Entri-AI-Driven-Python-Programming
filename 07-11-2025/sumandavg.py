sum=0
avg=0
n=int(input("eneter n numbers:-"))
for i in range (0,n,1):
  num=int(input("enter "n," numbers"))
  sum=sum+num
  # avg=sum/n
print(sum)
print('avg',sum/n)