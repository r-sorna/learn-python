choice=input("add/sub/mul/div:")
a=input()
b=input()
if "."in a and b:
    c=float(a)
    d=float(b)
    print(c,d)
elif a.isalpha() and b.isalpha():
    print("please enter only numbers")
else:
    c=int(a)
    d=int(b)    
print(choice)
if choice=="add":
    print(c+d)
elif choice=="sub":
    print(c-d)         
elif choice=="mul":
    print(c*d)
else:
    print(c/d)    
