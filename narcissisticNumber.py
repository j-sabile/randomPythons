'''
In number theory, a narcissistic number in a given number base b
is a number that is the sum of its own digits each raised to the
power of the number of digits.
'''

n = input("\nEnter a number: ")

sum = 0
for i in range (len(n)):
    sum = sum + (int(n[i])**(len(n)))

if sum == int(n):
    print(n, "is a narcissistic number.")
else:
    print(n, "is not a narcissistic number.")
