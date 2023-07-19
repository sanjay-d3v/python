try:
    file = open("excep.py")
    age = int(input('age: '))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("you didnt enter valid age")
else:
    print("no exceptions were thrown")
finally:
    file.close()
print("execution continues")
