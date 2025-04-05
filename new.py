##sum of two numbers
def add(a, b):
    return a + b
##subtraction of two numbers
def subtract(a, b):
    return a - b
##multiplication of two numbers
def multiply(a, b):
    return a * b
##division of two numbers
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
##modulus of two numbers
def modulus(a, b):
    return a % b
##exponentiation of two numbers
def exponentiation(a, b):
    return a ** b
##floor division of two numbers
def floor_division(a, b):
    return a // b
##square root of a number
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return a ** 0.5
##factorial of a number
def factorial(n):
    if n < 0:
        raise ValueError("Cannot take factorial of negative number")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
##greatest common divisor of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
##least common multiple of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
##prime number check                                                                                
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
##fibonacci series  
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
##factorial of a number
def factorial(n):
    if n < 0:
        raise ValueError("Cannot take factorial of negative number")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
##sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
##reverse a number                  



def reverse_number(n):
    return int(str(n)[::-1])
##check if a number is palindrome       
def is_palindrome(n):
    return str(n) == str(n)[::-1]
##count the number of digits in a number
def count_digits(n):
    return len(str(abs(n)))
##check if a number is Armstrong number     
def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)
##check if a number is perfect number   
def is_perfect(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
##check if a number is abundant number  
def is_abundant(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum > n
##check if a number is deficient number
def is_deficient(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum < n
##check if a number is triangular number
def is_triangular(n):
    if n < 0:
        return False
    x = (8 * n + 1) ** 0.5
    return x.is_integer() and (x - 1) % 2 == 0
##check if a number is square number    
def is_square(n):
    if n < 0:
        return False
    x = n ** 0.5
    return x.is_integer()
##check if a number is cube number
def is_cube(n):
    if n < 0:
        return False
    x = n ** (1/3)
    return x.is_integer()
##check if a number is even
def is_even(n):
    return n % 2 == 0
##check if a number is odd
def is_odd(n):
    return n % 2 != 0
##check if a number is positive
def is_positive(n):
    return n > 0
##check if a number is negative
def is_negative(n):
    return n < 0
##check if a number is zero
def is_zero(n):
    return n == 0
##check if a number is prime factor
def is_prime_factor(n, factor):
    if n <= 1 or factor <= 1:
        return False
    return n % factor == 0 and is_prime(factor)
##check if a number is composite
def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False
##check if a number is abundant factor
def is_abundant_factor(n, factor):
    if n <= 1 or factor <= 1:
        return False
    return n % factor == 0 and is_abundant(factor)
##check if a number is deficient factor
def is_deficient_factor(n, factor):
    if n <= 1 or factor <= 1:
        return False
    return n % factor == 0 and is_deficient(factor)

##check if a number is perfect factor