def square_digits(num):
    a = ((num % 10) **2)
    b = (((int(num/10)) % 10) **2)
    c = (((int(num/100)) % 10) **2)
    d = (((int(num/1000)) % 10) **2)

    z = int(str(a)+str(b)+str(c)+str(d))
    print(z)

num = 9119

square_digits(9119)