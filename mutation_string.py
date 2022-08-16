"""
Task
Read a given string, change the character at a given index and then print the modified string.
Function Description

Complete the mutate_string function in the editor below.

mutate_string has the following parameters:

string string: the string to change
int position: the index to insert the character at
string character: the character to insert

"""

def mutate_string(string, position, character):
   
    string = string[:position] + character + string[position+1:]
    print(string)
        
    
    

if __name__ == '__main__':
    s = 'abracadabra'   
    i = 5
    c= 'k'
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    

## Another SOLUTION
""""
def mutate_string(string, position, character):
    new_string = []
    for i in range(0, len(string)):
        
        if i == position:
           new_string.append( string[i].replace(string[i],character))
        elif  i != position:   
            new_string.append(string[i])
    s = ''.join(str(x) for x in new_string)
    return s


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
"""
