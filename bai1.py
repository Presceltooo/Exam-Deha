import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập số nguyên dương n: "))
if is_prime(n):
    print(n," là số nguyên tố.")
else:
    print(n," không phải là số nguyên tố.")

