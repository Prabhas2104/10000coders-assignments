# ip=12521
# ip1=ip
# # op=874521
# rev=0
# while(ip>0):
#     ld=ip%10
#     rev=rev*10+ld
#     ip=ip//10
# print(rev)

# if(ip1==rev):
#     print("given num is palindrome")
# else:
#     print("given num is not a palindrome")
    
# ip=12521
# d=0
# while(ip>0):
#     s=ip%10
#     d=d+s
#     ip=ip//10
# print(d)

# ip=12521
# count=0
# while(ip>0):
#     count+=1
#     ip=ip//10
# print(count)

# ip=12589
# sum=0
# while ip>0:
#     d=ip%10
#     if d%2==0:
#         sum=sum+d
#     ip=ip//10
# print(sum)

# ip=12589
# count=0
# while ip>0:
#     d=ip%10
#     if d%2 !=0:
#         count=count+1
#     ip=ip//10
# print(count)        


num = int(input("Enter a number: "))
# Count digits
n = len(str(num))
# Calculate sum of powers
total = 0
for digit in str(num):
    total += int(digit) ** n
# Check and print result
if num == total:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")

