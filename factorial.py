import sys

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    nums = sys.argv[1:]
    print('Computing the factorial of nums: ')
    for n in nums:
        n = int(n)
        result = factorial(n)
        print('The factorial of {} is {} '.format(nums,result))