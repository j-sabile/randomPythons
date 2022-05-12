def per(n):
    n = str(n)
    rep = 0
    while len(n) != 1:
        sum = 1
        for i in range (len(str(n))):
            sum *= int(n[i])
        n = str(sum)
        rep += 1
    return(rep)

while 1:
    try:
        number = int(input("\nThis program multiplies all the digits until 1 digit would be left.\n\nEnter a number: "))
        print("It would take", per(number), "cycle/s to turn it into 1 digit.\n")
        break
    except:
        print("Please enter only a number.")
