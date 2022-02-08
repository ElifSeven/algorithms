#def firstReverse(str):
    #return str[::-1]
#print(firstReverse("I love you so muchh"))


def Reversed(str):
    strlength = len(str)-1
    reversed = ''

    for i in range(strlength,-1,-1):
         reversed += str[i]
    return reversed

print(Reversed(input()))
