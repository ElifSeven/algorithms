def LongestWord(sen):
    max = 0
    for word in sen.split():
      if (len(word) > max  and word.isalpha()):
        max = len(word)
        largest = word
      # code goes here
    return largest

print(LongestWord(input()))


""" Have the function LongestWord(str) take the str parameter being passed and return the longest word in the string.
If there are two or more words that are the same length, return the first word from the string with that length
"""
