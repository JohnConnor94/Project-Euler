# python 3.7.4
def fibonacci(upper_limit: int) -> []:
    """
    Creates a list of elements of fibonacci series starting from 1-2... and stopping at upper_limit
    :param upper_limit: all elements of this series are minor than upper_limit
    :return: list containing the elements of fibonacci
    """
    lista = [1, 2]

    while lista[-1] <= upper_limit:
        # add the new element of the series
        lista.append(lista[-1] + lista[-2])

    # remove the last if exceeds the upper limit
    # if lista[-1] > upper_limit:
    # print(f"Removed last element 'cause it exceeds {upper_limit} -> last element = {lista[-1]}")
    # lista.pop()

    # remove last element because it exceeds the upper limit
    lista.pop()
    return lista


def main():
    limit = 4 * 10 ** 6
    lista = list(filter(lambda n: n % 2 == 0, fibonacci(limit)))

    total = 0
    for x in lista:
        total += x

    print(f"Upper limit = {limit}")
    print(f"The sum of all fibonacci'series elements below {limit} (included) is {total}")
    pass


main()
