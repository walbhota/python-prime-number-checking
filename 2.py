num = int(input("This number: "))
for i in range(2, num):
    if num % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")
