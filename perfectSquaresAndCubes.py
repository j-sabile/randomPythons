n = int(input("Enter a number: "))
for i in range (1, n+1):
    if i**2 <= n: 
        print(i**2, "is a perfect square.")
    if i**3 <= n:
        print(i**3, "is a perfect cube.")
