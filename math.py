import math

def fibonnaci(n):
  if n<=1:
    return n
  else:
    return fibonnaci(n-1) + fibonnaci(n-2)

def fib_seq(n):
  for i in range(n):
    print(fibonnaci(i),end='')
  print('\n')

#2.factorial of a number
def factorial(n):
  if n<1:
    raise ValueError('Negative factorial does not exist')
  elif n == 1:
    return 1
  else:
    return n*factorial(n-1)

#3.roots of quadratic equation
def roots():
  a = int(input('Enter first term a: '))
  b = int(input('Enter second term b: '))
  c = int(input('Enter constant term c: '))
  print(f'Your quadratic equation would look like this: {a}x^2 + ({b}x) + ({c})')
  x1 = (-b + (b**2 - 4*a*c)**0.5)/2*a
  x2 = (-b - (b**2 - 4*a*c)**0.5)/2*a
  print(f'The two roots of above equation are {x1} and {x2}')

#4.area of triangle
def area_of_triangle(a,b,c):
  s = (a+b+c)/2
  area = round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)
  print(f'The area of triangle with sides {a},{b} and {c} is {area}')

#5.Calculate simple interest (PXRXT)/100
def simple_intr(p,r,t):
  val = (p*r*t)/100
  print(f'Simple interest with principal {p}, rate of interest {r} and time {t} is {val}')

#6.pythagorean triplets upto a range a^2 + b^2 = c^2
def pyth():
  limit = int(input('Enter upper limit: '))
  c = 0
  m = 2
  while (c<limit):
    for n in range(1,m+1):
      a = m*m - n*n
      b = 2*m*n
      c = m*m + n*n
      if (c>limit):
        break
      elif (a == 0 or b == 0 or c == 0):
        break
      else:
        print(a,b,c)
    m=m+1

def main():
  fib_seq(3)
  print(factorial(3))
  #roots()
  area_of_triangle(15,9,7)
  simple_intr(200,5,5)
  pyth()

main()