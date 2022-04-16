# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 14:07:13 2022

@author: Elif
"""

def frequencyOfList(myString):
    myList = {}
    for char in myString:
        if char in myList:
            myList[char] += 1
        else: 
            myList[char] = 1
    return myList
            


def anagramCheck(a,b):
    return a == b



def anagramSolution(a,b):
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    
    if anagramCheck(sorted_a,sorted_b):
        return "they are anagrams"
    else:
        return anagramDifference(a,b)
    


def charDifference(subjectList,targetList):
    removeChars = 0
    
    for char in subjectList:
        if(char not in targetList) or (subjectList[char] > targetList[char]):
            removeChars += 1
    
    return removeChars


    
def anagramDifference(a,b):
    a_input = frequencyOfList(a)
    b_input = frequencyOfList(b)
    
    removeCharsA = charDifference(a_input, b_input)
    removeCharsB = charDifference(b_input, a_input)
    
    return "\nremove {aChr} characters from '{a}' and {bChr} characters from '{b}'".format(
            a = a,
            aChr = removeCharsA,
            b = b,
            bChr = removeCharsB
            )



def main():
    a = input("a: ")
    b = input("b: ")
    
    print(anagramSolution(a,b))

if __name__ == '__main__':
    main()