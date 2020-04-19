# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
# Input Format
# The first line contains . The second line contains an array   of  integers each separated by a space.
# Print the runner-up score.
# n = int(input())
# arr=list(map(int,input().split()))
# large=max(arr)
# print(large)
# print(arr)
# a=0
# n, a = int(input()), list(set([int(x) for x in input().split()]))
# print (sorted(a)[len(a)-1])
n=int(input())
a=list(set(int(x) for x in input().split()))
large = max(a)
# print(large)
# print(a)
# b=len(a)
# print(b)
for i in range(len(a)+1):
    if large == max(a):
        a.remove(max(a))
print(max(a))








