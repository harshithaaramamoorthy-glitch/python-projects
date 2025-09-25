while True:
    print("welcome to atm:")
    print("enter your password:")
    a=int(input("enter your password"))
    if(a==6789):
        print("proceed transaction:")
    else:
        a=int(input("password is invalid"))
        print("re-enter your password:")
        break
        