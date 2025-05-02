import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()
s3 = sys.stdin.readline().strip()

fizzbuzz = ['FizzBuzz', 'Fizz', 'Buzz']

if s1 not in fizzbuzz:
    s1 = int(s1)
    s2 = s1 + 1
    s3 = s1 + 2
if s2 not in fizzbuzz:
    s2 = int(s2)
    s1 = s2 - 1
    s3 = s2 + 1
if s3 not in fizzbuzz:
    s3 = int(s3)
    s1 = s3 - 2
    s2 = s3 - 1

s4 = s3 + 1

if s4 % 3 == 0 and s4 % 5 == 0:
    s4 = 'FizzBuzz'
elif s4 % 3 == 0 and not (s4 % 5 == 0):
    s4 = 'Fizz'
elif not (s4 % 3 == 0) and s4 % 5 == 0:
    s4 = 'Buzz'

print(s4)