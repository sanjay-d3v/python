try:
    numbers = input("number : ")
    raise ("number cant be zero")
    print(numbers % 0)
    raise ZeroDivisionError("cannot be divided by zero")
except:
    print("zerodivisionerror")
else:
    print("no error in code")
finally:
    print("good to go")
