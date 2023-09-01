sec=int(input("enter seconds"))
if sec>59:
    print("mins=",int(sec/60),"hrs=",int(sec/3600),"second=",int(sec%60))
else:
    print(int(sec))

