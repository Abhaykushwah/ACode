import random
import time
length = int(input("Enter the length of your Password ="))
x = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890':;!?*/)(#@$][}{\%")
password= (" ")
for i in range(length):
	password+=random.choice(x)
print ("Please wait a second Your password in genrating.....")
time.sleep(1)

print("-"*55)
print ("Your password is :" +password)
print("-"*55)
