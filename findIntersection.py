'''
Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
Output: 1,4,13
'''

def FindIntersection(strArr):
  import string
  arrays = [arr_string.split(',') for arr_string in strArr]
  intersection = []

  for num in arrays[0]:
    if num in arrays[1]:
      intersection.append(int(num))

  return ','.join([str(n) for n in sorted(intersection)])
print(FindIntersection(["1,2,3,4,5","2,5,1,6,7,4"]))

