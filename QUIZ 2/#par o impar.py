#par o impar
N=int(input(""))
for i in range (1,N+1):
    X=int(input(""))
    if(X %2 ==0 and X > 0):
        print(f"EVEN POSITIVE {X}")
    elif(X %2==0 and X < 0):
        print(f"EVEN NEGATIVE {X}")
    elif(X %2 ==1 and X>0):
        print(f"ODD POSITIVE {X}")
    elif(X %2 ==1 and X<0):
        print(f"ODD NEGATIVE {X}")
    elif(X == 0):
        print("NULL")
    