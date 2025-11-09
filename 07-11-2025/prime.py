isprime = True
num=int(input("enter a number : -"))
if num==1:
  # print("1 is not a prime number")
  isprime = False
else:
  for i in range (2,num ):
    if num % i ==0:
      isprime = False
      break

if isprime == True: 
  print("Number is prime")
else:
  print("not prime")