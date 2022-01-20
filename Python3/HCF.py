def hcf(a, b):
    if (b == 0):
        return a
    else :
        return hcf(b, a % b)

a = int(input("Enter the first value : "))
b = int(input("Enter the second value : "))

print(hcf(a,b))
