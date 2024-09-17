def double_char(str):
  newStr= ""
  for i in range(len(str)):
    newStr+= str[i]*2
  return newStr

# Given a string, return a string where for every char in the original, there are two chars.

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'