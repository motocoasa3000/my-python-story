import math

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's prime number.")
    else:
        print("It's not a prime number.")
        
n = int(input("Insert a number to check if is prime number or not: "))
prime_checker(number=n)
               
                
