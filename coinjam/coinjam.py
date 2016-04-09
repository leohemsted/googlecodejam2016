from math import sqrt
from itertools import takewhile

def jamcoin_generator(num_digits):
    """
    Return a generator of all valid binary numbers with provided length, that start and end with 1.
    eg jamcoin_generator(4) yields "1001", "1011", "1101", "1001"
    """
    if num_digits == 2:
        yield '11'
        return
    num_digits -= 2
    # format string: put a 1 on beginning and end, convert int to binary, and leftpad the string
    # with the requisite amount of 0s
    format_string = '1{{:0{}b}}1'.format(num_digits)
    for x in range(2 ** num_digits):
        yield format_string.format(x)


def get_jamcoin_divisors(binary_string):
    """
    Given a binary string (e.g. '1001'), return if it's a jamcoin. It is a valid jamcoin if in all
    bases 2 through 10 inclusive, it is not a prime. So the example string is a jamcoin, as all
    interpretations of it have non-trivial factors (not 1 or itself)
    """
    out = []
    for base in range(2, 11):
        num = int(binary_string, base)
        # find a divisor
        for i in range(2, int(sqrt(num))+1):
            if not num % i:
                # we've found a nontrivial divisor!
                # print('{} in base {} equals {} and has non-prime factor {}'.format(binary_string, base, num, i))
                out.append(i)
                break
        else:
            return False
    return out


def main():
    test_cases = int(input())

    for test_case in range(1, test_cases + 1):
        n, j = map(int, input().split())
        print('Case #{}:'.format(test_case))

        jamcoins_found = 0
        for jamcoin in takewhile(lambda x: jamcoins_found < j, jamcoin_generator(n)):
            divisors = get_jamcoin_divisors(jamcoin)
            if divisors:
                jamcoins_found += 1
                print(jamcoin, ' '.join(map(str, divisors)))

main()
