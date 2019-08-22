# python 3.7.4
def sol1(limit) -> int:
    """
    Simple solution with for, C-stylish
    """
    total = 0
    for x in range(limit):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total


def sol2(limit) -> int:
    """
    A little more pythonic solution with list comprehension to generate the list
    """
    total = 0
    numbers = [x for x in range(limit) if x % 3 == 0 or x % 5 == 0]
    for x in numbers:
        total += x
    return total

def sol3(limtit) -> int:
    """
    A third implementation it could be made with iterators to avoid instatiating a list 
    """
    
    // implementation 
    
    pass

def main():
    limit = 1000
    print(sol1(limit))
    print(sol2(limit))
    pass


main()
