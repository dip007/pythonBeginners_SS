x,y,z,n = (int(input()) for i in range(4))
print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c!=n])

#Input and output: This prints the details in lexicographic order.
# 1
# 1
# 1
# 2
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# x=int(input())
# y=int(input())
# z=int(input())
# n=int(input())
# p=0
# ar=[]
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if (i+j+k)!=n:
#                 ar.append([])
#                 ar[p]=[i,j,k]
#                 p=p+1
#                 print (ar,end='')