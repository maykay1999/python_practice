#1.even or odd
def even_or_odd(sample_no):
  if sample_no %2 == 0:
     print("Number is even")
  else:
     print("Number is odd")

#2.positive or negative
def pos_or_neg(sample_no):
  if sample_no>0:
    print('Positive no')
  else:
    print('Negative no')

#3.odd numbers in a range
def odd(sample_no):
  if sample_no %2 !=0:
    return sample_no
    
def odd_nos(a,b):
  for i in range(a,b):
    print(odd(i))

#4.palindrome
def palindrome(sample_no):
  seq = list(str(sample_no))
  if len(seq) %2 == 0:
    print('Number is not a palindrome')
  elif len(seq) %2 !=0:
    if seq == seq[::-1]:
      print(f'{sample_no} is a palindrome')
    else:
      print(f'{sample_no} is not a palindrome')

#5.reverse a no
def reverse_a_no(sample_no):
  lt = list(str(sample_no))
  no = int(''.join(map(str,lt[::-1])))
  print(no)
    
#6.neither divisible by 2 and 3
def not_div_by_2_or_3():
  for i in range (1,51):
    if i%2 != 0 and i%3 != 0:
      print('neither divisible by 2 or 3 is ',i)

#7.divisible by 7 and multiple of 5
def div_by_7_and_mul_of_5(n):
  for i in range (1,n+1):
    if i%7 == 0 and i%5 == 0:
      print('divisible by 7 and multiple of 5',i)

#8.divisible by a no in a given range
def div(a,b,n):
  for i in range(a,b+1):
    if i % n == 0:
      print('divisible by a number in given range',i)

#9.sum of individual numbers
def sum(sample_no):
  original_no = sample_no
  total = 0
  while(sample_no>0):
    digit = sample_no % 10
    total = total + digit
    sample_no = sample_no // 10
  print(f'The sum of individual numbers {original_no} is ',total)

#10.count digits in a number
def no_count(sample_no):
  print(f'The count of digits in number {sample_no} is ',len(str(sample_no)))

#11.all divisors of an integer
def divisors_of_number(sample_no):
  for i in range(1,sample_no+1):
    if sample_no%i == 0:
      print(i)

#12.binary of integer
def binary(sample_no):
  if sample_no > 1:
    binary(sample_no // 2)
  print(sample_no%2,end='')

#13.print multiplication table of given no
def mul(n):
  print('\n')
  for i in range(1,11):
    print(n,'*',i,' =',n*i)

#14.leap year
def leap(year):
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} is a leap year')
  else:
    print(f'{year} is not a leap year')

#15.prime numbers
'''
To check a prime number start from 2 because 0 and 1 are not prime nos.
if the required no is divisible by a number in range of 2 to half its number
then it is not a prime number.
'''
def prime(n):
  if n > 1:
    for i in range(2,(n//2)+1):
      if n%i == 0:
        print(f'{n} is not a prime number')
        break
    else:
      print(f'{n} is a prime number---')
  else:
    print('Given number is negative so not a prime number')

#16.prime numbers in a given range
def prime_range(a,b):
  for i in range(a,b+1):
    if i>1:
      for k in range(2,i):
        if i%k == 0:
          break
      else:
        print(i)

#17.perfect numbers
#perfect numbers are nos whose divisors sum is equal to the original no
def perfect(no):
  arr = []
  if no>1:
    for i in range(1,no):
      if no%i == 0:
        arr.append(i)
  else:
    print('the number is negative so cannot be a perfect number')
  sum = 0
  for j in arr:
    sum=sum+j
  print(f'The sum of divisors is {sum}')
  if sum == no:
    print('Perfect number')
  else:
    print('Not a perfect no')

#18.Armstrong number
#if sum of cube of digits equal to number then armstrong no.
def armstrong(n):
  list_of_nos = map(int,str(n))
  sum = 0
  for i in list_of_nos:
    sum = sum + i*i*i
  if sum == n:
    print(f'{n} is an armstrong number')
  else:
    print(f'{n} is not an armstrong number')

#19.sum of n natural numbers
def sum_of_n_nos(n):
  sum = 0
  for i in range(1,n+1):
    sum = sum + i
  print(f'Sum of n natural numbers is {sum}')

#20.strong number
#number whose sum of factorial of individual nos is equal to original no.
def factorial(no):
  if no == 1:
    return 1
  else:
    return no*factorial(no-1)

def strong(sample_no):
  digits = map(int,str(sample_no))
  sum = 0
  for i in digits:
    sum = sum + factorial(i)
  if sum == sample_no:
    print(f'{sample_no} is an strong number')
  else:
    print(f'{sample_no} is not an strong number')

#21.prime factors
"""
2 | 630<--- no & LHS is divisor.
3 | 315
3 | 105
3 | 35
5 | 7
7 | 1
"""
def prime_factors(no):
  factors = []
  divisor = 2
  while divisor<=no:
    if no%divisor ==  0:
      factors.append(divisor)
      no = no/divisor
    else:
      divisor = divisor + 1
  print(f'The prime factors of number are {factors}')

#22.amicable numbers
# two such nos whose sum of both divisors should be equal to each other
def factors(no):
  fact = []
  divisor = 2
  for j in range(2,no+1):
    if no%j == 0:
      fact.append(j)
    else:
      divisor+=1
  sum = 0
  for i in fact:
    sum = sum + i
  return sum

def amicable_nos(a,b):
  if factors(a)==factors(b):
    print(f'{a} and {b} are amicable numbers')
  else:
    print('Numbers are not amicable!')

#23.power using recursion
def power(x, y):
  if y == 0:
      return 1
  if y >= 1:
      return x * power(x, y - 1)

#24.all possible combination of three digits
def combo(a,b,c):
  d = []
  d.append(a)
  d.append(b)
  d.append(c)
  for i in range(0,3):
    for j in range(0,3):
      for k in range(0,3):
        if(i!=j & j!=k & k!=i):
          print(d[i],d[j],d[k])


def main():
  even_or_odd(4)
  even_or_odd(5)
  pos_or_neg(3)
  pos_or_neg(-1)
  odd_nos(3,10)
  palindrome(12321)
  palindrome(12345)
  reverse_a_no(32748)
  not_div_by_2_or_3()
  div_by_7_and_mul_of_5(100)
  div(1,100,5)
  sum(123)
  no_count(32847582)
  divisors_of_number(25)
  binary(34)
  mul(5)
  leap(2024)
  prime(11)
  prime_range(10,20)
  perfect(6)
  armstrong(153)
  sum_of_n_nos(3)
  strong(145)
  prime_factors(630)
  amicable_nos(220,284)
  print(power(5,2))
  combo(1,2,3)

main()