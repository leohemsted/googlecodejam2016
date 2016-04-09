from itertools import takewhile, count
test_cases = int(input())

for test_case in range(1, test_cases + 1):
    n = int(input())
    if n == 0:
        print('Case #{}: INSOMNIA'.format(test_case))
        continue


    chars_seen = set()

    for i in takewhile(lambda x: len(chars_seen) != 10, count(start=1)):
        chars_seen.update(c for c in str(i * n))
    print('Case #{}: {}'.format(test_case, i * n))
