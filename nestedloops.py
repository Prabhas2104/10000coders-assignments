# n = 10
# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i} x {j} = {i*j}')
#     print()


# mat = [[1,2,3],[4,5,6],[7,8,9]]
# res = []
# for i in range(len(mat)):
#     summ=0
#     for j in range(len(mat)):
#         summ=summ+mat[i][j]
#     res.append(summ)
# print(res)


# n = int(input())  #integer
# s= input()   #string
# a,b,c,d,e,f= map(int,input().split())
# l=list(map(int,input().split()))  #list type of input


# l = []
# n=3
# for i in range(n):
#     l1=list(map(int,(input("enter row").split())))
#     l.append(l1)
# print(l)


# for i in range(4):
#     for j in range(4):
#         print("*", end=" ")
#     print()



# for i in range(1, 5):         
#     for j in range(i):         
#         print("*", end=" ")
#     print()
 

# def isprime(n):
#     if n<2: return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# n=11
# print(isprime(n))


# def isprime(n):
#     if n<2: return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# n=9
# if isprime(n):
#     print(n)
# else:
#     left=n-1
#     right=n-1
#     while True:
#         if isprime(left):
#             print(left)
#             break
#         if isprime(right):
#             print(right)
#             break
#         left=1
#         right+=1

# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()


# for i in range(4):
#     for j in range(1):
#         print("1 2 3 4 5", end=" ")
#     print()

# n=5
# for i in range(n):        
#     for _ in range(i,n-1):         
#         print(" ", end=" ")
#     for _ in range(i+1):              
#         print("*",end=" ")
#     print()

# n=5
# for i in range(n):
#     for _ in range(i+1):              
#         print(" ",end=" ")        
#     for _ in range(i,n):         
#         print("*", end=" ")
#     print()

# n = 5
# for i in range(n):
#     for _ in range(n - i - 1):
#         print(" ", end=" ")
#     for _ in range(i + 1):
#         print("*", end=" ")
#     print()

n = 5
for i in range(n):
    for _ in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n - 2, -1, -1):
    for _ in range(i + 1):
        print("*", end=" ")
    print()


# n = 5
# for i in range(n):
#     for _ in range(n - i - 1):
#         print(" ", end=" ")
#     for _ in range(i + 1):
#         print("*", end=" ")
#     print()
# for i in range(n - 2, -1, -1):
#     for _ in range(n - i - 1):
#         print(" ", end=" ")
#     for _ in range(i + 1):
#         print("*", end=" ")
#     print()

