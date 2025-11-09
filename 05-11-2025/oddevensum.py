i=1
evensum=0
oddsum=0
while i<=100:
  if i%2 == 0:
    evensum=evensum+i
  else: 
    oddsum=oddsum+i
  i=i+1    
print( oddsum)    