try:
    a=int(input("enter the first number"))
    b=int(input("enter the second"))
    c=int(input("enter the third number"))
    print("a=",a,"b=",b, "c=",c)
    print(a, b, c, sep=".......")
    if a>b:
        if a>c:
            print("A is greatest")
        else:
            print("C is greatest")
    elif b>c:
        print("B is greatest ")
    else:
        print("C is greatest")
except exception as e:
    print("please enter integer numer",e)