# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
def count_code(str):
  count = 0

  s = str.find("co")
  if not s or len(str) < 3:
    return 0

  for i in range(s,len(str)):
    
    if str[i + 3] == 'e':
      count+= 1
      if len(str) > i+4:
        s = str[i+4:].find("co")
  

        
  return count