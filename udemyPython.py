#Use for, split(), and if to create a Statement that will print out words that start with 's':
# st = 'Print only the words that start with s in this sentence'
# for s in st.split():
#     if s[0] == 's':
#         print(s)
#Use range() to print all the even numbers from 0 to 10.
# for i in range(11):
#     if i % 2 ==0:
#         print(i)
#Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
# lst=[number for number in range(0,51) if number % 3 == 0]
#  print(lst)
# st = 'Print every word in this sentence that has an even number of letters'
# for s in st.split():
#     if len(s)%2==0:
#         print (s)
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
#  and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# for i in range(1,101):
#     if (i%3==0 and i%5==0):
#         print("FizzBuzz")
#     elif (i%3==0):
#         print("Fizz")
#     elif (i%5==0):
#         print("Buzz")
#     else:
#         print(i)
#Use List Comprehension to create a list of the first letters of every word in the string below:
# st = 'Create a list of the first letters of every word in this string'
# l = [word[0] for word in st.split()]
# print(l)
# def add_num(num1,num2):
#     return num1 + num2
# print(add_num(3,5))
def is_prime(num):
    for n in range(2,num+1):
        if num % n == 0:
            print('Hey there it is not a prime number and returned from the is_prime function',n)
        break
    else:
        print('It is a prime number and is returned from the function',n)

print(is_prime(4))
# import math
# n=15
# for i in range(3,int(math.sqrt(n)+1,2)):
#     print(n)


