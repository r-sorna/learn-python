i=int(input("givr your starting range: "))
j=int(input("give your end range:"))
for k in range(i,j):
  print("even")
  if (k%2)==0:
    print(k)
    
  else:
    print("")  
print("odd")
for m in range(i,j):
  if (m%2)!=0:
    print(m)
  else:
    print("")       