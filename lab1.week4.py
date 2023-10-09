a=input("enter the string:")
b=a.replace(" ","")
print(b)

x=input("enter the string")
b=(x[::-1])
if x==b:
    print("palindrome")
else:
    print("not palindrome")