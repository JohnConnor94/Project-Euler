# python 3.7.4
"""
I used an iterative approach.
List comprehension would create a very long lists.
This approach tend to have less iteration when you hit a prime factor
because the initial number will be divided at every hit.
In the worst case we have n iteration in prime_factors function because we have inserted a prime number.
In a medium case we have a  m/2 <= n <= m iteration where m is the max prime factor.
"""


def prime_factors(n: int) -> []:
    factors = [1]
    d = 2  # first number
    count = 0  # to save how many iterations are necessary
    while d <= n:
        count += 1
        if n % d == 0:
            factors.append(d)  # found a new prime, save it
            n = n / d
        else:
            if d % 2 == 0:
                d += 1  # if even add 1 to become odd
            else:
                d += 2  # if odd continue add 2 to skip the even numbers
    print(f"Count = {count}")
    return factors


def main():
    n = 0
    try:
        n = int(input("Insert an integer number:"))
    except ValueError as error:
        print(f"{n} is not an integer number!")
        exit(1)

    # get the list
    primes = prime_factors(n)

    print(f"You have inserted {n}")
    print(f"Prime factors of {n}:{primes}")
    # print(f"Max prime factor of {n} : {max(primes)}") # we have primes in ascending order so we can optimize
    print(f"Max prime factor of {n} : {primes[-1]}")
    pass


main()
