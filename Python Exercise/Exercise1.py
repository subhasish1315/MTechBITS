
# 1. Write a Python function to find the factorial of a number using recursion.
# Description: The factorial of a number n is the product of all positive integers less than
# or equal to n.
# Example Input: 5
# Example Output: 120


def factorial(n):
    if n == 1 :
        return n
    else:
        return n * factorial(n-1)

def find_factorial(n):
    if n < 0:
        print("Factorial Cannot be Done with Negative Number")
    elif n == 0:
        print("Factorial of 0 is 1")
    else:
        print("Factorial of ",n ," is ",factorial(n))

number = 5
find_factorial(n = 5)
 

# 2. Given two lists, write a Python function to find the intersection (common elements) of the
# lists.
# Description: The function should return a list of elements that appear in both input lists.
# Example Input: [1, 2, 3, 4] and [3, 4, 5, 6]
# Example Output: [3, 4]


def find_common(l1,l2):
    common_item = list(set(l1) & set(l2))
    print("List1 - ",l1, " List2 - ",l2," Common Item - ",common_item)

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]

find_common(l1 = l1,l2 =l2)



# 3. Write a Python program to count the frequency of each element in a list.
# o Description: Given a list of elements, return a dictionary where the keys are elements
# and the values are their frequencies.
# o Example Input: [1, 2, 2, 3, 3, 3, 4]
# o Example Output: {1: 1, 2: 2, 3: 3, 4: 1}

from collections import Counter

inputlist = [1, 2, 2, 3, 3, 3, 4]
print("Count of the List ",inputlist," Item Count ",dict(Counter(inputlist)))



# 4. Write a Python program to remove duplicates from a list while preserving the original
# order.
# o Description: Given a list, return a new list with all duplicate elements removed, keeping
# only the first occurrence of each element.
# o Example Input: [1, 2, 2, 3, 4, 3]
# o Example Output: [1, 2, 3, 4]


def rmv_dup_org_order(lst):
    res_set = set()

    for i in lst:
        if i not in res_set:
            res_set.add(i)
    
    print("Input List - ",lst)
    print("Output List - ",list(res_set))

ilist = [1, 2, 2, 3, 4, 3]
rmv_dup_org_order(lst =ilist)


# 5. Write a Python function to calculate nCr (binomial coefficient) using the formula
# nCr=n!r!(n−r)!nCr = \frac{n!}{r!(n-r)!}nCr=r!(n−r)!n!.
# Description: Given integers n and r, calculate the value of nCr.
# Example Input: n = 5, r = 3
# Example Output: 10

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = 5
r = 3
print(nCr(n, r))





# 6. Write a Python function that takes a string as input and returns the string reversed.
# Example Input: "hello"
# Example Output: "olleh"

st = "hello"
print("Inpite String = ",st, " Reversed Output = ",st[::-1])



# 7. Write a Python program to check if a given year is a leap year or not.
# Description: A year is a leap year if it is divisible by 4, except for years that are divisible by
# 100, unless they are also divisible by 400.
# Example Input: 2020
# Example Output: True

def check_leap_year(yr):
    if yr % 4 == 0:
        return True
    else:
        return False

year = 2001
print(check_leap_year(yr = year))


# 8. Write a Python function to count the number of vowels in a given string.
# Example Input: "hello world"
# Example Output: 3


def count_vowel(st):
    count = 0
    for i in st:
        if i.lower() in ['a','e','i','o','u']:
            count = count+1
    print("Total No of Vowels ", count)


st = "hello world"
count_vowel(st =st)


# 9. Write a Python function that takes a list of integers and returns a tuple containing the
# maximum and minimum values from the list.
# Example Input: [1, 2, 3, 4, 5]
# Example Output: (5, 1)

ip = [1, 2, 3, 4, 5]
op  = (min(ip),max(ip))
print(op)


# 10. Write a Python function that takes a list of integers and returns the sum of all the even
# numbers in the list.
# ○ Example Input: [1, 2, 3, 4, 5]
# ○ Example Output: 6

def even_sum(lst):
    su = 0
    for i in lst:
        if i % 2 == 0:
            su = su + i
    print("Sum of all Even Numbers ", su)
    
inputlist = [1, 2, 3, 4, 5]
even_sum(lst = inputlist)


# 11. Write a Python function that takes a list of integers and returns the second largest element
# in the list. If there is no second largest, return None.
# ○ Example Input: [1, 2, 3, 4, 5]
# ○ Example Output: 4
# ○ Example Input: [5, 5, 5]
# ○ Example Output: None

def second_largest(lst):
    lst.sort(reverse =True)    
    if lst[1] == lst[-0]:
        return None
    else:
        return lst[1]

input = [1, 2, 3, 4, 5]   
print(second_largest(lst = input))
input = [5, 5, 5]
print(second_largest(lst = input))



# 12. Write a Python function that removes all whitespace characters (spaces, tabs, etc.) from a
# string.
# Example Input: "hello world"
# Example Output: helloworld

string = "hello world"
print(''.join(string.split()))


# 13. Write a Python function that takes a string and returns the length of the longest word in
# the string.
# Example Input: "The quick brown fox"
# Example Output: 5


def long_word(st):
    return  max([len(c)  for c in st.split(" ") ])

st = "The quick brown fox"
print(long_word(st))
    


# 14. Write a Python function that prints the multiplication table for a given number from 1 to
# 10.
# ○ Example Input: 3
# ○ Example Output:
# # 3 x 1 = 3
# # 3 x 2 = 6
# # 3 x 3 = 9
# # ...
# # 3 x 10 = 30

def mul_table(num):
    for i in range(1,11):
        print(  num ," x ", i, " = ", num*i )
mul_table(num=3)



# 15. Write a Python function that prints all prime numbers between start and end (inclusive).
# ○ Example Input: 10, 20
# ○ Example Output: 11, 13, 17, 19
# **************

def print_primes(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

print_primes(10, 20)
