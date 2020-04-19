#Program to calculate the symmetric difference
n1 = int(input())
set_1 = set(map(int,input().split()))
n2 = int(input())
set_2 = set(map(int,input().split()))
print(len(set_1.symmetric_difference(set_2)))
#lst = [x**2 for x in range(0,12)]
#print(lst)
#lst = [number for number in range(11) if number % 2 == 0]
#print(lst)
#lst = [x**2 for x in [x**2 for x in range(11)] ] #prints x**4
#print(lst)
