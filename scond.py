# Given a string, return a new string where the first and last chars have been exchanged.

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):

  if len(str) > 1:
    temp=str[0]
    temp0= str[len(str)-1]
    new=""+temp0
    for i in range(1,len(str)-1):
      new+=str[i]
    new+=temp
    return new
  else: 
    return str


# or

def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]