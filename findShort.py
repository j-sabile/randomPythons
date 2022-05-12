def find_short(s):
    s = s.split(" ")
    l = s[0]
    for i in range (len(s)):
        if int((len(s[i]))) < len(l) :
            l = s[i]
    return (len(l))

print(find_short("bitcoin take over the world maybe who knows perhaps")) 
print(find_short("i want to travel the world writing code one day")) 
