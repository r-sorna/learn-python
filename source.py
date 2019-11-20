print("bike=10,car=20,auto=5")
catagory=input("bike/car/auto: ")
username=input("name: ")
mail=input("mailid: ")
phone=input("phone: ")
source=input("source: ")
destination=input("destination: ")
bprice=10
cprice=20
aprice=5
km=source-destination
if "-"in source and destination:
    print("please enter valid details: ")
elif source==0 or destination==0:
    print("please enter valid details")     
elif catagory=="bike":
    total=km*bprice
    print(total)
elif catagory=="car":
    total1=km*cprice  
    print(total1)
else:
    total2=km*aprice
    print(total2)      
