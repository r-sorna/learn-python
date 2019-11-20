username=input("name: ")
mail=input("mailid: ")
phone=input("phone: ")
catagory=input("bike/car/auto: ")
source=input("source: ")
destination=input("destination: ")
bprice=10
cprice=20
aprice=5
km=0
if "-"in source or destination:
    print("please enter valid details: ")
elif source==0 and destination==0:
    print("please enter valid details") 
elif source.isalpha() and destination.isalpha():
    print("please enter valid details") 
elif source>destination:
    source1=int(source)
    dest=int(destination)
    km=destination-source
else:
    source1=int(source)
    dest=int(destination) 
    km=source-destination   
print("calculation")           
if catagory=="bike":
    total=km*bprice
    print(total)
elif catagory=="car":
    total1=km*cprice  
    print(total1)
else:
    total2=km*aprice
    print(total2)      
